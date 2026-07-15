# Odoo 逐字稿批次下載工具｜使用說明

> 目的：取代手動逐支操作 downsub.com 的流程，一次批次下載整個模組的逐字稿

---

## 一次安裝

在終端機（命令提示字元）執行：
```
pip install youtube-transcript-api
```

安裝一次，永久可用。

---

## 每次使用流程

### Step 1｜收集 YouTube 網址

**方法 A（推薦）**：從 Odoo 官方學習平台取得

1. 進入 Odoo 課程（如 CRM 模組）
2. 點課程頁面中的影片
3. 右下角點紅框 YouTube 圖示 → 跳出 YouTube 網頁
4. 複製網址貼入 `urls.txt`（每行一個）
5. 重複，把這個模組所有影片的網址全部貼進去

**方法 B**：直接從 YouTube 搜尋 Odoo 官方影片也可以

### Step 2｜建立 urls.txt

在本工具資料夾（`工具/`）建立或編輯 `urls.txt`，格式：
```
# CRM 模組 - Getting Started
https://www.youtube.com/watch?v=NoxYrnnHgfk
https://www.youtube.com/watch?v=xxxxxxxxxxxxxxxx
https://www.youtube.com/watch?v=xxxxxxxxxxxxxxxx

# 開頭有 # 的行會被忽略（可用來加備註）
```

### Step 3｜執行腳本

```bash
cd C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\Odoo知識庫\工具
python3 odoo_transcript_downloader.py
```

或直接在 PowerShell 雙擊執行。

### Step 4｜取得逐字稿

腳本執行完後，逐字稿會存到：
```
工具/transcripts_YYYYMMDD_HHMM/
  NoxYrnnHgfk.txt    ← 每支影片一個檔案
  xxxxxxxxxxxxxxx.txt
  ...
```

---

## 替代方案（不想裝 Python）

**YouTube 內建逐字稿**（比 downsub 少 3 個步驟）：
1. 打開 YouTube 影片
2. 點影片下方「⋯」（更多）→ **顯示逐字稿**
3. 右側面板出現逐字稿 + 時間戳
4. 全選（Ctrl+A）→ 複製（Ctrl+C）→ 貼進文字檔

---

## 與 SOP 處理流程的銜接

收集完逐字稿後 → 複製內容 → 到 Cowork 對話貼上，說：

```
逐字稿：[模組名稱] / [影片名稱]
[貼上逐字稿內容]
```

→ 海瑟姆開始執行 7 步驟 odoo-learning-pipeline

---

## 常見問題

**Q：某支影片下載失敗怎麼辦？**
A：代表該影片沒有開放字幕。改用 YouTube 內建逐字稿手動複製。

**Q：字幕是自動生成的（auto-generated），品質夠好嗎？**
A：官方 Odoo 教學影片通常有人工字幕，品質很好。自動生成的偶爾會有語音辨識錯誤，但 SOP 萃取時會自動過濾。

**Q：可以抓中文字幕嗎？**
A：可以。修改腳本第 57 行的 `prefer_lang='en'` 改為 `prefer_lang='zh-TW'`。

---

## 版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v0.1 | 2026-07-10 | 初始版本 |
