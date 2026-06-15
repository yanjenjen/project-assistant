from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

from pypdf import PdfReader


PDF_ANNOTATED = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案\0608資料更新\Doc-01-專案範圍與需求規格書 1.0(請修改).pdf")
PDF_REVISED = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案\0612資料更新\DOC-01專案範圍與需求規格書2.0.pdf")
OUT_DIR = Path(r"C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\tmp\pdfs\doc01_compare")


IGNORE_SUBTYPES = {"/Popup", "/Link"}


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


def clean_text(text: str) -> str:
    text = text.replace("\u3000", " ")
    text = re.sub(r"\s+", "", text)
    return text


def extract_text_pages(path: Path) -> list[str]:
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
            if subtype in IGNORE_SUBTYPES:
                continue
            content = str(obj.get("/Contents", "") or "").strip()
            subject = str(obj.get("/Subj", "") or "").strip()
            author = str(obj.get("/T", "") or "").strip()
            modified = str(obj.get("/M", "") or "").strip()
            rect_raw = obj.get("/Rect") or []
            rect = [float(x) for x in rect_raw]
            rows.append(
                Annotation(
                    no=no,
                    page=page_index,
                    subtype=subtype,
                    subject=subject,
                    author=author,
                    modified=modified,
                    content=content,
                    rect=rect,
                )
            )
            no += 1
    return rows


def context_for_page(text: str, limit: int = 700) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def nearby_pages(pages: list[str], page_no: int, radius: int = 1) -> str:
    start = max(1, page_no - radius)
    end = min(len(pages), page_no + radius)
    return "\n".join(pages[i - 1] for i in range(start, end + 1))


def candidate_status(annotation: Annotation, revised_pages: list[str]) -> dict[str, Any]:
    content = annotation.content.strip()
    clean_content = clean_text(content)
    all_revised_clean = clean_text("\n".join(revised_pages))
    local_revised_clean = clean_text(nearby_pages(revised_pages, annotation.page, radius=1))

    appears_global = bool(clean_content and clean_content in all_revised_clean)
    appears_local = bool(clean_content and clean_content in local_revised_clean)

    status = "需人工確認"
    evidence = ""

    if not content:
        status = "需依畫面確認"
        evidence = "刪除線或標記無文字內容，需比對原頁面位置。"
    elif annotation.subtype == "/StrikeOut":
        if appears_global:
            status = "疑似未刪除"
            evidence = "被刪除線標示的文字仍出現在 2.0。"
        else:
            status = "可能已刪除"
            evidence = "被刪除線標示的文字未在 2.0 文字層找到。"
    elif annotation.subtype in {"/Caret", "/Text"}:
        if appears_global:
            status = "可能已加入"
            evidence = "註解文字可在 2.0 找到。"
        else:
            status = "未找到註解文字"
            evidence = "註解文字未在 2.0 文字層找到。"
    elif annotation.subtype == "/Highlight":
        if appears_global:
            status = "標註文字仍存在"
            evidence = "Highlight 的內容在 2.0 仍可找到，需判斷是否只是標註參考或仍未調整。"
        else:
            status = "標註文字已變更或移除"
            evidence = "Highlight 的內容未在 2.0 文字層找到。"

    return {
        "status": status,
        "evidence": evidence,
        "appears_global": appears_global,
        "appears_local": appears_local,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    annotations = extract_annotations(PDF_ANNOTATED)
    original_pages = extract_text_pages(PDF_ANNOTATED)
    revised_pages = extract_text_pages(PDF_REVISED)

    records = []
    for annot in annotations:
        status = candidate_status(annot, revised_pages)
        record = asdict(annot)
        record.update(status)
        record["original_page_context"] = context_for_page(original_pages[annot.page - 1])
        record["revised_nearby_context"] = context_for_page(nearby_pages(revised_pages, annot.page, radius=1), limit=1000)
        records.append(record)

    (OUT_DIR / "annotations_1_0.json").write_text(
        json.dumps([asdict(a) for a in annotations], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT_DIR / "comparison_records.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    with (OUT_DIR / "comparison_records.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "no",
                "page",
                "subtype",
                "subject",
                "author",
                "modified",
                "content",
                "status",
                "evidence",
                "appears_global",
                "appears_local",
            ],
        )
        writer.writeheader()
        for record in records:
            writer.writerow({key: record.get(key, "") for key in writer.fieldnames})

    print(json.dumps({
        "annotation_count": len(annotations),
        "original_pages": len(original_pages),
        "revised_pages": len(revised_pages),
        "output_dir": str(OUT_DIR),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
