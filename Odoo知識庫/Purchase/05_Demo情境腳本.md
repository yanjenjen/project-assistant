# Odoo Purchase 模組 - Demo 情境腳本

> 版本標示：Odoo 17（依影片介面推測，待確認）
> 學習日期：2026-07-22
> 狀態：🔄 草稿
> 說明：依顧問 Demo 情境設計，可依客戶行業調整數字與產品名稱

---

## 情境一：基礎採購流程 - 一次性 RFQ 到收貨
**對應影片**：PAL01  
**適用客戶**：所有行業  
**情境描述**：採購人員需要緊急向廠商採購一批產品，包含議價折扣，並完成收貨。

### 前置條件
- 已建立廠商主檔（如：Azer Interior）
- 廠商已設定廠商價格表（含數量折扣）
- 產品已建立於系統中

### Demo 步驟

1. **進入 Purchase → Dashboard**
   - 說明：儀表板概覽所有 RFQ 狀態（大色塊 = 全公司 / 小色塊 = 我的）

2. **New → 建立 RFQ**
   - Vendor：選廠商
   - Order Deadline：設定本週截止日
   - Products 分頁：加入產品，數量 = 1 → 觀察單價
   - 調整數量至折扣門檻（如 15）→ **單價自動下調**（示範廠商價格表效果）

3. **Send RFQ**
   - 觀察：Email 草稿自動產生（說明節省發信時間）
   - 點 Send → 狀態變為「RFQ Sent」
   - Chatter 留存寄件紀錄

4. **Confirm Order**
   - 廠商回覆接受後 → 點 Confirm Order
   - 說明：狀態由 RFQ Sent → Purchase Order

5. **收貨驗收**
   - 點 Receipt 智慧按鈕
   - Operations 分頁：確認 Demand / Done 數量
   - 點 Validate → 庫存自動更新

### 說明重點
- 整個流程在 Purchase app 一處完成，無需 Email/試算表切換
- 庫存即時更新，Inventory 可立即查到收貨記錄

---

## 情境二：自動補貨 - 補貨規則觸發採購
**對應影片**：PAL02、PAL03  
**適用客戶**：有穩定補貨需求、庫存管理需要自動化的企業  
**情境描述**：設定好前置時間與補貨規則後，Odoo 自動於正確時機提醒採購、計算採購量。

### 前置條件
- 已啟用 Advanced Scheduling（安全前置時間）
- 產品已設定：廠商前置時間（購買分頁廠商價格表 Delivery Lead Time）
- Settings 已設定：Security Lead Time + Days to Purchase
- 產品已建立補貨規則（Min/Max）
- 產品 Purchase 分頁已設定廠商

### Demo 步驟

1. **展示三種前置時間設定**
   - Purchase → Configuration → Settings → Advanced Scheduling
   - 指出三個數字（廠商 7 天 + 安全 2 天 + 詢價 1 天 = 10 天規劃視窗）
   - 說明：這就是 Odoo 會提前多久提醒你下 RFQ

2. **查看補貨報表**
   - Purchase → Operations → Replenishment
   - 找到庫存低於 Min 的產品 → 眼睛圖示查看預測
   - 說明：藍色高亮日期 = 三種前置時間加總的日期

3. **手動觸發補貨**
   - 點 Order → 自動建立 RFQ
   - 前往 Purchase → RFQ 列表 → 找到剛建立的 RFQ
   - 說明：Order Deadline = 今天 + Days to Purchase；Expected Arrival = Deadline + Vendor Lead Time

4. **（選配）展示補貨規則計算**
   - 有未確認銷售訂單的產品 → Run Scheduler
   - 展示 RFQ 數量 = Max Qty + 銷售需求（如 10 + 6 = 16）

### 說明重點
- Odoo 不是在庫存歸零時才提醒，而是提前「前置時間總和」的天數
- 補貨量自動納入銷售需求計算，不會補到剩一點點又要再補

---

## 情境三：採購審核 + 廠商警告 - 控制新進員工採購行為
**對應影片**：PAL05  
**適用客戶**：採購人員組成複雜（新進員工/外包/實習生）、有預算控管需求  
**情境描述**：設定金額審核門檻與廠商/產品警告，防止員工不當採購。

### 前置條件
- 已啟用 Purchase Order Approval 並設定門檻（如 $500）
- 已啟用 Warnings 功能
- 廠商已設定 Warning（如：此廠商回應慢）
- 特定產品已設定 Blocking Message（如：停產品）
- 已建立測試用「一般使用者」帳號（非管理者）

### Demo 步驟（切換帳號展示）

**以主管帳號設定：**
1. Purchase → Configuration → Settings → 展示 PO Approval 開啟 + 金額設定
2. Warnings 啟用展示
3. Orders → Vendors → 選廠商 → Internal Notes → 設定 Warning 文字
4. Products → 選產品 → Purchase 分頁 → Blocking Message 設定

**切換一般使用者帳號：**
5. 建立新 RFQ → 選有警告的廠商 → **自動彈出警告訊息**（不阻擋但提醒）
6. 嘗試加入有 Blocking Message 的產品 → **被完全阻擋**（說明封鎖 vs 警告差異）
7. 建立金額超過 $500 的 RFQ → Confirm Order → 進入「**To Approve**」狀態

**切換回主管帳號：**
8. Purchase → RFQ 列表 → 過濾「To Approve」
9. 點開 RFQ → 點「**Approve Order**」 → 轉為 PO

### 說明重點
- 這是「**預防勝於治療**」的內控設計，不需要靠主管事後追查
- Warning 讓員工有資訊、Blocking 讓系統幫你擋住高風險操作

---

## 情境四：框架訂單 - 年度採購合約分批到貨
**對應影片**：PAL06  
**適用客戶**：有年度採購合約、需要分批到貨、要追蹤合約使用量  
**情境描述**：與廠商簽訂年度供應協議，以優惠總價但分三批交貨。

### 前置條件
- 已啟用 Purchase Agreements 功能
- 廠商主檔已建立

### Demo 步驟

1. **建立框架訂單**
   - Orders → Purchase Agreements → New
   - Agreement Type = Blanket Order
   - 廠商 + 有效期（年度）
   - 填入全年總採購量與議定單價
   - 點 Confirm

2. **分三批建立 RFQ**
   - 點 New Quotation（第一批）→ 設定 Order Deadline（第一批交期）→ 填入 1/3 數量 → Confirm Order
   - 重複建立第二批、第三批（可展示複製技巧：齒輪 → Duplicate）

3. **框架訂單追蹤**
   - 返回框架訂單 → Smart Button 查看子 RFQ/PO 狀態
   - 說明「Ordered」欄位追蹤已確認採購量 vs 協議總量

4. **（選配）走完第一批完整流程**
   - 第一張 PO → Receive Products → Validate → Create Bill → Register Payment
   - 返回框架訂單：展示 Ordered 欄位更新

### 說明重點
- 廠商給年度合約折扣，但你不需要一次拉入全部庫存
- Odoo 自動追蹤每批次狀態與累計金額，不需靠試算表

---

## 情境五：比價採購（Calls for Tender）
**對應影片**：PAL08  
**適用客戶**：公部門採購需留存比價紀錄、私部門尋求最低採購成本  
**情境描述**：同時向三家廠商詢價，比較後選最優廠商確認訂單。

### 前置條件
- 已啟用 Purchase Agreements + Purchase Alternatives
- 已建立 2-3 家廠商主檔

### Demo 步驟

1. **建立第一張 RFQ**（主要廠商）
   - 填廠商 + 產品 → Send by Email

2. **新增替代 RFQ**
   - Alternatives 分頁 → Create Alternative → 選第二家廠商
   - 選擇是否複製產品 → Send by Email

3. **連結第三家獨立 RFQ**
   - 另建一張新 RFQ（第三廠商）→ Send
   - 回到任一 RFQ → Alternatives → Link to Existing RFQ → 選剛建的第三張

4. **比價**
   - Alternatives 分頁 → Compare Products
   - 展示 Odoo 自動標記綠色最低價與最快交期
   - 說明：顧問/採購人員在此做最終判斷

5. **確認最佳廠商**
   - 進入選定廠商 RFQ → Confirm Order
   - 彈窗：Cancel Alternatives → 其餘 RFQ 自動取消

### 說明重點
- 公部門可用此功能留存完整比價紀錄，符合採購法規要求
- Compare Products 頁面即比價結果頁，可截圖存檔

---

## 情境六：EDI 跨資料庫採購轉銷售
**對應影片**：PAL10  
**適用客戶**：買賣雙方都使用 Odoo 的情境；展示 Odoo to Odoo 整合亮點  
**情境描述**：買方在 Odoo 建立 PO，廠商直接上傳至自己的 Odoo，自動生成銷售訂單。

### 前置條件
- 兩個 Odoo 資料庫（買方 + 賣方）
- 廠商已設定 Portal Access

### Demo 步驟（雙螢幕或分頁切換展示）

**買方 Odoo：**
1. Purchase → New RFQ → 填廠商（Joel Willis）+ 產品
2. Confirm Order → 轉為 PO
3. 說明廠商可在入口網站看到此 PO

**廠商 Portal（模擬切換）：**
4. 廠商登入 Portal → Our Orders → 找到 PO
5. 點「Connect with your software」→ 說明彈窗（支援 XML / PDF 拖放）
6. 複製 XML URL → 新分頁貼上 → 自動下載 .xml 檔

**賣方 Odoo（廠商自己的 Sales app）：**
7. Sales → Upload → 選 XML 檔
8. 展示自動產生的 Sales Order：Customer / 產品 / 數量 / 價格全部帶入
9. Chatter 顯示 XML 來源檔（說明：可追溯性）

### 說明重點
- 完全無需人工重新輸入，消除資料轉換錯誤風險
- 適合供應商一體化、集團企業 Odoo 多資料庫的情境

---

## Demo 快速選用指南

| 客戶痛點 | 推薦情境 |
|---------|---------|
| 採購靠 Email，不知道訂單狀態 | 情境一（基礎流程） |
| 常常缺貨或庫存積壓 | 情境二（自動補貨） |
| 新員工採購超預算 | 情境三（審核 + 警告） |
| 有年度合約但管理困難 | 情境四（框架訂單） |
| 需要比價 / 公部門採購 | 情境五（比價採購） |
| 客戶供應商都用 Odoo | 情境六（EDI） |

---

*本文件為草稿，情境資料（廠商名、產品名、金額）為範例，實際 Demo 請依客戶行業調整。*
