# Odoo Purchase 模組 - 操作 SOP

> 版本標示：Odoo 17（依影片介面與功能推測，待確認）
> 學習日期：2026-07-22
> 補充中文對照：2026-07-23
> 狀態：🔄 草稿
> 說明：每支影片核心操作步驟，[MM:SS] 為影片時間錨點。全文英文系統名詞統一補上中文對照，格式為「中文（English）」，方便對照畫面操作（依 Jenny 回饋：英文不好，需中文+英文並列）。

---

## PAL01 主線流程：建立詢價單（RFQ）→ 採購單（PO）→ 收貨（Receipt）

### Step 1｜建立新詢價單（RFQ）

路徑：採購（Purchase）→ 首頁儀表板（Dashboard）→ 新增（New）（或 訂單（Orders）→ 詢價單（RFQ）→ 新增（New））

1. **供應商（Vendor）**：輸入廠商名稱（如 Azer Interior）
2. **訂單截止日（Order Deadline）**：設定詢價截止日（廠商需在此日前確認）
3. **產品分頁（Products）**：點「新增產品（Add a product）」 → 選擇產品
   - 數量（Quantity）與單價（Unit Price）自動帶入
   - 若數量達廠商折扣門檻 → 單價自動下調（廠商價格表觸發）[02:30]
4. 若產品不存在 → 輸入名稱 → 選「建立並編輯（Create and Edit）」 → 填入成本 → 儲存（Save）[03:17]

### Step 2｜發送詢價單（RFQ）給廠商

1. 點上方「**發送詢價單（Send RFQ）**」按鈕 [03:47]
2. 系統自動產生電子郵件（Email）草稿（可編輯）→ 點「發送（Send）」
3. 狀態變更為「**詢價單已發送（RFQ Sent）**」
4. 留言紀錄（Chatter）記錄寄出的 Email；亦可點「列印（Print）」取得 PDF 版

### Step 3｜確認為採購單（PO）

1. 廠商確認後 → 點「**確認訂單（Confirm Order）**」 [04:43]
2. 狀態由詢價單（RFQ）→ **採購單（Purchase Order）**
3. 右上角出現「**收貨（Receipt）**」智慧按鈕

### Step 4｜收貨驗收

1. 點「收貨（Receipt）」智慧按鈕 → 進入收貨單 [04:57]
2. 作業分頁（Operations）：確認需求數量（Demand）與完成數量（Done）一致
3. 點「**驗證／確認收貨（Validate）**」 → 庫存自動更新

---

## PAL02 前置時間設定 SOP

### 廠商前置時間（Vendor Lead Time）設定

路徑：庫存（Inventory）（或 採購（Purchase））→ 產品（Products）→ 產品（Products）→ 選產品 → **採購分頁（Purchase）**

- **交貨前置天數（Delivery Lead Time，即廠商前置時間）**：廠商確認 PO 後，產品到達倉庫所需天數

### 採購安全前置時間 & 詢價日數設定

路徑：採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ **進階排程（Advanced Scheduling）** [02:32]

| 欄位 | 說明 |
|------|------|
| 安全前置時間（Security Lead Time for Purchase） | 全公司緩衝天數（建議值：2 天） |
| 詢價審核天數（Days to Purchase） | 廠商審核 RFQ 所需天數（建議值：1 天） |

儲存（Save）後生效。

### 前置時間計算公式

```
訂單截止日（Order Deadline）= 詢價單建立日 + 詢價審核天數（Days to Purchase）
預計到貨日（Expected Arrival）= 訂單截止日（Order Deadline）+ 廠商前置時間（Vendor Lead Time）（+ 安全前置時間（Security Lead Time））
總規劃視窗 = 詢價審核天數 + 安全前置時間 + 廠商前置時間
```

範例（PAL02）：Days=1 + Security=2 + Vendor=7 = **10 天規劃視窗**

### 觸發補貨

路徑：採購（Purchase）→ 作業（Operations）→ 補貨（Replenishment） [03:00]

- 紅色眼睛圖示 = 庫存低於最小量
- 藍色標示預測日期 = 各項前置時間的加總
- 點「下單（Order）」→ 自動建立詢價單（RFQ）

---

## PAL03 補貨規則（Reordering Rules）設定 SOP

### Step 1｜建立補貨規則

路徑：產品（Products）→ 產品（Products）→ 選產品 → 點「**補貨規則（Reordering Rules）**」智慧按鈕 → 新增（New）

| 欄位 | 說明 | 範例 |
|------|------|------|
| 產品（Product） | 自動帶入當前產品 | Desk Lamp |
| 最小庫存量（Min Quantity） | 最小庫存（低於此值觸發） | 5 |
| 補貨目標庫存（Max Quantity） | 補貨目標庫存 | 10 |
| 訂購倍數（Quantity Multiple） | 訂購倍數 | 1 |
| 前置時間（Lead Time） | 1 Day to Purchase / 1 Day to Get Products | — |

儲存（Save）

### Step 2｜設定廠商（必要條件）

返回產品表單 → 編輯（Edit）→ **採購分頁（Purchase）** → 新增一行（Add a Line）→ 選廠商 + 填入價格（Price）→ 儲存（Save） [02:17]

> ⚠️ 若未設廠商，Odoo 無法自動建立詢價單（RFQ）。

### Step 3｜觸發排程器（Scheduler）

**手動觸發（單一產品）**：產品 → 補貨規則（Reordering Rules）→ 點規則本身 → 「**執行排程器（Run Scheduler）**」 [04:23]

**手動觸發（全部產品）**：庫存（Inventory）→ 作業（Operations）→ **執行排程器（Run Scheduler）** [06:12]

> 📌 Odoo 每日自動執行一次；如需立即生效請手動觸發。

### Odoo 計算訂購量邏輯

```
訂購量 = 補貨目標庫存（Max Quantity）+ 未滿足銷售訂單需求量
範例：Max=10，銷售訂單=6 → 自動 RFQ 數量=16
```

---

## PAL04 廠商價格表設定 SOP

### 單筆設定（產品層級）

路徑：產品（Products）→ 產品（Products）→ 選產品 → **採購分頁（Purchase）** → 廠商價格表（Vendor Pricelist）

| 操作 | 說明 |
|------|------|
| 新增廠商 | 點「新增一行（Add a Line）」→ 選廠商 |
| 設定單價 | 價格欄位（Price） |
| 設定交期 | 交貨前置天數（Delivery Lead Time，即廠商前置時間） |
| 設定數量折扣 | 再新增一行，同廠商，設數量（Quantity）門檻 + 折扣價（或啟用折扣（Discount）欄位填 %） |
| 優先順序 | 列表最頂端 = 補貨規則預設廠商 |

### 啟用折扣百分比欄位

點「交貨前置天數（Delivery Lead Time）」旁的**斜線圖示（slider icon）** → 勾選折扣（Discount）欄位顯示 [02:04]

### 批量匯入廠商價格表

1. 路徑：採購（Purchase）→ 設定（Configuration）→ **廠商價格表（Vendor Price List）** [02:33]
2. 勾選範例資料 → 動作（Action）→ **匯出（Export）** → 選 Excel 或 CSV
3. 按格式填入廠商資料
4. 點左上「齒輪圖示（Cog icon）」→ **匯入紀錄（Import Records）** → 上傳檔案（Upload File）→ 匯入（Import）

---

## PAL05 審核與警告設定 SOP

### 設定採購審核門檻

路徑：採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ 訂單區塊（Orders）

1. 勾選「**採購單審核（Purchase Order Approval）**」
2. 設定「**最低金額門檻（Minimum Amount）**」（如 $500）
3. 點「**儲存（Save）**」 [01:10]

### 設定使用者採購權限

路徑：一般設定（General Settings）→ 管理使用者（Manage Users）→ 選使用者 → 滾至 庫存（Inventory）區塊 → 採購（Purchase）欄位

| 選項 | 說明 |
|------|------|
| 一般使用者（User） | 超過門檻需主管審核 |
| 管理者（Administrator） | 可直接確認任何金額 PO |

### 審核流程

1. 一般使用者建立 RFQ → 點「確認訂單（Confirm Order）」→ 狀態變為「**待審核（To Approve）**」[06:01]
2. 管理者路徑：採購（Purchase）→ 訂單（Orders）→ 詢價單（RFQ）→ 過濾「待審核（To Approve）」
3. 管理者點「**核准訂單（Approve Order）**」→ 轉為採購單（Purchase Order） [06:43]

### 設定廠商警告

路徑：採購（Purchase）→ 訂單（Orders）→ **供應商（Vendors）** → 選廠商 → **內部備註分頁（Internal Notes）** → 警告（Warning）區塊

| 選項 | 說明 |
|------|------|
| 警告（Warning） | 彈出提示訊息（不阻擋） |
| 封鎖訊息（Blocking Message） | 彈出訊息並阻擋繼續操作 |

### 設定產品警告

路徑：產品（Products）→ 產品（Products）→ 選產品 → **採購分頁（Purchase）** → 採購時警告（Warning When Purchasing）區塊

選類型（警告 Warning / 封鎖訊息 Blocking Message）→ 填入訊息內容 [04:29]

---

## PAL06 框架訂單（Blanket Order）操作 SOP

### 前置設定

路徑：採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ 訂單（Orders）→ 勾選「**採購協議（Purchase Agreements）**」→ 儲存（Save） [01:00]

### Step 1｜建立框架訂單

路徑：採購（Purchase）→ 訂單（Orders）→ **採購協議（Purchase Agreements）** → 新增（New）

| 欄位 | 說明 |
|------|------|
| 協議類型（Agreement Type） | 選「**框架訂單（Blanket Order）**」 |
| 廠商（Vendor） | 選廠商 |
| 有效期間（Agreement Validity，From / To） | 設定有效期間（如全年度） |
| 產品區塊（Products） | 加入產品、設定**總採購數量**與**議定單價** |

→ 點「**確認（Confirm）**」[02:53]

### Step 2｜分批建立詢價單（RFQ）

1. 點「**新增報價（New Quotation）**」按鈕 → 產生以框架訂單條件為基礎的 RFQ [03:01]
2. 設定每張 RFQ 的訂單截止日（Order Deadline）與預計到貨日（Expected Arrival）
3. 修改各批次數量（如 1/3、1/3、1/3）
4. 點「確認訂單（Confirm Order）」→ 轉採購單（PO）→ 收貨（Receive Products）→ 驗證（Validate）→ 建立帳單（Create Bill）

### 追蹤框架訂單狀態

- 點框架訂單右上智慧按鈕（Smart Button）「詢價單/訂單（RFQs/Orders）」→ 查看所有子 RFQ/PO 狀態與到貨日
- 框架訂單「已訂購（Ordered）」欄位追蹤累計採購數量
- 關閉框架訂單條件：所有 RFQ 轉為 PO 即可（不需全部完成帳單）

---

## PAL07 帳單控制 & 三方比對 SOP

### 設定帳單控制政策（全域）

路徑：採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ **開票區塊（Invoicing）**

| 選項 | 說明 |
|------|------|
| 依訂購數量開票（Ordered Quantities） | PO 確認後即可建立帳單 |
| 依收貨數量開票（Received Quantities） | 收貨後才可建立帳單（搭配三方比對） |

勾選「**三方比對（3-Way Matching）**」 → 儲存（Save）

### 設定帳單控制政策（產品層級覆蓋）

路徑：產品（Products）→ 產品（Products）→ 選產品 → **採購分頁（Purchase）** → 供應商帳單（Vendor Bills）→ **控制政策（Control Policy）** [01:51]

→ 可選依訂購數量開票（Ordered Quantities）（與全域不同，單品覆蓋）

### 三方比對流程（依收貨數量開票政策）

```
1. 確認訂單（Confirm Order，確認 PO）
   ↓
2. 收貨並驗證（Receive Products → Validate，收貨驗收）
   ↓
3. 返回 PO → 點「建立帳單（Create Bill）」（收貨前無法點此）
   ↓
4. 帳單其他資訊分頁（Other Info）→ 確認「應付款（Should Be Paid）」= Yes
   ↓
5. 設定帳單日期（Bill Date）→ 確認（Confirm）→ 登記付款（Register Payment）
```

### 查看帳單狀態

PO → **其他資訊分頁（Other Information）** → **帳單狀態（Billing Status）**

| 狀態 | 說明 |
|------|------|
| 無需開票（Nothing to Bill） | 尚無可開帳內容 |
| 等待開票（Waiting Bills） | 可建立帳單（已收貨） |
| 已完全開票（Fully Billed） | 已完成對帳 |

---

## PAL08 替代詢價 / 比價採購 SOP

### 前置設定

路徑：採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ 勾選「**採購協議（Purchase Agreements）**」+ 「**替代詢價（Purchase Alternatives）**」→ 儲存（Save）

### Step 1｜建立主要詢價單（RFQ）並發送

路徑：採購（Purchase）→ 訂單（Orders）→ 詢價單（RFQ）→ 新增（New）→ 填廠商 + 產品 → 以電子郵件發送（Send by Email）→ 發送（Send）

### Step 2｜新增替代詢價單（RFQ）

在已發送的 RFQ → 點「**替代方案分頁（Alternatives）**」→「**建立替代方案（Create Alternative）**」[02:43]

- 選擇不同廠商
- 是否複製產品（Copy Products）：不勾 = 手動加入
- 點「建立替代方案（Create Alternatives）」→ 再填入產品 → 以電子郵件發送（Send by Email）

### Step 3｜連結現有詢價單（可選）

在任一替代 RFQ → 替代方案分頁（Alternatives）→ 「**連結至現有詢價單（Link to Existing RFQ）**」→ 勾選要比較的 RFQ → 選擇（Select） [04:51]

### Step 4｜比價選廠商

在任一替代 RFQ → 替代方案分頁（Alternatives）→ 點「**比較產品（Compare Products）**」[05:11]

- Odoo 自動以**綠色**標示：最快到貨日、最低單價、最低總金額
- 勾選各產品的最佳廠商

### Step 5｜確認訂單

進入選定廠商的 RFQ → 點「**確認訂單（Confirm Order）**」→ 彈窗選擇是否「**取消其他替代方案（Cancel Alternatives）**」（建議選 Cancel） [06:07]

---

## PAL09 採購範本（Purchase Template）SOP

### 前置設定

採購（Purchase）→ 設定（Configuration）→ 偏好設定（Settings）→ 勾選「**採購協議（Purchase Agreements）**」→ 儲存（Save）

### 建立採購範本

路徑：採購（Purchase）→ 訂單（Orders）→ **採購協議（Purchase Agreements）** → 新增（New）

| 欄位 | 說明 |
|------|------|
| 廠商（Vendor） | 可選擇性填入（選填） |
| 協議類型（Agreement Type） | 選「**採購範本（Purchase Template）**」 |
| 產品（Products） | 加入產品 + 設定固定數量 + 單價 |

→ 點「**確認（Confirm）**」

### 使用範本下單

1. 在確認的範本頁面 → 點「**新增報價（New Quotation）**」[02:05]
2. 所有產品、數量、價格、廠商自動複製
3. 可自由修改：數量、價格、刪除或新增產品
4. 確認 → 走一般詢價單（RFQ）→ 採購單（PO）流程

### 追蹤範本使用紀錄

智慧按鈕（Smart Button）「詢價單/訂單（RFQs/Orders）」→ 查看所有由此範本產生的訂單

重要欄位：
- **確認日期（Confirmation Date）**：RFQ 轉 PO 的日期
- **預計到貨日（Expected Arrival Date）**：預計到貨日
- 底部**總金額**：使用此範本的累計採購金額

---

## PAL10 EDI 採購單 → 銷售訂單 SOP

### 買方端（採購應用 Purchase App）

1. 建立詢價單（RFQ）→ 加入產品 → 點「確認訂單（Confirm Order）」→ 轉為採購單（PO） [01:39]

### 廠商端（入口網站視圖 Portal View）

1. 廠商從 Email 或入口網站（Portal）登入
2. 查看「我方訂單（Our Orders）」→ 找到相關 PO [02:01]
3. 點「**連結至您的軟體（Connect with your software）**」按鈕 [02:35]
4. 彈窗說明上傳方式（支援 XML 或拖放 PDF）
5. 複製 XML URL → 於新分頁貼上 → 自動下載 `.xml` 檔案

### 廠商端（銷售應用 Sales App，接收方）

1. 進入廠商自己的 Odoo → **銷售（Sales）** 應用
2. 點左上「**上傳（Upload）**」按鈕 [03:17]
3. 選取剛下載的 XML 檔
4. 系統自動建立銷售訂單（Sales Order）：
   - 客戶欄位（Customer）= 買方公司自動填入
   - 產品、數量、價格全部帶入
   - XML 檔案存於留言紀錄（Chatter，可追溯）

---

## 版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v0.1（草稿） | 2026-07-22 | 依 PAL01–PAL10 影片逐字稿初次整理 |
| v0.2（草稿） | 2026-07-23 | 全文補上中文對照，統一為「中文（English）」格式（依 Jenny 回饋：英文不好，需中文+英文並列） |

*本文件為草稿，依據 PAL01–PAL10 影片逐字稿整理，實際操作細節請以當前部署版本為準。*
