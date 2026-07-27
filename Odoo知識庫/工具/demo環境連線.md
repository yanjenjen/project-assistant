# Odoo Demo 環境連線資訊

## Jenny 個人練習資料庫

| 項目 | 內容 |
|------|------|
| Server URL | https://odoo-demo19.ideaxpress.biz |
| Database | v19-ce-jenny |
| 版本 | Odoo 19 Community Edition |
| Demo Data | 已啟用（建立時勾選） |
| 登入帳號 | jenny.lu@ideaxpress.biz |
| 登入密碼 | admin |
| 介面語言 | 繁體中文（建立時誤選，保留使用） |
| 建立日期 | 2026-07-22 |
| **重建日期** | **2026-07-23（原資料庫登入密碼遺失，已刪除重建）** |

## 使用說明

- **登入路徑**：https://odoo-demo19.ideaxpress.biz/web/login → 選擇 Database: `v19-ce-jenny`
- **用途**：個人學習練習、Demo 情境腳本驗證（對應 Track A 05_Demo情境腳本）
- **注意**：這是共用伺服器上的個人專屬 database，操作前確認 database 已選到 `v19-ce-jenny`
- **注意**：伺服器 IP 會隨基礎設施調整變動（曾遇過 IP 換過但網域/資料庫不受影響），若連不上先確認網域本身是否能連線，而非資料庫遺失
- Master Password（刪除/重建資料庫用）記錄在艾創點內部的 Odoo Docker 連線資訊文件中，不重複記錄在此檔案

## 重建說明（需要乾淨環境時）

1. 登入後進入 Settings → Technical → Database Management（或直接前往 `/web/database/manager`）
2. Duplicate `v19-ce-jenny` 做備份（選填），或直接 Drop 再重建
3. 重建時勾選 Demo Data

## 相關工具

- 逐字稿下載腳本：`工具/odoo_transcript_downloader.py`
- Inventory URL 清單：`工具/urls_inventory.txt`
