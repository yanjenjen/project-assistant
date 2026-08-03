# Odoo 學習管道 SOP
> 任何對話視窗接手此專案時，先讀本文件再動作。
> 最後更新：2026-07-30

---

## 一、系統架構

### 雙軌制

| 軌道 | 負責人 | 內容 |
|------|--------|------|
| Track A（本機知識庫） | 海瑟姆（員工_03）→ 產出由小果（員工_02）整理 | 每個模組 6 支 .md 知識庫文件 |
| Track B（Notion 索引） | 小果（員工_02） | Notion 資料庫同步索引 |

### 知識庫位置
- 本機：`C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\Odoo知識庫\`
- 工具資料夾：`...\Odoo知識庫\工具\`
- 各模組子資料夾：`...\Odoo知識庫\[模組名稱]\`（如 CRM、Sales、Purchase、Inventory、eCommerce…）

### Track A 每模組 6 支固定文件
```
01_功能概覽.md
02_操作SOP.md
03_欄位與單據清單.md
04_內控點與風險.md
05_Demo情境腳本.md
06_常見問題.md
```
模板參照：`...\Odoo知識庫\SOP_模板.md`

---

## 二、模組代號與進度

| # | 模組 | 代號 | Slides URL | 影片數 | 狀態 |
|---|------|------|-----------|--------|------|
| 1 | Getting Started | GS | — | — | ✅ 完成 |
| 2 | CRM | CRM | /slides/crm-17 | 22 | ✅ 完成 |
| 3 | Sales | SAL | /slides/sales-18 | 31 | ✅ 完成 |
| 4 | Purchase | PAL | /slides/purchase-23 | 10 | ✅ 完成 |
| 5 | Inventory | INV | /slides/inventory-24 | 37 | ✅ 完成（Track A 01~06 草稿，2026-07-30） |
| 6 | Website & eCommerce | ECM | /slides/website-ecommerce-25 | 26 | ✅ 完成（Track A 01~06 草稿，2026-07-30） |
| 7 | Accounting | ACC | 需確認 | — | 🔲 未開始 |
| 8 | Manufacturing | MFG | 需確認 | — | 🔲 未開始 |

---

## 三、完整管道流程（每個模組）

### Step 1：找 Slides URL 與 Channel ID

**方法 A（已知模組）**：直接從上表查。

**方法 B（新模組）**：用 Claude in Chrome 瀏覽 `https://www.odoo.com/slides/all`，找到對應模組的 Channel ID（URL 末尾數字）。

URL 格式：`https://www.odoo.com/slides/[模組slug]-[channel-id]`

---

### Step 2：抓取所有 YouTube ID（Odoo JSON-RPC API 法）

> ⚡ 最快方法：不需逐頁導航，一次拿全部。

**前提**：在 Chrome 瀏覽器中已開啟任一 `odoo.com/slides/` 頁面（需在 odoo.com domain 下）。

在 Claude in Chrome 的 javascript_tool 執行：

```javascript
const channelId = 25; // 替換為目標 Channel ID
const res = await fetch('/web/dataset/call_kw', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    jsonrpc: '2.0', method: 'call', id: 1,
    params: {
      model: 'slide.slide',
      method: 'search_read',
      args: [[['channel_id', '=', channelId]]],
      kwargs: {
        fields: ['name', 'youtube_id', 'sequence'],
        limit: 100,
        order: 'sequence asc'
      }
    }
  })
});
const data = await res.json();
const slides = data.result.filter(s => s.youtube_id);
slides.forEach(s => console.log(`${s.sequence}. ${s.name} → ${s.youtube_id}`));
slides.length + ' videos total';
```

回傳結果直接包含所有影片名稱與 YouTube ID，section header（youtube_id=false）會被 filter 掉。

---

### Step 3：建立 urls_[模組].txt

**位置**：`工具/urls_[模組代號小寫].txt`（如 `urls_inventory.txt`、`urls_ecommerce.txt`）

**格式**（參照既有檔案）：
```
# Odoo [模組名] YouTube 網址清單
# 來源：https://www.odoo.com/slides/[slug]-[id]
# 更新日期：YYYY-MM-DD
# 共 N 支影片（Xh Ym）
#
# ============================================================
# Section 1: [Section Name]（N 支）
# ============================================================

# [代號]01｜[影片標題]
https://www.youtube.com/watch?v=[youtube_id]
```

**代號規則**：CRM / SAL / PAL / INV / ECM / ACC / MFG + 兩位數序號（01-99）

**注意**：有些影片 ID 以「-」開頭（如 `-HCfwpavx-c`），這是正常的 YouTube ID，直接放入 URL 即可。

---

### Step 4：使用者在本機執行下載腳本

```powershell
cd C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\Odoo知識庫\工具
python odoo_transcript_downloader.py urls_[模組].txt
```

**已知問題**：
- YouTube 會 429 限流。遇到全部失敗時，等 10–30 分鐘再重試。
- 先用單支測試：`python odoo_transcript_downloader.py "https://www.youtube.com/watch?v=XXX"`
- 逐字稿下載成功後存入 `工具/transcripts_YYYYMMDD_HHMM/` 資料夾。

**工具版本**：腳本已更新為 `yt-dlp`（不再使用 `youtube_transcript_api`）。

---

### Step 5：產出 Track A 知識庫（01~06）

AI 讀取逐字稿資料夾內所有 .txt，依 `SOP_模板.md` 格式產出 6 支文件。

**角色**：海瑟姆（員工_03）主責分析，小果（員工_02）主責文件格式整理。

**輸出位置**：`Odoo知識庫/[模組名]/`

**指令（給新視窗）**：
```
請讀取 工具/transcripts_[日期]/ 下所有逐字稿，
以及 SOP_模板.md，
產出 [模組名]/ 資料夾的 01~06 知識庫文件。
參考 Purchase/ 下的既有文件作為格式範例。
```

---

### Step 5b：Track B — Notion 同步（⚠️ 必做，不可省略）

> Track A 完成後，**必須**執行 Track B，兩軌並行才算該模組完成。

**角色**：小果（員工_02）主責。

**操作步驟**：

1. **確認 Notion 知識庫資料庫有對應的 APP模組 選項**
   - 資料庫：`【Odoo】Knowledge Base｜知識庫`（data_source_id: `33d65d18-4cda-8007-8a12-000b677ee0c7`）
   - 若新模組的 APP模組 選項不存在，先用 `notion-update-data-source` 的 `ALTER COLUMN` 新增
   - 語法範例：`ALTER COLUMN "APP模組" SET SELECT('X':default, '主設定/通用':purple, ... '新模組':blue)`
   - ⚠️ 必須保留所有現有選項，只在末尾新增

2. **為每個模組建立 6 支 Notion 頁面**
   - 每頁 parent: `data_source_id: 33d65d18-4cda-8007-8a12-000b677ee0c7`
   - 必填 properties：`名稱`、`APP模組`、`文件類型`、`系統類型`（Odoo）、`知識類型`、`來源狀態`（草稿）、`版本日期`
   - 內容：從 Track A 對應 .md 摘要重點（不需全文複製，保留關鍵表格與流程）
   - 頁尾加：`> 本頁同步自本機 Track A：艾創點數位-ERP顧問/Odoo知識庫/[模組]/[檔名].md`

3. **確認 6 頁建立完成後，在進度總覽備註欄填入 Notion 頁面連結**

**各模組 APP模組 值對應**：

| 模組 | APP模組 值 |
|------|-----------|
| CRM | CRM |
| Sales | Sales |
| Purchase | 採購 |
| Inventory | 庫存 |
| Website & eCommerce | 電商/網站 |
| Accounting | 會計（新增） |
| Manufacturing | 製造（新增） |

---

### Step 6：更新學習進度

更新 `Odoo知識庫/00_學習進度總覽.md` 對應模組列的狀態（Track A + Track B 均完成才標 ✅）。

---

## 四、工具清單

| 檔案 | 用途 |
|------|------|
| `工具/odoo_transcript_downloader.py` | 批次下載 YouTube 逐字稿（yt-dlp 版） |
| `工具/urls_inventory.txt` | Inventory 37 支影片 URL（INV01-INV37） |
| `工具/urls_ecommerce.txt` | eCommerce 26 支影片 URL（ECM01-ECM26） |
| `工具/demo環境連線.md` | Odoo demo 練習環境連線資訊 |
| `00_學習進度總覽.md` | 全模組學習進度追蹤 |
| `SOP_模板.md` | Track A 6 支文件的模板 |

---

## 五、目前待完成事項（2026-07-30 更新）

已完成：
- ✅ Inventory 37 支逐字稿下載 + Track A 01~06（草稿）
- ✅ Website & eCommerce 26 支逐字稿下載 + Track A 01~06（草稿）

下一批（未開始）：
1. **Accounting**：找 Slides URL → 批次下載逐字稿 → 產出 Track A 01~06
2. **Manufacturing**：找 Slides URL → 批次下載逐字稿 → 產出 Track A 01~06

---

## 六、新視窗接手時的快速確認清單

1. 讀本文件（`工具/Odoo學習管道SOP.md`）
2. 讀 `00_學習進度總覽.md` 確認目前進度
3. 確認 `工具/` 下有哪些 `transcripts_*/` 資料夾（逐字稿是否已下載）
4. 從「目前待完成事項」找到下一步執行

---

## 七、Odoo Slides Channel ID 參照表

| 模組 | Slug | Channel ID | 完整 URL |
|------|------|-----------|---------|
| Getting Started | getting-started | 1（需確認） | — |
| CRM | crm | 17 | /slides/crm-17 |
| Sales | sales | 18 | /slides/sales-18 |
| Purchase | purchase | 23 | /slides/purchase-23 |
| Inventory | inventory | 24 | /slides/inventory-24 |
| Website & eCommerce | website-ecommerce | 25 | /slides/website-ecommerce-25 |
| Accounting | 需確認 | 需確認 | — |
| Manufacturing | 需確認 | 需確認 | — |
