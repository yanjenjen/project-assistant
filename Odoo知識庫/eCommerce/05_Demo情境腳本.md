# Odoo Website & eCommerce 模組 - Demo 情境腳本

> 模組：Website + eCommerce
> 版本標示：Odoo（依影片介面推測，待確認）
> 學習日期：2026-07-30
> 狀態：草稿
> 資料來源：26 支官方教學影片（ECM01–ECM26）

---

## Demo 情境 1：從零建立電商網站（Website Configurator）

**對應影片：** ECM02、ECM01、ECM03
**Demo 時間預估：** 10–15 分鐘
**適用場景：** 展示如何在 5 分鐘內建立完整網站骨架，並快速完成視覺設計

### 前提條件
- 已準備好公司 Logo 檔案（PNG，背景透明為佳）
- 已確認公司品牌色系（至少有一個主色的 Hex 碼）
- Odoo 已安裝 Website App（或使用全新資料庫示範）

### Demo 步驟

**Step 1：啟動 Website Configurator（2 分鐘）**
1. 進入 Website App → 首次安裝會自動觸發 Configurator
2. 選擇：「我要建立一個電子商務網站（Store）」
3. 選擇行業：輸入「Ceramic」或目標行業關鍵字

**Step 2：設定網站目標與品牌（2 分鐘）**
1. 目標選擇：「Sell More（銷售商品）」
2. 上傳 Logo → 觀察 Odoo 自動提取品牌色
3. 選擇網站頁面：勾選「About Us」、「Shop」、「Contact」

**Step 3：選擇主題（1 分鐘）**
1. 瀏覽 3-5 個主題預覽
2. 選擇適合品牌調性的主題
3. 點選確認 → 網站自動生成

**Step 4：展示快速調整（5 分鐘）**
1. 進入 Edit → Theme 分頁
2. 修改主色為品牌色（貼上 Hex 碼）
3. 修改字型（從 Google Fonts 選擇一個更符合品牌感的字型）
4. 在首頁加入一個 Feature 類型的 Building Block（拖放示範）
5. 從 Unsplash 搜尋「ceramics」插入一張圖片
6. Save → 呈現完整網站成果

### 驗證點
- [ ] 網站已正確顯示公司名稱與 Logo
- [ ] 配色符合品牌色（主色/次色均正確）
- [ ] 首頁有 CTA 按鈕且指向 Shop 頁面
- [ ] 所有選擇的頁面（About Us/Contact）已建立在選單中
- [ ] 行動版預覽（切換行動圖示）顯示正常

---

## Demo 情境 2：建立商品並上架（含變體）

**對應影片：** ECM13、ECM14、ECM15、ECM17
**Demo 時間預估：** 15–20 分鐘
**適用場景：** 展示完整的商品上架流程，從建立到前台顯示

### 前提條件
- 電商網站已建立
- 已備好商品圖片（至少 1–2 張）
- 已決定商品分類結構（至少建立 1 個父分類）

### Demo 步驟

**Step 1：建立商品分類（3 分鐘）**
1. **eCommerce → Categories → New**
2. 名稱：「Mugs」
3. 上傳分類圖片
4. Description 分頁：填寫分類描述文字
5. Save → 在分類清單中拖移至正確排序位置

**Step 2：從後台建立商品（5 分鐘）**
1. **eCommerce → Products → New**
2. 填寫：商品名稱「Signature Stoneware Mug」、銷售價格 €10
3. 上傳商品圖片
4. **eCommerce 分頁**：
   - 選擇分類：Mugs
   - 點選 **/** → AI → 輸入「Write a short product description」→ 插入生成文字
5. Save

**Step 3：新增商品變體（5 分鐘）**
1. 點選 **Attributes and Variants 分頁**
2. Add a line → 選擇「Color」→ 加入 Oatmeal、Slate Gray、Chalk White
3. Add a line → 選擇「Size」→ 加入 S、M、L
4. Save → 點選 Variants 智慧按鈕（應顯示 9 個組合）
5. 設定排除組合：在 Size 列點選 Configure → 排除 Chalk White + Size S
6. Save → 確認 Variants 智慧按鈕顯示 8 個

**Step 4：設定各變體價格差異（2 分鐘）**
1. 在 Variants 智慧按鈕中選擇 Size L 的任一顏色
2. 將 Sales Price 從 €10 改為 €15
3. 回到後台：說明「也可以從 eCommerce → Attributes → Size → L 設定統一的 Extra Price」

**Step 5：前台展示成果（3 分鐘）**
1. 點選商品頁的「Go to Website」智慧按鈕
2. 在前台展示：
   - 顏色切換時圖片即時更新（若已為各變體設定圖片）
   - Size L 的價格顯示 €15（與 S/M 不同）
   - 小型示範：選擇 S + Chalk White → 該組合不可選（已排除）

### 驗證點
- [ ] 商品已在 Mugs 分類下正確顯示
- [ ] 前台商品頁可切換顏色與尺寸
- [ ] 被排除的組合確實無法選取
- [ ] Size L 顯示正確的價差金額
- [ ] 商品頁顯示 AI 生成的描述文字（已儲存）

---

## Demo 情境 3：完整顧客購物流程（加入購物車 → 結帳 → 付款）

**對應影片：** ECM19、ECM20、ECM21、ECM23
**Demo 時間預估：** 10–15 分鐘
**適用場景：** 展示顧客視角的完整購物體驗，重點呈現 Odoo 電商結帳流程的彈性

### 前提條件
- 至少一個商品已上架
- 已設定至少一種配送方式（可使用自訂規則）
- 已設定至少一種付款方式（建議使用 Wire Transfer 方便示範）

### Demo 步驟

**Step 1：顧客瀏覽與加入購物車（2 分鐘）**
1. 切換至 Incognito（無痕）模式，模擬真實顧客視角
2. 瀏覽 Shop 頁面
3. 展示商品過濾器（若已設定 Sidebar Filters）
4. 選擇商品 → 選擇顏色和尺寸變體 → 點選 **Add to Cart**
5. 如已設定「Buy Now」按鈕 → 也可示範快速購買路徑

**Step 2：購物車確認（2 分鐘）**
1. 展示購物車頁面
2. 若已設定 Accessory Products → 展示配件推薦出現在購物車下方
3. 修改商品數量 → 小計即時更新
4. 點選 **Checkout**

**Step 3：填寫地址（2 分鐘）**
1. 展示結帳第一步（地址填寫）
2. 說明：若顧客有帳號，地址會自動帶入
3. 示範 B2B 欄位（若已啟用）：公司名稱欄位顯示
4. 填入測試地址 → Continue

**Step 4：選擇配送方式（2 分鐘）**
1. 展示已設定的配送方式清單
2. 若已設定 Click & Collect → 切換展示地圖選取點
3. 選擇自訂配送方式（Green Mobility）→ 確認費率計算公式（€3 + €0.80 × 重量）
4. Continue

**Step 5：額外步驟 - 禮品留言（1 分鐘，若已設定）**
1. 展示 Extra Step 頁面（禮品留言表單）
2. 填入留言 → Continue

**Step 6：付款與確認（2 分鐘）**
1. 勾選 Terms and Conditions（若已啟用）
2. 選擇 Wire Transfer 付款 → 確認按鈕顯示「Confirm」（非 Pay Now）
3. 點選確認 → 展示訂單確認頁
4. 回到後台：**eCommerce → Orders** → 展示訂單出現在 Quotation Sent 狀態

### 驗證點
- [ ] 購物車正確顯示商品（含選擇的變體）
- [ ] 配送費用正確計算
- [ ] 訂單確認頁顯示正確的訂單摘要
- [ ] 後台訂單清單正確出現此訂單
- [ ] 顧客收到確認 Email（若已設定）

---

## Demo 情境 4：促銷活動設定（Gift Cards / Loyalty / eWallet）

**對應影片：** ECM24、ECM16
**Demo 時間預估：** 15–20 分鐘
**適用場景：** 展示 Odoo 電商的促銷工具組合，適合展示給重視顧客留存的品牌

### 前提條件
- 已在 Settings 啟用「Discounts, Loyalty & Gift Cards」選項
- 至少兩個商品已上架

### Demo 步驟

**Step 1：建立忠誠積點計劃（5 分鐘）**
1. **eCommerce → Loyalty（或 Settings 連結）→ New**
2. 選擇程式類型：Loyalty Card
3. 命名：「VIP Loyalty」
4. 積點名稱：改為「Glazed Points」
5. 設定積點規則：
   - 最低消費：€20
   - 每 €1 消費 → 50 積點
6. 設定獎勵：
   - 兌換 1000 積點 → 享 5% 折扣
7. 勾選「Available on Website」
8. Save → 命名程式 → Save

**Step 2：建立促銷代碼（Promo Code）（3 分鐘）**
1. **eCommerce → Price Lists → New**
2. 命名：「Welcome10」
3. 在 Rules 分頁：Add a line → 類型「Discount」→ 折扣 10% → Apply on All Products
4. 在 eCommerce 分頁：填入 Promotional Code「WELCOME10」
5. 不勾選 Selectable（僅持有代碼者可使用）
6. Save

**Step 3：建立禮品卡（3 分鐘）**
1. **eCommerce → Gift Cards & eWallets → New**
2. 命名：「Gift Card €20」
3. 確認類型：Gift Card
4. 確認已連結的商品（已在 eCommerce 上架的「Gift Card」商品）
5. 點選 Generate：
   - 匿名（Anonymous）
   - 數量：10 張
   - 面額：€20
6. 產生後點選「10 Gift Cards」智慧按鈕 → 展示代碼清單
7. 展示如何複製連結分享

**Step 4：前台示範完整使用流程（5 分鐘）**
1. 以已有積點的帳號登入（或事先操作累積積點）
2. 前往 Shop → 加入商品至購物車（金額超過 €20）
3. 進入結帳 → 展示積點可兌換的折扣和免費配送
4. 點選 Claim → 折扣自動套用
5. 在折扣代碼欄輸入「WELCOME10」→ 點選 Apply → 追加 10% 折扣
6. 若有 eWallet 餘額 → 展示以 eWallet 支付

### 驗證點
- [ ] 忠誠計劃在顧客 My Account 頁面可見積點餘額
- [ ] 滿足消費條件時，結帳頁面出現可兌換的獎勵
- [ ] 促銷代碼輸入後正確套用折扣
- [ ] 禮品卡代碼可成功抵扣金額
- [ ] 所有折扣疊加後的最終金額計算正確

---

## Demo 情境 5：訂單管理（後台處理）

**對應影片：** ECM25、ECM26
**Demo 時間預估：** 10 分鐘
**適用場景：** 展示電商訂單如何在 Odoo 後台流轉，適合展示給 Operations / 客服團隊

### 前提條件
- 已有至少一筆測試訂單（從 Demo 情境 3 產生）
- 已設定 Order Confirmation Email 範本
- 已啟用 Automatic Invoice

### Demo 步驟

**Step 1：訂單 Dashboard 總覽（2 分鐘）**
1. **eCommerce → Orders**
2. 說明三個主要 Kanban 欄：
   - To Fulfill：已付款待出貨
   - To Confirm：已選擇線下付款方式（待人工確認）
   - To Invoice：已確認但待開立發票
3. 示範 Filter 功能：切換「Unpaid」或「Abandoned Cart」篩選

**Step 2：設定訂單自動化（3 分鐘）**
1. **Configuration → Settings**
2. 展示並說明各項設定：
   - Order Assignment：Website 訂單指派給「網站銷售團隊」
   - Confirmation Email：自動發送訂單確認 Email
   - Abandoned Cart Follow-up：10 小時後自動發送棄單追蹤 Email
   - Automatic Invoice：付款後自動產生發票
3. 說明棄單追蹤的商業價值（回收 5-15% 的棄單訂單）

**Step 3：處理一筆銷售訂單（3 分鐘）**
1. 從 Orders 開啟一筆「Sales Order」狀態的訂單
2. 展示 Chatter 紀錄：自動產生的 Email 通知時間軸
3. 點選「Invoice」智慧按鈕 → 展示自動產生的發票
4. 返回訂單 → 點選「Delivery」智慧按鈕
5. Validate 出貨 → 觀察 Chatter 新增配送確認紀錄

**Step 4：展示交叉銷售設定（2 分鐘）**
1. **eCommerce → Products** → 選擇主力商品
2. Sales 分頁：展示三種推薦商品類型
   - Optional Products（加入購物車時推薦）
   - Accessory Products（購物車頁推薦）
   - Alternative Products（商品頁下方顯示）
3. 切換前台 → 展示各位置的推薦商品如何呈現給顧客

### 驗證點
- [ ] 訂單在 Chatter 中有完整的狀態流轉紀錄（建立 → 付款 → 發票 → 配送）
- [ ] 出貨 Validate 後，顧客 Email/SMS 確認自動發出
- [ ] 前台購物流程中可見到已設定的 Optional/Accessory/Alternative Products
- [ ] 退貨流程可正常執行（庫存正確回沖）

---

*本文件為草稿，依據 ECM01–ECM26 影片逐字稿整理。Demo 步驟中的公司名稱與商品為範例，實際 Demo 時應替換為客戶行業相關的內容。*
