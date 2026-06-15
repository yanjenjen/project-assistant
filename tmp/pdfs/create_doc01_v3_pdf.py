from __future__ import annotations

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


SRC = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案\0612資料更新\DOC-01專案範圍與需求規格書2.0.pdf")
OUT_DIR = Path(r"C:\Users\jenny.lu\Documents\建大輪胎專案\期中交付文件")
OUT = OUT_DIR / "DOC-01專案範圍與需求規格書3.0.pdf"

FONT = "MSung-Light"
TEXT = HexColor("#333333")
MUTED = HexColor("#b9a7ad")
GRID = HexColor("#dfc7cc")
LIGHT_ROW = HexColor("#fff7f8")


pdfmetrics.registerFont(UnicodeCIDFont(FONT))


def y_from_top(page_height: float, top: float) -> float:
    return page_height - top


def rect_from_top(c: canvas.Canvas, page_height: float, x: float, top: float, w: float, h: float, color=white) -> None:
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.rect(x, page_height - top - h, w, h, stroke=0, fill=1)


def draw_text(c: canvas.Canvas, x: float, y: float, text: str, size: float = 8.5, color=TEXT) -> None:
    c.setFillColor(color)
    c.setFont(FONT, size)
    c.drawString(x, y, text)


def wrap_text(text: str, max_chars: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        if len(current) >= max_chars and ch not in "，、。）)；;":
            lines.append(current)
            current = ch
        else:
            current += ch
    if current:
        lines.append(current)
    return lines


def draw_wrapped(c: canvas.Canvas, x: float, y: float, text: str, max_chars: int, size: float = 7.4, leading: float = 11) -> None:
    for idx, line in enumerate(wrap_text(text, max_chars)):
        draw_text(c, x, y - idx * leading, line, size=size)


def footer_version(c: canvas.Canvas, page_w: float, page_h: float) -> None:
    rect_from_top(c, page_h, 531, 811.5, 25, 13, white)
    draw_text(c, 535.5, 20.5, "v3.0", size=7.5, color=MUTED)


def page_overlay(page_no: int, page_w: float, page_h: float) -> BytesIO:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_w, page_h))

    footer_version(c, page_w, page_h)

    if page_no == 1:
        rect_from_top(c, page_h, 476, 132, 28, 14, white)
        draw_text(c, 479.5, y_from_top(page_h, 142.4), "v3.0", size=8.5, color=MUTED)
        rect_from_top(c, page_h, 160, 676, 38, 18, white)
        draw_text(c, 164.5, y_from_top(page_h, 690), "v3.0", size=11)
        rect_from_top(c, page_h, 160, 703, 88, 18, white)
        draw_text(c, 164.5, y_from_top(page_h, 717), "2026-06-15", size=11)

    if page_no == 4:
        rect_from_top(c, page_h, 126, 257, 34, 17, white)
        draw_text(c, 131.3, y_from_top(page_h, 270), "v3.0", size=9)
        rect_from_top(c, page_h, 126, 284, 74, 17, white)
        draw_text(c, 131.3, y_from_top(page_h, 297), "2026-06-15", size=9)
        # Redraw the last revision-record row as a clean v3.0 row.
        rect_from_top(c, page_h, 44, 714, 509, 60, white)
        c.setStrokeColor(GRID)
        c.setFillColor(LIGHT_ROW)
        c.rect(44.8, page_h - 774, 506, 60, stroke=1, fill=1)
        for x in [44.8, 82, 138, 174, 550.8]:
            c.line(x, page_h - 714, x, page_h - 774)
        draw_text(c, 53.2, y_from_top(page_h, 733), "v3.0", size=8)
        draw_text(c, 91, y_from_top(page_h, 728), "2026-", size=8)
        draw_text(c, 91, y_from_top(page_h, 742), "06-15", size=8)
        draw_text(c, 148, y_from_top(page_h, 728), "艾創", size=8)
        draw_text(c, 148, y_from_top(page_h, 742), "點", size=8)
        draw_wrapped(
            c,
            181,
            y_from_top(page_h, 729),
            "依客戶審閱意見補正：天津廠/內胎名詞、三層報價與拆單表述、外部顧問殘留及教育訓練說明會。",
            max_chars=39,
            size=7.8,
            leading=10,
        )

    if page_no == 8:
        # Add two terms below the existing glossary table.
        x0, x1 = 44.8, 550.8
        col1, col2 = 105.5, 274.0
        top = 535.0
        row_h = 27.0
        c.setStrokeColor(GRID)
        c.setLineWidth(0.6)
        for i in range(2):
            y = page_h - top - (i + 1) * row_h
            c.setFillColor(LIGHT_ROW if i % 2 == 0 else white)
            c.rect(x0, y, x1 - x0, row_h, stroke=1, fill=1)
        for x in [x0, col1, col2, x1]:
            c.line(x, page_h - top, x, page_h - top - 2 * row_h)
        c.line(x0, page_h - top - row_h, x1, page_h - top - row_h)
        draw_text(c, 53, page_h - top - 17, "Tianjin", size=8.7)
        draw_text(c, 112, page_h - top - 17, "Kenda Tianjin", size=8.7)
        draw_text(c, 280, page_h - top - 17, "建大天津廠（生產廠；正式代號依建大主檔）", size=8.2)
        draw_text(c, 53, page_h - top - row_h - 17, "內胎", size=8.7)
        draw_text(c, 112, page_h - top - row_h - 17, "Tube", size=8.7)
        draw_text(c, 280, page_h - top - row_h - 17, "內胎產品別；與 TT / TL 規格標示區分", size=8.2)

    if page_no == 10:
        # Clarify out-of-scope three-tier pricing versus checkout split rule.
        rect_from_top(c, page_h, 50, 222, 498, 61, white)
        c.setStrokeColor(GRID)
        c.setFillColor(LIGHT_ROW)
        c.rect(44.8, page_h - 283, 506, 61, stroke=1, fill=1)
        c.line(171, page_h - 222, 171, page_h - 283)
        draw_wrapped(c, 53, page_h - 236, "三層報價功能（經銷商階層定價結構）", max_chars=12, size=8.0, leading=10)
        draw_wrapped(
            c,
            179,
            page_h - 236,
            "指依經銷商階層（例如一級／二級）建立之多層報價結構，非本案範圍；本案結帳自動拆單僅依報價單號＋包裝單位，請勿與三層報價功能混淆。",
            max_chars=45,
            size=7.4,
            leading=10,
        )

    if page_no == 20:
        rect_from_top(c, page_h, 101, 675, 282, 16, white)
        draw_text(c, 103, y_from_top(page_h, 687), "退貨流程、三層報價功能等複雜功能不含於本案範圍，列入後續版本", size=8.2)

    if page_no == 21:
        # AS-05
        rect_from_top(c, page_h, 106, 223, 430, 24, white)
        draw_wrapped(
            c,
            109.5,
            y_from_top(page_h, 234),
            "艾創點提供操作手冊及「經銷商網路下單平台_教育訓練說明會」；建大負責內部推廣與學員安排。",
            max_chars=42,
            size=7.7,
            leading=10,
        )
        # Responsible party: remove external consultant.
        rect_from_top(c, page_h, 499, 562, 45, 16, white)
        draw_text(c, 504, y_from_top(page_h, 575), "建大資訊", size=8.2)

    if page_no == 22:
        rect_from_top(c, page_h, 88, 256, 170, 18, white)
        draw_text(c, 89.5, y_from_top(page_h, 270), "建大業務確認業績/獎金計算邏輯", size=9.0)
        rect_from_top(c, page_h, 52, 596, 290, 18, white)
        draw_text(c, 53.2, y_from_top(page_h, 609), "操作手冊及經銷商網路下單平台教育訓練說明會完成", size=8.2)

    if page_no == 24:
        # Appendix title version/date.
        rect_from_top(c, page_h, 43, 78, 510, 54, white)
        rect_from_top(c, page_h, 43, 124, 510, 34, white)
        draw_text(c, 44, y_from_top(page_h, 106), "附錄 A：客戶審閱意見回覆對照表", size=16)
        draw_text(c, 294, y_from_top(page_h, 104), "（v1.1 → v3.0，2026-06-15）", size=12)
        c.setStrokeColor(HexColor("#d20a2e"))
        c.setLineWidth(2.0)
        c.line(44, page_h - 147, 550, page_h - 147)
        # A-05 response/status.
        rect_from_top(c, page_h, 265, 441, 286, 185, white)
        c.setStrokeColor(GRID)
        for top_line in [441, 505, 561, 625]:
            c.line(265, page_h - top_line, 550.8, page_h - top_line)
        for x in [265, 495, 550.8]:
            c.line(x, page_h - 441, x, page_h - 625)
        draw_wrapped(
            c,
            270,
            y_from_top(page_h, 459),
            "已補列 Tianjin／建大天津廠及「內胎」名詞；正式代號仍以建大提供之廠別/產品主檔為準",
            max_chars=28,
            size=6.6,
            leading=9,
        )
        draw_text(c, 505, y_from_top(page_h, 459), "✅ 已修", size=6.6)
        draw_text(c, 505, y_from_top(page_h, 468), "訂", size=6.6)
        # A-06 and A-07 response/status.
        draw_wrapped(
            c,
            270,
            y_from_top(page_h, 515),
            "已澄清：三層報價功能不在本案範圍；本案結帳自動拆單僅依報價單號＋包裝單位。",
            max_chars=29,
            size=6.7,
            leading=9,
        )
        draw_text(c, 505, y_from_top(page_h, 515), "✅ 已澄", size=6.6)
        draw_text(c, 505, y_from_top(page_h, 524), "清", size=6.6)
        draw_wrapped(
            c,
            270,
            y_from_top(page_h, 571),
            "文件拆單規則明定為二層：報價單號＋包裝單位；取消廢胎費及三層拆單相關敘述。",
            max_chars=29,
            size=6.7,
            leading=9,
        )
        draw_text(c, 505, y_from_top(page_h, 571), "✅ 已修", size=6.6)
        draw_text(c, 505, y_from_top(page_h, 580), "訂", size=6.6)

    if page_no == 25:
        # Add A-19 for training note in remaining white space above legend.
        rect_from_top(c, page_h, 44, 696, 507, 42, white)
        c.setStrokeColor(GRID)
        c.setFillColor(LIGHT_ROW)
        c.rect(44.8, page_h - 738, 506, 42, stroke=1, fill=1)
        c.line(73, page_h - 696, 73, page_h - 738)
        c.line(117, page_h - 696, 117, page_h - 738)
        c.line(267, page_h - 696, 267, page_h - 738)
        c.line(495, page_h - 696, 495, page_h - 738)
        draw_text(c, 52, page_h - 710, "A-", size=6.5)
        draw_text(c, 52, page_h - 719, "19", size=6.5)
        draw_text(c, 78, page_h - 710, "AS-05", size=6.5)
        draw_text(c, 78, page_h - 719, "訓練", size=6.5)
        draw_wrapped(c, 122, page_h - 710, "經銷商網路下單平台_教育訓練說明會", max_chars=15, size=6.5, leading=8)
        draw_wrapped(
            c,
            272,
            page_h - 710,
            "AS-05 已改列操作手冊及教育訓練說明會，並保留建大內部推廣分工",
            max_chars=28,
            size=6.4,
            leading=8,
        )
        draw_text(c, 502, page_h - 710, "✅ 已修", size=6.3)
        draw_text(c, 502, page_h - 718, "訂", size=6.3)

    c.save()
    buf.seek(0)
    return buf


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(str(SRC))
    writer = PdfWriter()
    for idx, page in enumerate(reader.pages, start=1):
        page_w = float(page.mediabox.width)
        page_h = float(page.mediabox.height)
        overlay_pdf = PdfReader(page_overlay(idx, page_w, page_h))
        page.merge_page(overlay_pdf.pages[0])
        writer.add_page(page)

    with OUT.open("wb") as f:
        writer.write(f)

    print(OUT)


if __name__ == "__main__":
    main()
