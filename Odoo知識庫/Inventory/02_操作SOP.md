# Odoo Inventory 模組 - 操作 SOP

> 模組：Inventory（庫存）
> 版本標示：Odoo 17（依影片介面與功能推測，待確認）
> 學習日期：2026-07-30
> 狀態：草稿
> 資料來源：37 支官方教學影片（INV01–INV37）

---

## SOP-01：基本入庫收貨流程（1 步驟）

### 前置條件
- 產品已建立（Product Type = Goods、Track Inventory 已勾選）
- Storage Locations 已啟用
- 已存在來自 Purchase Order 或手動建立的 Receipt

### 操作步驟

1. **進入收貨清單**
   - Inventory → 主儀表板 → Receipts 卡片 → 點擊「N to Receive」

2. **開啟待收收貨單**
   - 點選對應收貨單（Source Document 顯示關聯 PO 編號）

3. **核對到貨數量**
   - 在 Operations Tab 中，確認 Demand（訂購量）與實際到貨量
   - 若數量不符，手動修改 Quantity 欄位

4. **設定目標儲位**
   - 在表頭的 Destination Location 欄位選擇正確儲位（如 Warehouse Stock / Shelf 3）

5. **儲存並驗收**
   - 點擊 Save → 點擊 Validate

6. **處理 Back Order（數量不足時）**
   - 彈出視窗選擇：
     - **Create Back Order**：期待剩餘數量後續到貨，建立待收單
     - **No Back Order**：不建立，本次收貨結束

7. **確認入庫結果**
   - 點擊 Move Smart Button 確認庫存已移至目標儲位
   - 至 Operations → Physical Inventory 查看在手數量更新

### 注意事項
- 條碼掃描器可從 Barcode App 直接掃描包裹條碼開啟對應收貨單
- 未設定 Track Inventory 的產品（如耗材）不會出現在 Physical Inventory

### 控制點
- Demand vs Quantity 差異 → 需調查是否有少裝或規格不符
- 儲位填寫錯誤 → 使用 Physical Inventory → Actions → Relocate 修正

---

## SOP-02：出庫出貨流程（2 步驟：Pick → Deliver）

### 前置條件
- Multi-Step Routes 已啟用
- 倉庫設定為「Pick then Deliver（2 Steps）」
- 來自 Sales Order 已確認的出貨任務

### 操作步驟

**Step A：揀貨（Pick）**

1. **進入揀貨清單**
   - Inventory 主儀表板 → Pick 卡片 → 點擊「N to Process」

2. **確認揀貨狀態**
   - 確認 Status = Ready（庫存充足可揀）
   - 查看 Source Document 確認對應 SO

3. **執行揀貨（條碼模式）**
   - 開啟 Barcode App → Operations → Pick
   - 掃描揀貨單條碼 或 手動選取
   - 掃描儲位條碼確認所在位置 → 掃描產品條碼確認品項數量
   - 點擊 Validate 完成揀貨，產品移至 Output 位置

**Step B：出貨（Delivery）**

4. **進入交付清單**
   - Inventory 主儀表板 → Delivery Orders 卡片 → 點擊「N to Deliver」

5. **核對出貨內容**
   - 在 Operations Tab 確認所有產品數量符合
   - 確認 Product Availability 欄位顯示綠色 Available

6. **選擇出貨方式**
   - 若已設定 Shipping Connector（FedEx、UPS），標籤將自動產生
   - 確認 Additional Info 中的 Shipping Method 與 Carrier

7. **驗證出貨**
   - 點擊 Validate → 出貨標籤出現於 Chatter

### 注意事項
- 若 Product Availability 顯示日期而非 Available，表示部分庫存預計到貨日期
- 出貨訂單僅記錄產品「離開倉庫」，實際運送由承運商負責

### 控制點
- 揀貨前確認 Source Location 與 Destination Location 正確
- 條碼掃描可降低揀錯品項的風險

---

## SOP-03：庫存調整（Inventory Adjustment）

### 前置條件
- Storage Locations 已啟用
- 操作員具備 Inventory 存取權限

### 操作步驟

**A. 快速盤點調整**

1. Inventory → Operations → Physical Inventory
2. 在搜尋列使用 Group by Location 整理清單
3. 在 Counted Quantity 欄輸入實際盤點數量
4. 若數量與系統一致，點擊 Set Quantity on Hand（打勾）
5. 發現差異後填入正確數量 → 點擊 Apply All → 輸入原因 → Apply Quantities

**B. 快速歸零**
1. 勾選產品左側 Checkbox → Actions → Set to Zero

**C. 重新定位（誤放儲位）**
1. 勾選錯誤的產品 → Actions → Relocate
2. 選擇正確儲位 → 輸入備註原因 → Confirm

**D. 新增未登錄庫存**
1. Physical Inventory 頁面 → New
2. 填入 Product、Location、Counted Quantity
3. 儲存 → Apply All → Apply Quantities

### 注意事項
- 調整記錄寫入 Moves History 可供稽核
- 設定 Annual Inventory Date 可在 Physical Inventory 頁看到年度盤點倒計時
- 僅 Goods 類型且 Track Inventory 已啟用的產品才會出現

### 控制點
- 差異須調查原因（誤掃、遺失、損壞、計量單位混用）
- 建議記錄調整原因以供日後審計

---

## SOP-04：循環盤點（Cycle Count）設定與執行

### 前置條件
- Storage Locations 已啟用
- 已對至少一個儲位執行過庫存調整（觸發循環計數器）

### 操作步驟

**A. 設定循環盤點頻率**

1. Inventory → Configuration → Locations → 選擇目標儲位
2. 在 Cyclic Counting → Inventory Frequency 填入天數（如 30 天）
3. 手動儲存（雲端圖示）

**B. 分派盤點任務**

1. Inventory → Operations → Physical Inventory
2. 搜尋列 Group by Location
3. 展開目標儲位 → 勾選要盤點的產品
4. 點擊 Request a Count → 指派負責人（Assigned To）→ 設定日期 → Confirm

**C. 執行盤點**

1. 負責人至 Physical Inventory（或 Barcode App）查看待盤點任務
2. 實際清點後在 Counted Quantity 輸入數量
3. Apply All → 輸入盤點名稱（如「First Cycle Count」）→ Apply Quantities

**D. 確認循環更新**
- Apply 後，Scheduled Date 自動跳至未來 N 天（依設定頻率）

### 注意事項
- 循環盤點需完成首次調整後才開始計時
- 可同時指派多個儲位的盤點任務給不同人員

### 控制點
- 盤點差異（如 Solid Oak Legs 預期 62 實際 58）需追查原因
- 每次盤點後系統自動安排下次盤點日期，確保持續執行

---

## SOP-05：補貨規則設定（Reordering Rules）

### 前置條件
- 產品 Product Type = Goods、Track Inventory 已啟用、Purchase Checkbox 已勾選
- 已設定至少一個廠商（Purchase Tab → Vendors）
- 廠商已設定 Delivery Lead Time

### 操作步驟

**A. 建立手動補貨規則**

1. 開啟產品頁 → Reordering Rules Smart Button → New
2. 填入：
   - Min Quantity（最小庫存量）
   - Max Quantity（最大庫存量）
   - Trigger = Manual
3. 儲存 → 當庫存不足時點擊 Order 按鈕觸發 RFQ

**B. 建立自動補貨規則**

1. 開啟產品頁 → Reordering Rules Smart Button → New
2. 填入 Min / Max Quantity
3. Trigger = Auto
4. 儲存後等待 Odoo 每日排程器（Scheduler）自動掃描
   - 手動觸發：Inventory → Operations → Replenishment → Run Scheduler（或單個產品 Order 按鈕）

**C. 多倉庫補貨規則**

1. 在子倉庫的 Warehouse → Configuration Tab 設定 Resupply from 來源倉庫
2. 在產品 Inventory Tab 勾選子倉庫的補貨路線
3. 設定補貨規則時選擇 Location = 子倉庫 Stock

### 注意事項
- 預測數量（Forecasted Qty）包含確認的進貨訂單與待出的銷售訂單
- 自動規則在 Scheduler 執行後才產生 RFQ，RFQ 仍需人工確認為 PO

### 控制點
- 廠商 Lead Time 設定正確，確保建議訂單日期合理
- 確認補貨規則的 Route 設定（如多倉庫時需選擇正確補貨路線）

---

## SOP-06：Lots 與 Serial Numbers 追蹤入庫

### 前置條件
- Lots & Serial Numbers 已啟用
- 產品設定 Track Inventory = By Lots 或 By Unique Serial Number

### 操作步驟

**A. 接收時指派批號（Lots）**

1. 開啟 Receipt → Validate（若未設批號會跳出錯誤）
2. 關閉錯誤 → 點擊數量欄旁的清單圖示（Hamburger Icon）
3. 在詳細操作視窗：
   - 若同一批到貨同一批號：直接在 Lot/Serial Number 欄填入批號
   - 若分多批號：點擊 Add a Line 分行填入各批號及數量
4. 儲存 → 回主頁點擊 Validate

**B. 接收時指派序號（Serial Numbers）**

1. 同上開啟詳細操作視窗
2. 選擇方式：
   - **手動**：Add a Line 逐一填入序號
   - **匯入**：Import Serials/Lots → 貼上序號清單
   - **自動產生**：Generate Serials/Lots → 填入前綴與起始號碼 + 數量 → Generate
3. 儲存 → Validate

**C. 查看追蹤報告**

1. Inventory → Products → Lots/Serial Numbers
2. 點選特定批號 → Smart Buttons 查看位置、可追溯性、採購、銷售
3. 點擊 Traceability Smart Button 查看完整移動路徑

### 注意事項
- 出庫時 Odoo 依移除策略自動選擇批號，在詳細操作中可確認
- 追蹤報告可用於產品召回與品質問題追查

### 控制點
- 接收時批號/序號必須填寫完整，否則無法 Validate
- 確認 Lot 的到期日是否需要在接收時設定（易腐品）

---

## SOP-07：批次揀貨（Batch Transfers）

### 前置條件
- Batch/Wave/Cluster Transfers 已啟用
- Storage Locations + Multi-Step Routes 已啟用
- 倉庫設定為 2 步驟出貨（或以上）

### 操作步驟

**A. 手動建立批次**

1. Inventory 主儀表板 → Pick 卡片 → 點擊三點選單 → Prepare Batch
2. 在批次視窗點擊 Add a Line → 勾選要加入的揀貨單 → Select
3. 點擊 Confirm → 設定 Responsible（負責人）→ 儲存
4. （DMS 情境）選擇 Vehicle（車輛）查看重量/體積使用率

**B. 執行批次揀貨（Barcode App）**

1. 開啟 Barcode App → Operations → Pick → Batches Tab
2. 選取或掃描批次條碼
3. 依位置提示逐一掃描儲位條碼與產品條碼確認數量
4. 點擊 Validate 完成揀貨，產品移至 Output 位置

**C. 自動批次（依 Carrier 分組）**

1. Inventory → Configuration → Operation Types → Delivery Orders
2. 勾選 Automatic Batches → 分組方式選 Carrier
3. 揀貨完成後，Delivery Orders 卡片自動顯示依 Carrier 分好的批次
4. 開啟批次 → 確認內容 → Validate

### 注意事項
- 批次揀貨減少來回移動時間，適合大型倉庫
- 揀貨完成後在 Output Location 進行訂單分揀（依載體分批）

### 控制點
- DMS 情境下需確認批次重量/體積未超過車輛上限
- 自動批次設定 Carrier 分組前需先設定 Shipping Methods

---

## SOP-08：列印出貨標籤

### 前置條件
- 已啟用並設定 Shipping Connector（如 FedEx、UPS）
- Shipping Method 設定：Integration Level = Get Rate & Create Shipment
- 公司地址與電話已在 Settings → Company 填寫
- 客戶地址與電話已在 Contacts 填寫
- 產品重量已在 Inventory Tab → Logistics → Weight 填寫

### 操作步驟

1. 開啟 Sales App → New（建立新詢價單）
2. 填入客戶 → 加入產品
3. 點擊右下角 Add Shipping → 選擇 Shipping Method（如 FedEx US）→ Get Rate
4. 確認運費金額 → Add → Confirm（轉為 SO）
5. 點擊 Delivery Smart Button → 進入出貨單
6. 確認產品備齊後點擊 Validate
7. 出貨標籤自動出現於 Chatter → 點擊下載/列印 → 貼附於包裹

### 注意事項
- 測試環境（Test Environment）的標籤不會真正通知承運商，正式作業前需切換至 Production Environment
- 若連線帳號設定有誤，Get Rate 會回傳錯誤

### 控制點
- 確認 Shipping Method 的 Configuration Tab 帳戶憑證正確
- 確認包裹類型（Package Type）與實際包裝相符，影響運費計算

---

*本文件為草稿，依據 INV01–INV37 影片逐字稿整理，實際操作細節請以當前部署版本為準。*
