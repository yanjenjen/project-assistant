# Odoo Inventory 模組 - Demo 情境腳本

> 模組：Inventory（庫存）
> 版本標示：Odoo 17（依影片介面與功能推測，待確認）
> 學習日期：2026-07-30
> 狀態：草稿
> 資料來源：37 支官方教學影片（INV01–INV37）

---

## Demo 01：基本入庫出庫完整流程

### 業務背景
Stealthy Wood 家具公司從廠商 Gemini Furniture 訂購了 100 片木板（Wood Panels），入庫後立即有客戶 Deco Addict 下訂要求交貨。展示 PO → Receipt → SO → Delivery 的標準流程。

### 前置設定
- 產品「Wood Panels」已設定 Product Type = Goods、Track Inventory 已勾選
- Gemini Furniture 已設為廠商（Purchase Tab → Vendors）
- 庫存設定：Storage Locations 已啟用（1 步驟收發）

### 操作步驟

**Part A：採購入庫**

1. **採購下單**（Purchase App）
   - Purchase → New → 廠商選 Gemini Furniture
   - 加入 Wood Panels，數量 100 → Confirm Order

2. **收貨驗收**（Inventory App）
   - Inventory 主儀表板 → Receipts 卡片 → 開啟對應收貨單
   - 確認 Source Document = PO 編號；Demand = 100
   - Quantity 欄確認實際到貨數量
   - Destination Location 設定為 WH/Stock → Validate
   - 若全數到齊 → No Back Order

3. **確認入庫**
   - 點擊 Move Smart Button：確認 100 片已移至 WH/Stock
   - Inventory → Operations → Physical Inventory：確認在手數量 = 100

**Part B：銷售出庫**

4. **接收客戶訂單**（Sales App）
   - Sales → New → 客戶選 Deco Addict
   - 加入 Wood Panels，數量 10 → Confirm

5. **執行出貨**（Inventory App）
   - Inventory 主儀表板 → Delivery Orders → 開啟對應出貨單
   - 確認 Product Availability = 綠色 Available
   - Validate → 完成出貨

6. **確認庫存更新**
   - Physical Inventory：Wood Panels 在手數量應更新為 90

### 預期結果
- Inventory Valuation 反映 90 片 Wood Panels
- SO Smart Button 顯示出貨 Validated
- Moves History 清楚記錄 PO 入庫與 SO 出庫兩筆移動

---

## Demo 02：補貨規則自動觸發

### 業務背景
Stealthy Wood 的「Coffee Table（咖啡桌）」設有自動補貨規則：最小庫存 100 件、最大 200 件。當庫存因銷售低於 100 件時，系統次日自動產生 RFQ，採購團隊確認後接收。

### 前置設定
- 產品「Coffee Table」已設 Track Inventory、Purchase Checkbox 已勾選
- 廠商「Coffee Vendor」已在 Purchase Tab 設定，Lead Time = 1 天、Unit Price = $20
- 自動補貨規則：Min = 100、Max = 200、Trigger = Auto

### 操作步驟

1. **確認補貨規則設定**
   - 開啟 Coffee Table 產品 → Reordering Rules Smart Button
   - 確認規則：Min = 100、Max = 200、Trigger = Auto
   - 查看 Forecasted Quantity（目前低於 100）

2. **等待排程器（或手動觸發）**
   - 手動觸發：Inventory → Operations → Replenishment → Order（全部）
   - 系統自動計算 Suggested Quantity = 200 - Forecasted Qty

3. **確認 RFQ 產生**
   - Purchase App → 找到 Coffee Vendor 的新 RFQ
   - 確認產品、數量、預計到貨日（= 今天 + 1 天 Lead Time）
   - Confirm Order → 轉為 PO

4. **接收到貨**
   - 隔天：Inventory → Receipts → 開啟對應收貨單 → Validate

5. **確認庫存恢復**
   - Physical Inventory：Coffee Table 在手數量已回補至 200

### 預期結果
- PO Source Document 顯示「OP」前綴（Order Point = 補貨規則觸發）
- 補貨 RFQ 以「草稿」狀態等待採購人員確認，不直接產生已確認 PO
- 預計到貨日已計入廠商 Lead Time

---

## Demo 03：批次揀貨（Batch Picking + Barcode App）

### 業務背景
Stealthy Wood 倉庫收到 5 筆待揀貨訂單。倉庫主管 Wall-E 建立批次，指派揀貨員 Nathan 使用條碼掃描器在一趟中完成所有揀貨，提高效率。

### 前置設定
- Batch/Wave/Cluster Transfers 已啟用
- Storage Locations + Multi-Step Routes 已啟用
- 倉庫設定：Outgoing Shipments = Pick then Deliver（2 Steps）
- 產品已設定 Barcode；儲位已設定 Barcode

### 操作步驟

1. **確認待揀貨訂單**
   - Inventory 主儀表板 → Pick 卡片 → 5 to Process

2. **建立批次**
   - 點擊 Pick 卡片三點選單 → Prepare Batch
   - 點擊 Add a Line → 勾選所有揀貨單（依儲位分配：L 層架給 Nathan）
   - Select → Confirm
   - Responsible = Nathan → 儲存

3. **列印批次條碼清單（選擇性）**
   - 批次頁面 → 齒輪圖示 → Batch Transfer
   - 列印條碼表：第一頁（批次和揀貨單條碼）、第二頁（產品條碼）

4. **Nathan 執行揀貨（Barcode App）**
   - 開啟 Barcode App → Operations → Pick → Batches Tab
   - 掃描批次條碼 → 進入批次揀貨清單
   - 依序：
     - 掃描儲位條碼（確認所在位置）
     - 掃描產品條碼（確認品項）
     - 掃描至數量達到需求（或點 + 快速確認）
   - 所有產品揀完後 → Validate（產品移至 Output）

5. **出貨分揀與驗收（Delivery Team）**
   - Inventory → Delivery Orders 卡片 → N to Deliver
   - 若設定 Automatic Batches by Carrier：自動顯示分組（FedEx / UPS）
   - 開啟各批次 → 核對內容 → Validate

### 預期結果
- 5 張揀貨單合併為 1 趟完成，減少往返次數
- Barcode App 即時更新每個揀貨數量
- 揀貨完成後 Output 位置顯示正確產品與數量
- 出貨批次依承運商自動分組，方便對接 FedEx / UPS

---

## Demo 04：批號追蹤與移除策略（FIFO）

### 業務背景
Stealthy Wood 進口潤滑噴劑（Lubricant），以批號追蹤，並設定 FIFO 移除策略確保先收到的貨先出。客戶訂購時系統自動選擇最早入庫的批號。

### 前置設定
- Lots & Serial Numbers 已啟用
- 產品「Lubricant」設定 Tracking = By Lots
- Shelf F 儲位設定 Removal Strategy = FIFO（First In First Out）

### 操作步驟

1. **分批收貨（建立批號）**
   - 第一次收貨（Lot S1）：驗收 20 罐 → Hamburger Icon → Lot = S1，Qty = 20 → Validate
   - 第二次收貨（Lot S2）：驗收 20 罐 → Lot = S2，Qty = 20 → Validate

2. **確認批號到貨日**
   - Inventory → Products → Lots/Serial Numbers
   - 移除 Location 分組 → Group by Product → 展開 Lubricant
   - 查看 Created On（到貨日）：Lot S1 最早、Lot S2 次之

3. **客戶下訂**（Sales App）
   - 新增 SO → 客戶選 Benjamin → 加入 Lubricant 1 罐 → Confirm

4. **確認揀貨批號**
   - 出貨單 → Operations Tab → 點擊數量旁 Hamburger Icon
   - 查看詳細操作：確認選擇的是 **Lot S1**（最早入庫，FIFO）

5. **Validate 出貨**

### 預期結果
- 系統自動選擇 Lot S1（較早到貨），符合 FIFO 策略
- Traceability Report 顯示完整批號追蹤路徑（廠商 → 入庫 → 出貨給客戶）
- 若有產品召回，可依批號快速找出受影響的所有客戶

---

## Demo 05：寄售庫存（Consignment）入庫與估值確認

### 業務背景
廠商 Wood Hut 將 50 張辦公桌（Office Desk，成本 $200 / 張）寄放在 Stealthy Wood 倉庫銷售。公司代管但不擁有，庫存估值應為 $0，不影響公司資產帳。

### 前置設定
- Consignment 已啟用（Inventory → Configuration → Settings → Traceability）
- 產品「Office Desk」已建立，成本 = $200

### 操作步驟

1. **手動建立收貨單（無 PO）**
   - Inventory 主儀表板 → Receipts → New
   - Receive From：Wood Hut
   - **Assigned Owner：Wood Hut**（此為關鍵欄位）
   - Operations Tab → Add a Line → Office Desk，Demand = 50
   - Validate

2. **確認在手數量**
   - Products → Office Desk → On Hand Smart Button
   - 應顯示 50 Units On Hand

3. **確認庫存估值**
   - Inventory → Reporting → Valuation
   - 找到 Office Desk 列 → Total Value = **$0**
   - 確認系統識別 Wood Hut 為所有人，不計入公司資產

4. **說明差異**（顧問解說點）
   - 若 50 張 × $200 = $10,000，一般應為公司資產
   - 但因 Assigned Owner = Wood Hut，系統自動排除估值 = 寄售庫存不計入公司財務

### 預期結果
- On Hand = 50（物理上在倉庫）
- Inventory Valuation = $0（不屬於公司）
- 使用說明：未來售出時的帳務處理需另行確認（待補資料）

---

## Demo 06：多步驟出貨 + 落地成本分攤

### 業務背景
Stealthy Wood 從海外廠商 Wood Hut 進口 20 組書桌整理器（Desk Organizer），須支付 $2 進口稅（每組 $0.1）。展示落地成本如何提升庫存估值。

### 前置設定
- Accounting App 已安裝
- Landed Costs 功能已啟用（Inventory → Settings → Valuation）
- 產品類別「Office/Furniture」設定：Costing Method = AVCO、Inventory Valuation = Perpetual
- 已建立 Service 類型產品「Import Tax」，Purchase Only、Landed Cost 核取方塊已勾選、Split Method = Equal

### 操作步驟

1. **採購下單**
   - Purchase → New → 廠商 Wood Hut
   - 加入 Desk Organizer，數量 20，Unit Price = $50/組
   - 加入 Import Tax，Unit Price = $2
   - Confirm Order

2. **接收並驗收**
   - Receive Products → Validate

3. **記下收貨單編號**（如 WH/IN/00025）

4. **建立廠商帳單並建立落地成本**
   - 回到 PO → Create Bill（或 Upload Bill）
   - 在草稿帳單頁面點擊 **Create Landed Costs** 按鈕
   - 在落地成本表單：
     - 確認 Import Tax 已列在 Additional Costs
     - Transfers 欄位：搜尋並選擇剛才的收貨單 WH/IN/00025
     - 點擊 **Compute** → 查看 Valuation Adjustments Tab
     - 確認分攤計算（Equal 方式 = 每種產品各 $1）
     - Validate

5. **確認估值更新**
   - Valuation Adjustments Tab：
     - Original Value = $50（原成本）
     - Additional Cost = $2（落地成本分攤後）
     - New Value = $52

### 預期結果
- 每組 Desk Organizer 的庫存成本從 $50 提升至 $52
- 損益分析更準確（若售價 $55，毛利應為 $3，非 $5）
- 帳務分錄自動產生（Inventory → Accounting）

---

*本文件為草稿，依據 INV01–INV37 影片逐字稿整理，實際操作細節請以當前部署版本為準。*
