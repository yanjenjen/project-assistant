# Odoo Purchase 模組 - 操作 SOP

> 版本標示：Odoo 17（依影片介面與功能推測，待確認）
> 學習日期：2026-07-22
> 狀態：🔄 草稿
> 說明：每支影片核心操作步驟，[MM:SS] 為影片時間錨點

---

## PAL01 主線流程：建立 RFQ → PO → 收貨

### Step 1｜建立新 RFQ

路徑：Purchase → 首頁 Dashboard → New（或 Orders → RFQ → New）

1. **Vendor**：輸入廠商名稱（如 Azer Interior）
2. **Order Deadline**：設定詢價截止日（廠商需在此日前確認）
3. **Products 分頁**：點「Add a product」 → 選擇產品
   - 數量（Quantity）與單價（Unit Price）自動帶入
   - 若數量達廠商折扣門檻 → 單價自動下調（廠商價格表觸發）[02:30]
4. 若產品不存在 → 輸入名稱 → 選「Create and Edit」 → 填入成本 → Save [03:17]

### Step 2｜發送 RFQ 給廠商

1. 點上方「**Send RFQ**」按鈕 [03:47]
2. 系統自動產生 Email 草稿（可編輯）→ 點「Send」
3. 狀態變更為「**RFQ Sent**」
4. Chatter 記錄寄出的 Email；亦可點「Print」取得 PDF 版

### Step 3｜確認為採購單（PO）

1. 廠商確認後 → 點「**Confirm Order**」 [04:43]
2. 狀態由 RFQ → **Purchase Order**
3. 右上角出現「**Receipt**」智慧按鈕

### Step 4｜收貨驗收

1. 點「Receipt」智慧按鈕 → 進入收貨單 [04:57]
2. Operations 分頁：確認 Demand 與 Done 數量一致
3. 點「**Validate**」 → 庫存自動更新

---

## PAL02 前置時間設定 SOP

### 廠商前置時間（Vendor Lead Time）設定

路徑：Inventory（或 Purchase）→ Products → Products → 選產品 → **Purchase 分頁**

- **Delivery Lead Time（廠商前置時間）**：廠商確認 PO 後，產品到達倉庫所需天數

### 採購安全前置時間 & 詢價日數設定

路徑：Purchase → Configuration → Settings → **Advanced Scheduling** [02:32]

| 欄位 | 說明 |
|------|------|
| Security Lead Time for Purchase | 全公司緩衝天數（建議值：2 天） |
| Days to Purchase | 廠商審核 RFQ 所需天數（建議值：1 天） |

儲存（Save）後生效。

### 前置時間計算公式

```
Order Deadline = RFQ 建立日 + Days to Purchase
Expected Arrival = Order Deadline + Vendor Lead Time（+ Security Lead Time）
總規劃視窗 = Days to Purchase + Security Lead Time + Vendor Lead Time
```

範例（PAL02）：Days=1 + Security=2 + Vendor=7 = **10 天規劃視窗**

### 觸發補貨

路徑：Purchase → Operations → Replenishment [03:00]

- 紅色眼睛圖示 = 庫存低於最小量
- 藍色標示預測日期 = 各項前置時間的加總
- 點「Order」→ 自動建立 RFQ

---

## PAL03 補貨規則（Reordering Rules）設定 SOP

### Step 1｜建立補貨規則

路徑：Products → Products → 選產品 → 點「**Reordering Rules**」智慧按鈕 → New

| 欄位 | 說明 | 範例 |
|------|------|------|
| Product | 自動帶入當前產品 | Desk Lamp |
| Min Quantity | 最小庫存（低於此值觸發） | 5 |
| Max Quantity | 補貨目標庫存 | 10 |
| Quantity Multiple | 訂購倍數 | 1 |
| Lead Time | 1 Day to Purchase / 1 Day to Get Products | — |

儲存（Save）

### Step 2｜設定廠商（必要條件）

返回產品表單 → Edit → **Purchase 分頁** → Add a Line → 選廠商 + 填入 Price → Save [02:17]

> ⚠️ 若未設廠商，Odoo 無法自動建立 RFQ。

### Step 3｜觸發排程器

**手動觸發（單一產品）**：產品 → Reordering Rules → 點規則本身 → 「**Run Scheduler**」 [04:23]

**手動觸發（全部產品）**：Inventory → Operations → **Run Scheduler** [06:12]

> 📌 Odoo 每日自動執行一次；如需立即生效請手動觸發。

### Odoo 計算訂購量邏輯

```
訂購量 = Max Quantity + 未滿足銷售訂單需求量
範例：Max=10，銷售訂單=6 → 自動 RFQ 數量=16
```

---

## PAL04 廠商價格表設定 SOP

### 單筆設定（產品層級）

路徑：Products → Products → 選產品 → **Purchase 分頁** → Vendor Pricelist

| 操作 | 說明 |
|------|------|
| 新增廠商 | 點「Add a Line」→ 選廠商 |
| 設定單價 | Price 欄位 |
| 設定交期 | Delivery Lead Time（廠商前置時間） |
| 設定數量折扣 | 再新增一行，同廠商，設 Quantity 門檻 + 折扣價（或啟用 Discount 欄位填 %） |
| 優先順序 | 列表最頂端 = 補貨規則預設廠商 |

### 啟用折扣百分比欄位

點「Delivery Lead Time」旁的**斜線圖示（slider icon）** → 勾選 Discount 欄位顯示 [02:04]

### 批量匯入廠商價格表

1. 路徑：Purchase → Configuration → **Vendor Price List** [02:33]
2. 勾選範例資料 → Action → **Export** → 選 Excel 或 CSV
3. 按格式填入廠商資料
4. 點左上「Cog 齒輪圖示」→ **Import Records** → Upload File → Import

---

## PAL05 審核與警告設定 SOP

### 設定採購審核門檻

路徑：Purchase → Configuration → Settings → Orders 區塊

1. 勾選「**Purchase Order Approval**」
2. 設定「**Minimum Amount**」（如 $500）
3. 點「**Save**」 [01:10]

### 設定使用者採購權限

路徑：一般設定（General Settings）→ Manage Users → 選使用者 → 滾至 Inventory 區塊 → Purchase 欄位

| 選項 | 說明 |
|------|------|
| User | 一般使用者，超過門檻需主管審核 |
| Administrator | 可直接確認任何金額 PO |

### 審核流程

1. 一般使用者建立 RFQ → 點「Confirm Order」→ 狀態變為「**To Approve**」[06:01]
2. 管理者路徑：Purchase → Orders → RFQ → 過濾「To Approve」
3. 管理者點「**Approve Order**」→ 轉為 Purchase Order [06:43]

### 設定廠商警告

路徑：Purchase → Orders → **Vendors** → 選廠商 → **Internal Notes 分頁** → Warning 區塊

| 選項 | 說明 |
|------|------|
| Warning | 彈出提示訊息（不阻擋） |
| Blocking Message | 彈出訊息並阻擋繼續操作 |

### 設定產品警告

路徑：Products → Products → 選產品 → **Purchase 分頁** → Warning When Purchasing 區塊

選類型（Warning / Blocking Message）→ 填入訊息內容 [04:29]

---

## PAL06 Blanket Order（框架訂單）操作 SOP

### 前置設定

路徑：Purchase → Configuration → Settings → Orders → 勾選「**Purchase Agreements**」→ Save [01:00]

### Step 1｜建立框架訂單

路徑：Purchase → Orders → **Purchase Agreements** → New

| 欄位 | 說明 |
|------|------|
| Agreement Type | 選「**Blanket Order**」 |
| Vendor | 選廠商 |
| Agreement Validity（From / To） | 設定有效期間（如全年度） |
| Products 區塊 | 加入產品、設定**總採購數量**與**議定單價** |

→ 點「**Confirm**」[02:53]

### Step 2｜分批建立 RFQ

1. 點「**New Quotation**」按鈕 → 產生以框架訂單條件為基礎的 RFQ [03:01]
2. 設定每張 RFQ 的 Order Deadline（截止日）與 Expected Arrival（預計到貨日）
3. 修改各批次數量（如 1/3、1/3、1/3）
4. 點「Confirm Order」→ 轉 PO → Receive Products → Validate → Create Bill

### 追蹤框架訂單狀態

- 點框架訂單右上 Smart Button「RFQs/Orders」→ 查看所有子 RFQ/PO 狀態與到貨日
- 框架訂單「Ordered」欄位追蹤累計採購數量
- 關閉框架訂單條件：所有 RFQ 轉為 PO 即可（不需全部完成帳單）

---

## PAL07 帳單控制 & 三方比對 SOP

### 設定帳單控制政策（全域）

路徑：Purchase → Configuration → Settings → **Invoicing 區塊**

| 選項 | 說明 |
|------|------|
| Ordered Quantities | PO 確認後即可建立帳單 |
| Received Quantities | 收貨後才可建立帳單（搭配三方比對） |

勾選「**3-Way Matching**」 → Save

### 設定帳單控制政策（產品層級覆蓋）

路徑：Products → Products → 選產品 → **Purchase 分頁** → Vendor Bills → **Control Policy** [01:51]

→ 可選 Ordered Quantities（與全域不同，單品覆蓋）

### 三方比對流程（Received Quantities 政策）

```
1. Confirm Order（確認 PO）
   ↓
2. Receive Products → Validate（收貨驗收）
   ↓
3. 返回 PO → 點「Create Bill」（收貨前無法點此）
   ↓
4. Bill 的 Other Info 分頁 → 確認「Should Be Paid」= Yes
   ↓
5. 設定 Bill Date → Confirm → Register Payment
```

### 查看帳單狀態

PO → **Other Information 分頁** → **Billing Status**

| 狀態 | 說明 |
|------|------|
| Nothing to Bill | 尚無可開帳內容 |
| Waiting Bills | 可建立帳單（已收貨） |
| Fully Billed | 已完成對帳 |

---

## PAL08 替代詢價 / 比價採購 SOP

### 前置設定

路徑：Purchase → Configuration → Settings → 勾選「**Purchase Agreements**」+ 「**Purchase Alternatives**」→ Save

### Step 1｜建立主要 RFQ 並發送

路徑：Purchase → Orders → RFQ → New → 填廠商 + 產品 → Send by Email → Send

### Step 2｜新增替代 RFQ

在已發送的 RFQ → 點「**Alternatives 分頁**」→「**Create Alternative**」[02:43]

- 選擇不同廠商
- 是否複製產品（Copy Products）：不勾 = 手動加入
- 點「Create Alternatives」→ 再填入產品 → Send by Email

### Step 3｜連結現有 RFQ（可選）

在任一替代 RFQ → Alternatives 分頁 → 「**Link to Existing RFQ**」→ 勾選要比較的 RFQ → Select [04:51]

### Step 4｜比價選廠商

在任一替代 RFQ → Alternatives 分頁 → 點「**Compare Products**」[05:11]

- Odoo 自動以**綠色**標示：最快到貨日、最低單價、最低總金額
- 勾選各產品的最佳廠商

### Step 5｜確認訂單

進入選定廠商的 RFQ → 點「**Confirm Order**」→ 彈窗選擇是否「**Cancel Alternatives**」（建議選 Cancel）[06:07]

---

## PAL09 採購範本（Purchase Template）SOP

### 前置設定

Purchase → Configuration → Settings → 勾選「**Purchase Agreements**」→ Save

### 建立採購範本

路徑：Purchase → Orders → **Purchase Agreements** → New

| 欄位 | 說明 |
|------|------|
| Vendor | 可選擇性填入（選填） |
| Agreement Type | 選「**Purchase Template**」 |
| Products | 加入產品 + 設定固定數量 + 單價 |

→ 點「**Confirm**」

### 使用範本下單

1. 在確認的範本頁面 → 點「**New Quotation**」[02:05]
2. 所有產品、數量、價格、廠商自動複製
3. 可自由修改：數量、價格、刪除或新增產品
4. 確認 → 走一般 RFQ → PO 流程

### 追蹤範本使用紀錄

Smart Button「RFQs/Orders」→ 查看所有由此範本產生的訂單

重要欄位：
- **Confirmation Date**：RFQ 轉 PO 的日期
- **Expected Arrival Date**：預計到貨日
- 底部**總金額**：使用此範本的累計採購金額

---

## PAL10 EDI 採購單 → 銷售訂單 SOP

### 買方端（Purchase App）

1. 建立 RFQ → 加入產品 → 點「Confirm Order」→ 轉為 PO [01:39]

### 廠商端（Portal View）

1. 廠商從 Email 或入口網站登入 Portal
2. 查看「Our Orders」→ 找到相關 PO [02:01]
3. 點「**Connect with your software**」按鈕 [02:35]
4. 彈窗說明上傳方式（支援 XML 或拖放 PDF）
5. 複製 XML URL → 於新分頁貼上 → 自動下載 `.xml` 檔案

### 廠商端（Sales App - 接收方）

1. 進入廠商自己的 Odoo → **Sales** 應用
2. 點左上「**Upload**（上傳）」按鈕 [03:17]
3. 選取剛下載的 XML 檔
4. 系統自動建立 Sales Order：
   - Customer 欄位 = 買方公司自動填入
   - 產品、數量、價格全部帶入
   - XML 檔案存於 Chatter（可追溯）

---

*本文件為草稿，依據 PAL01–PAL10 影片逐字稿整理，實際操作細節請以當前部署版本為準。*
