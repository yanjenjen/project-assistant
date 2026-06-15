from __future__ import annotations

import json
import re
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import pypdfium2 as pdfium
from pypdf import PdfReader


ROOT = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案")
SRC_1 = ROOT / "0608資料更新"
SRC_2 = ROOT / "0612資料更新"
OUT_ROOT = ROOT / "期中交付文件" / "工作包"


@dataclass
class PdfDoc:
    doc_id: str
    version_key: str
    source_path: Path
    title: str


@dataclass
class Annotation:
    no: int
    page: int
    subtype: str
    subject: str
    author: str
    modified: str
    content: str
    rect: list[float]


def resolve(value: Any) -> Any:
    return value.get_object() if hasattr(value, "get_object") else value


def normalize_doc_id(name: str) -> str:
    match = re.search(r"DOC[-_ ]?0?(\d+)", name, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot parse DOC id from {name}")
    return f"DOC-{int(match.group(1)):02d}"


def clean_title(name: str, doc_id: str) -> str:
    title = Path(name).stem
    title = re.sub(r"(?i)^DOC[-_ ]?0?\d+[-_ ]*", "", title)
    title = re.sub(r"\s*1\.0\(請修改\)\s*$", "", title)
    title = re.sub(r"\s*2\.0\s*$", "", title)
    title = title.strip("-_ ")
    return title or doc_id


def collect_docs() -> list[PdfDoc]:
    docs: list[PdfDoc] = []
    for version_key, src in [("1.0_請修改", SRC_1), ("2.0", SRC_2)]:
        for path in sorted(src.glob("DOC-*.pdf")):
            doc_id = normalize_doc_id(path.name)
            docs.append(PdfDoc(doc_id=doc_id, version_key=version_key, source_path=path, title=clean_title(path.name, doc_id)))
    return docs


def page_texts(path: Path) -> list[str]:
    reader = PdfReader(str(path))
    return [page.extract_text() or "" for page in reader.pages]


def extract_annotations(path: Path) -> list[Annotation]:
    reader = PdfReader(str(path))
    rows: list[Annotation] = []
    no = 1
    for page_index, page in enumerate(reader.pages, start=1):
        annots = resolve(page.get("/Annots")) or []
        for annot_ref in annots:
            obj = resolve(annot_ref)
            subtype = str(obj.get("/Subtype", ""))
            if subtype in {"/Popup", "/Link"}:
                continue
            rect_raw = obj.get("/Rect") or []
            rows.append(
                Annotation(
                    no=no,
                    page=page_index,
                    subtype=subtype,
                    subject=str(obj.get("/Subj", "") or "").strip(),
                    author=str(obj.get("/T", "") or "").strip(),
                    modified=str(obj.get("/M", "") or "").strip(),
                    content=str(obj.get("/Contents", "") or "").strip(),
                    rect=[float(x) for x in rect_raw],
                )
            )
            no += 1
    return rows


def write_content_md(path: Path, texts: list[str], source_path: Path, doc: PdfDoc) -> None:
    lines = [
        f"# {doc.doc_id} {doc.title} - {doc.version_key} 正文抽取",
        "",
        f"- 來源檔：`{source_path}`",
        f"- 頁數：{len(texts)}",
        "",
    ]
    for idx, text in enumerate(texts, start=1):
        lines.extend(
            [
                f"## 第 {idx} 頁",
                "",
                (text.strip() or "_本頁未抽取到文字_"),
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_annotations_md(path: Path, annotations: list[Annotation], source_path: Path, doc: PdfDoc) -> None:
    lines = [
        f"# {doc.doc_id} {doc.title} - {doc.version_key} 註解抽取",
        "",
        f"- 來源檔：`{source_path}`",
        f"- 實際註解數：{len(annotations)}",
        "",
    ]
    if not annotations:
        lines.append("_未讀取到 PDF 註解/標示。_")
    for ann in annotations:
        lines.extend(
            [
                f"## {ann.no}. 第 {ann.page} 頁 - {ann.subtype}",
                "",
                f"- 主旨：{ann.subject or '(空)'}",
                f"- 作者：{ann.author or '(空)'}",
                f"- 修改時間：{ann.modified or '(空)'}",
                f"- 座標：{ann.rect}",
                "",
                "```text",
                ann.content or "(無文字內容，需看頁面圖片確認標示位置)",
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def render_pages(pdf_path: Path, pages_dir: Path, scale: float = 1.6) -> list[dict[str, Any]]:
    pages_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(pdf_path))
    rendered: list[dict[str, Any]] = []
    for idx in range(len(pdf)):
        page_no = idx + 1
        out = pages_dir / f"page-{page_no:03d}.png"
        page = pdf[idx]
        image = page.render(scale=scale).to_pil()
        image.save(out)
        rendered.append({"page": page_no, "image": str(out), "size": image.size})
    return rendered


def build_workpack(doc: PdfDoc) -> dict[str, Any]:
    out_dir = OUT_ROOT / doc.doc_id / doc.version_key
    pages_dir = out_dir / "pages"
    out_dir.mkdir(parents=True, exist_ok=True)

    source_copy = out_dir / doc.source_path.name
    shutil.copy2(doc.source_path, source_copy)

    texts = page_texts(doc.source_path)
    annotations = extract_annotations(doc.source_path)
    rendered = render_pages(doc.source_path, pages_dir)

    write_content_md(out_dir / "content.md", texts, doc.source_path, doc)
    write_annotations_md(out_dir / "annotations.md", annotations, doc.source_path, doc)

    manifest = {
        "doc_id": doc.doc_id,
        "title": doc.title,
        "version_key": doc.version_key,
        "source_path": str(doc.source_path),
        "source_copy": str(source_copy),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "page_count": len(texts),
        "annotation_count": len(annotations),
        "rendered_pages": rendered,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def write_index(manifests: list[dict[str, Any]]) -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for manifest in manifests:
        grouped.setdefault(manifest["doc_id"], []).append(manifest)

    lines = [
        "# 建大 DOC PDF 工作包索引",
        "",
        f"- 產生時間：{datetime.now().isoformat(timespec='seconds')}",
        f"- 工作包根目錄：`{OUT_ROOT}`",
        "",
    ]
    for doc_id in sorted(grouped):
        lines.extend([f"## {doc_id}", ""])
        for manifest in sorted(grouped[doc_id], key=lambda m: m["version_key"]):
            rel = Path(manifest["source_copy"]).parent
            lines.append(
                f"- `{manifest['version_key']}`：{manifest['page_count']} 頁，"
                f"{manifest['annotation_count']} 筆註解，資料夾 `{rel}`"
            )
        lines.append("")
    (OUT_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT_ROOT / "index.json").write_text(json.dumps(manifests, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    docs = collect_docs()
    manifests = [build_workpack(doc) for doc in docs]
    write_index(manifests)
    print(json.dumps({"count": len(manifests), "out_root": str(OUT_ROOT)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
