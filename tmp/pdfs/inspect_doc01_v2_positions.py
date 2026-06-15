from __future__ import annotations

from pathlib import Path

import pdfplumber


PDF = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案\0612資料更新\DOC-01專案範圍與需求規格書2.0.pdf")

TERMS = [
    "建達顧問",
    "AS-05",
    "使用者訓練",
    "使⽤者訓練",
    "三層",
    "報價拆分三層",
    "KC / KT",
    "TT / TL",
    "A-05",
    "A-07",
    "v1.2",
    "文件版本",
]


def main() -> None:
    with pdfplumber.open(str(PDF)) as pdf:
        for page_no in [1, 4, 7, 8, 10, 20, 21, 22, 23, 24, 25]:
            page = pdf.pages[page_no - 1]
            print(f"\n=== page {page_no} size={page.width}x{page.height} ===")
            text = page.extract_text() or ""
            print(text[:1200].replace("\n", " | "))
            words = page.extract_words(x_tolerance=2, y_tolerance=3, keep_blank_chars=False)
            for term in TERMS:
                hits = [w for w in words if term in w["text"]]
                for hit in hits[:10]:
                    print(
                        "HIT",
                        term,
                        {
                            "text": hit["text"],
                            "x0": round(hit["x0"], 2),
                            "top": round(hit["top"], 2),
                            "x1": round(hit["x1"], 2),
                            "bottom": round(hit["bottom"], 2),
                        },
                    )


if __name__ == "__main__":
    main()
