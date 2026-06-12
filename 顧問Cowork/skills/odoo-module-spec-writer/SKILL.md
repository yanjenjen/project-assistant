---
name: odoo-module-spec-writer
description: >
  為 Odoo yc_* 自研模組撰寫中英文系統功能使用說明書（.docx）。
  凡是遇到「幫我寫說明書」、「這個模組要寫使用手冊」、「系統功能說明書」、
  「模組說明文件」、「使用說明」、「write spec」、「user manual」等請求，
  立即使用此 skill。流程包含：閱讀原始碼確認功能範圍、規劃章節架構、
  生成系統介面 mockup 圖片（中英混合字型）、組裝 Word 文件。
---

# Odoo 模組系統功能說明書製作

## 標準工作流程

收到說明書需求後，**依序執行，不跳步驟**：

1. **閱讀模組原始碼**，確認功能範圍
2. **規劃章節架構**，等使用者確認
3. **生成系統介面 mockup 圖片**
4. **組裝 Word 文件**（使用 docx skill）
5. **提供下載連結**

---

## Step 1：閱讀模組原始碼

```bash
# 列出所有檔案
find /模組路徑 -type f | sort

# 重點閱讀順序：
# 1. __manifest__.py   → 模組名稱、依賴、版本
# 2. models/           → 欄位定義、業務邏輯
# 3. views/            → 畫面結構、按鈕、wizard 入口
# 4. wizard/           → 彈出操作流程
# 5. reports/          → 報表功能
# 6. data/             → 預設值、選項清單
```

閱讀完成後，整理：
- 模組解決什麼問題
- 影響哪些 Odoo 功能區塊（PO / SO / 發票 / 付款 / 庫存 / 報表）
- 適用哪些角色（採購 / 業務 / 財務 / 主管）
- 有哪些關鍵欄位與操作限制

---

## Step 2：規劃章節架構

依功能流向排章節，標準結構如下（依模組複雜度增減）：

| 章節 | 內容 |
|---|---|
| 第一章　功能概覽 | 問題背景、適用對象表格、功能流程地圖（圖） |
| 第 N 章　[功能區塊] | 啟用步驟、欄位說明表格、操作說明、注意事項 |
| 最後一章　常見問題 | FAQ 格式，8-10 個常見狀況與處理方式 |

規劃完成後，**以條列方式整理給使用者確認，等確認後才進入 Step 3**。

---

## Step 3：生成系統介面 mockup 圖片

### 字型規則（嚴格遵守）

| 字元類型 | 使用字型 | 說明 |
|---|---|---|
| CJK 中文字 | `DroidSansFallback` | /usr/share/fonts 下可用 |
| 英文 / 數字 / 符號 | `LiberationSans` | 確保 Latin 字元不變方塊 |

**禁止**單獨使用 DroidSansFallbackFull 繪製混合文字，會導致英文/數字變空白方塊 □。

### 混合字型繪製函式（必用此模式）

```python
from PIL import Image, ImageDraw, ImageFont
import unicodedata, os

def get_font(size, bold=False):
    """取得中英字型"""
    cjk_fonts = [
        '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
        '/usr/share/fonts/truetype/droid/DroidSansFallback.ttf',
    ]
    latin_fonts = [
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
        '/usr/share/fonts/truetype/freefont/FreeSans.ttf',
    ]
    cjk_font = None
    for f in cjk_fonts:
        if os.path.exists(f):
            cjk_font = ImageFont.truetype(f, size)
            break
    latin_font = None
    for f in latin_fonts:
        if os.path.exists(f):
            latin_font = ImageFont.truetype(f, size)
            break
    if cjk_font is None:
        cjk_font = ImageFont.load_default()
    if latin_font is None:
        latin_font = cjk_font
    return cjk_font, latin_font

def is_cjk(char):
    """判斷是否為 CJK 字元"""
    cp = ord(char)
    return (
        0x4E00 <= cp <= 0x9FFF or   # CJK Unified
        0x3400 <= cp <= 0x4DBF or   # CJK Extension A
        0xF900 <= cp <= 0xFAFF or   # CJK Compatibility
        0x3000 <= cp <= 0x303F or   # CJK Symbols
        0xFF00 <= cp <= 0xFFEF       # Halfwidth/Fullwidth
    )

def draw_mixed_text(draw, pos, text, size, color='#333333'):
    """混合中英文繪製，逐字判斷字型"""
    cjk_font, latin_font = get_font(size)
    x, y = pos
    for char in text:
        font = cjk_font if is_cjk(char) else latin_font
        draw.text((x, y), char, font=font, fill=color)
        bbox = font.getbbox(char)
        x += bbox[2] - bbox[0]
```

### mockup 圖片規格

```python
# 標準尺寸與配色
IMG_WIDTH = 900
IMG_HEIGHT = 依內容調整（通常 400-600）
BG_COLOR = '#F8F9FA'        # 淺灰背景（模擬 Odoo 介面）
HEADER_COLOR = '#875A7B'    # Odoo 紫色標題列
BORDER_COLOR = '#DEE2E6'    # 邊框
LABEL_COLOR = '#6C757D'     # 欄位標籤
VALUE_COLOR = '#333333'     # 欄位值
BLUE_COLOR = '#007BFF'      # 勾選框 / 按鈕
GREEN_COLOR = '#28A745'     # 成功狀態

# 每張圖下方加上圖例說明
caption = '▲ 圖說文字（中英混合）'
```

### 圖片數量與內容建議

每個主要功能區塊一張圖，通常 6-10 張：
- 流程地圖（第一章用）
- 每個操作畫面一張（PO / SO / 帳單 / 付款 wizard / 報表 等）

---

## Step 4：組裝 Word 文件

使用 **docx skill**（先讀取 docx/SKILL.md），再依以下規格組裝：

### 字型設定（Word XML 層級）

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_run_font(run, latin='Arial', east_asia='Microsoft JhengHei'):
    """設定中英文字型"""
    rPr = run._r.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), latin)
    rFonts.set(qn('w:hAnsi'), latin)
    rFonts.set(qn('w:cs'), latin)
    rFonts.set(qn('w:eastAsia'), east_asia)
    rPr.insert(0, rFonts)
```

### 文件結構規範

```
封面頁
  模組名稱（中文大標）
  模組名稱（英文小標）
  「使用說明書」
  ▲ 功能流程地圖圖片
  版本資訊（右下角）

各章節
  標題：第 N 章　章節名稱
  小節：N.M　小節名稱
  操作步驟：編號清單
  欄位說明：三欄表格（欄位名稱 / 說明 / 備註）
  圖片：段落內嵌，下方加 ▲ 說明文字（斜體、灰色）
  注意事項：底色方塊段落 或 ⚠️ 前綴
```

### 表格樣式

```python
# 欄位說明表格標準格式
# 標題列：深色背景 + 白色文字
# 資料列：交替淺灰 (#F8F9FA) / 白色
# 欄寬比例：欄位名稱 25% / 說明 50% / 備註 25%
```

---

## 檔案寫入規則

所有含中文字的 .py 腳本，用 Write 工具寫到 outputs，再用 bash 執行：

```bash
python3 /sessions/.../outputs/gen_mockup.py
python3 /sessions/.../outputs/gen_docx.py
```

生成的圖片先確認效果（讀取 base64 或 zoom 截圖），確認中英文正常才繼續組文件。

---

## 完成後交付

1. 確認文件頁數、圖片數量、檔案大小合理
2. 將 .docx 存到 Odoo 19 workspace 資料夾
3. 提供 `computer://` 連結讓使用者直接開啟

---

## 品質確認清單

- [ ] 每章至少一張 mockup 圖
- [ ] 中文字正常顯示（不是方塊）
- [ ] 英文/數字正常顯示（不是方塊）
- [ ] 表格欄位說明完整
- [ ] 操作步驟為編號清單
- [ ] 文件可在 Windows Word 正常開啟
