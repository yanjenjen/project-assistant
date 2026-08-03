# Odoo Website & eCommerce 模組 - 操作 SOP

> 模組：Website + eCommerce
> 版本標示：Odoo（依影片介面推測，待確認）
> 學習日期：2026-07-30
> 狀態：草稿
> 資料來源：26 支官方教學影片（ECM01–ECM26）

---

## SOP-01：使用 Website Configurator 建立網站

**影片來源：** ECM02

### 前置條件
- 尚未建立 Website，或需建立第二個全新網站
- 已確認公司名稱、Logo（可選）、目標客群

### 操作步驟

1. **啟動 Website App**
   - 方法 A（全新安裝 Odoo）：前往 odoo.com → 點選 Website 圖示 → Start Now → 填寫 Email 與網站名稱 → Start Now
   - 方法 B（已安裝 Odoo）：App Store → 點選 Website → Activate；或於 Settings → New Website

2. **選擇網站類型**
   - 選項：企業網站（Business）/ 電子商務（Store）/ 部落格（Blog）/ 線上課程（E-Learning）

3. **選擇行業類別**
   - 輸入關鍵字，系統自動建議（如 Travel Agency、Retail 等）

4. **設定主要目標（影響首頁 CTA 按鈕文字）**
   - 取得詢問（Get Leads）/ 銷售商品（Sell More）/ 品牌建立（Develop the Brand）/ 預約排程（Schedule Appointments）/ 告知顧客（Inform Customers）

5. **設定配色**
   - 方式 A：選擇預設色板
   - 方式 B：上傳 Logo → Odoo 自動提取色系

6. **選擇要建立的頁面**
   - 可選：About Us、Services、Pricing、Privacy Policy、Blog 等

7. **選擇主題（Theme）**
   - 影響全站排版與視覺風格，後續仍可修改

8. **完成建立**
   - 系統自動生成首頁與所選頁面、套用配色與主題

9. **確認基本設定**
   - 前往 Configuration → Settings，確認網站名稱、Favicon（瀏覽器分頁小圖示）

### 注意事項
- 所有選項（配色、主題、頁面）事後均可修改，無需在精靈中做到完美
- 選擇目標會影響首頁 CTA 按鈕，但不影響其他功能

### 控制點
- 確認網站名稱與 Favicon 已正確設定
- 確認首頁 CTA 按鈕指向正確動作

---

## SOP-02：網頁設計（文字/顏色/圖片/動態效果）

**影片來源：** ECM01、ECM03

### 前置條件
- Website App 已安裝，網站已建立
- 已確認品牌配色（Hex 碼或色板方向）

### 操作步驟

#### 2A：設定字型與顏色（全站層級）
1. 在前台點選 **Edit** 進入編輯器
2. 點選 **Theme** 分頁
3. **字型設定**：
   - 分別設定 Paragraph（內文）與 Heading（標題）字型
   - 若所需字型不在清單內：至 fonts.google.com 選擇字型 → 複製 Link 標籤 → 貼至 Odoo「Add a Google Font」欄位 → Save & Reload
4. **配色設定**：
   - 在 Theme 分頁修改 Primary / Secondary Color 及三個輔助色
   - 可參考 colorhunt.co 或 Adobe Color Wheel 選擇色板

#### 2B：自訂文字格式
1. 選取要編輯的文字區塊
2. 工具列提供：粗體、斜體、底線、刪除線、**Highlight（螢光筆特效）**
3. 文字寬度：選取段落 → 設定 Full Width / 50% Width / Small Width

#### 2C：新增與管理圖片
1. 點選現有圖片 → **Replace**
2. 來源選擇：
   - 上傳本地圖片
   - 搜尋 **Unsplash** 免費圖庫（關鍵字搜尋）
3. 設定圖片選項：Padding（間距）、Style、Corner Roundness、Shape（形狀遮罩）
4. 若圖片過重：點選圖片 → 手動調整檔案大小

#### 2D：加入影片背景
1. 選取 Welcome Banner 或任何區塊
2. 點選 **Video** → 貼上 YouTube / DailyMotion / Vimeo 連結 → 確定
3. 影片將自動循環播放作為背景

#### 2E：加入動畫效果
1. 選取任一元素（圖片/文字/按鈕）
2. 點選動畫設定 → 選擇類型（On Scroll / On Appearance）
3. 設定方向（Left/Right/Up/Down）、效果（Fade/Slide/Bounce）

#### 2F：管理 Building Blocks
1. 拖放 Building Blocks 至頁面（四大類：Structure / Features / Dynamic / Inner Content）
2. 調整區塊順序：拖移或使用 ↑↓ 箭頭
3. 複製區塊：點選區塊 → 複製按鈕
4. 儲存自訂範本：點選區塊 → Save → 輸入名稱 → 可在 Custom Templates 找到

### 注意事項
- 點選「Discard」會放棄自上次開啟編輯器以來所有未存的變更
- H1 全頁只能有一個（SEO 原則）
- Theme 分頁變更影響全站；Customize 分頁只影響選取的區塊

### 控制點
- 字型清單中確認新字型已出現
- 儲存後 Reload 頁面確認配色生效
- 儲存後預覽動畫效果是否正常

---

## SOP-03：導覽與選單設定

**影片來源：** ECM05

### 前置條件
- 網站頁面已建立
- 已確認選單結構與連結目標

### 操作步驟

#### 3A：建立連結
1. 在編輯模式下選取文字或圖片 → 點選 **Insert or Edit Link** 按鈕
2. 選擇連結類型：
   - **內部連結**：輸入 `/` + 頁面名稱關鍵字（系統自動搜尋）
   - **外部連結**：直接輸入完整 URL（含 https://）
   - **錨點連結**：先在目標元素點選「Create a link to target this section」建立錨點，再於連結欄位輸入 `#錨點名稱`
3. 設定是否在新分頁開啟（Open in new tab）

#### 3B：將連結轉換為按鈕
1. 選取連結 → Custom → 設定顏色、大小（Small/Medium/Large）、形狀（Default/Outline Round/Fill + Rounded）

#### 3C：設定 Header 選單
1. 點選 Header → 在模板列表選擇版型
2. 點選選單文字 → 直接修改文字內容

#### 3D：使用選單編輯器（Menu Editor）
1. 前台 → **Site** → **Menu Editor**
2. 拖移調整選單項目順序
3. 點選垃圾桶刪除項目
4. 點選「Add a menu item」新增項目（輸入名稱與 URL）
5. **建立子選單**：將項目向右拖移縮排（成為上一層的下拉選單）

#### 3E：新增 Mega Menu
1. 在 Menu Editor 中新增 Mega Menu 類型項目
2. 儲存後在前台點選 Mega Menu 項目 → 選擇模板 → 在格式化大型選單內編輯內容

#### 3F：設定 Footer
1. 點選 Footer → 在模板列表選擇版型
2. 點選社群媒體圖示 → 新增/移除平台 → 填入連結 → 設定顏色與大小

### 注意事項
- 每個頁面最多只有一個 H1（與連結及 SEO 相關）
- 外部連結建議設定為「在新分頁開啟」
- 子選單層級建議不超過 2 層，避免使用者困惑

### 控制點
- 確認所有連結點擊後正確導向
- 確認錨點連結跳轉至正確位置
- 行動版確認漢堡選單可正常展開

---

## SOP-04：商品建立與分類設定

**影片來源：** ECM13、ECM15

### 前置條件
- Website + eCommerce App 已安裝
- 已規劃商品分類結構（父/子分類）
- 若批次匯入：已備好 Excel/CSV 檔與圖片（檔名需一致）

### 操作步驟

#### 4A：建立商品分類
1. **Website → eCommerce → Categories → New**
2. 填寫：
   - 分類名稱
   - Parent Category（若為子分類）
   - 分類圖片（點選鉛筆圖示上傳）
3. 切換至 **Products** 分頁 → 新增屬於此分類的商品
4. 切換至 **Description** 分頁 → 填寫分類描述文字與封面圖片
5. Save

#### 4B：前台建立單一商品
1. 前往 Shop 頁面 → 點選右上角 **New → Product**
2. 填寫：
   - 商品名稱（Name）
   - 銷售價格（Sales Price）
   - 稅率（Taxes）
   - 商品圖片（點選鉛筆圖示上傳）
   - 網站分類（選擇所屬 eCommerce Category）
3. Save → 系統自動產生商品頁面
4. 在頁面上點選 **/** → 可插入 AI 描述、圖片、表格等
5. 點選 **Edit → Style 分頁** 可設定：評論顯示、條款與條件、搜尋列

#### 4C：後台建立單一商品
1. **eCommerce → Products → New**
2. 填寫基本資料（同前台）
3. **General Information 分頁**：產品類型（Goods/Service）、進貨成本、採購稅
4. **eCommerce 分頁**：發布開關、描述、分類、標籤、額外媒體（圖片/YouTube 連結）
5. **Sales 分頁**：選填性商品/配件商品/替代商品（見 SOP-09）
6. **Prices 分頁**：若啟用 Price Lists，可設定適用價格表

#### 4D：批次匯入商品
1. **eCommerce → Products → 齒輪圖示 → Import Records**
2. 下載匯入範本
3. 填寫商品資料（注意欄位對應）
4. 圖片欄填寫檔名（需與上傳圖片檔名完全一致）
5. 點選「Upload Data File」上傳 Excel/CSV
6. 上傳圖片（選取所有商品圖片）
7. 點選「Test」驗證格式 → 出現「Everything seems valid」→ 點選「Import」

### 注意事項
- 商品需關聯至現有分類，儲存後才會自動發布
- 若不想立即發布：在 eCommerce 分頁將發布開關關閉
- 批次匯入時，圖片檔名必須與 Excel 中的圖片欄完全一致（含副檔名）
- 分類順序在清單頁面的排序即為網站顯示的排序

### 控制點
- 確認商品頁面在前台顯示正確（含圖片/價格/分類）
- 確認批次匯入後所有商品圖片均正確對應
- 確認分類顯示在正確的頁面位置（頂部或側邊欄）

---

## SOP-05：商品變體與庫存管理

**影片來源：** ECM14

### 前置條件
- eCommerce App 已安裝
- 已規劃變體屬性（顏色、尺寸等）
- Inventory App 已安裝（進行庫存追蹤）

### 操作步驟

#### 5A：啟用商品變體功能
1. **Website → Configuration → Settings**
2. 在搜尋列輸入「variants」→ 啟用 **Product Variants** → Save

#### 5B：管理屬性
1. 點選設定頁面的 Attributes 連結（或 **eCommerce → Attributes**）
2. 建立屬性（如 Color、Size）及其值（如 Red/Blue、S/M/L）

#### 5C：為商品新增變體
1. 前往商品後台（eCommerce → Products → 選擇商品）
2. 點選 **Attributes and Variants** 分頁
3. 點選「Add a line」→ 選擇屬性 → 選擇所有適用值
4. 可設定多個屬性（如同時有 Color 和 Size）
5. Save → 點選 **Variants** 智慧按鈕確認產生的變體組合數量

#### 5D：設定變體排除組合
1. 在 Attributes and Variants 分頁，點選某屬性列的 **Configure**
2. 在 Exclude for 欄位，選擇要排除的其他屬性值
3. Save → 確認 Variants 智慧按鈕數量減少

#### 5E：為各變體設定圖片與價格
1. 點選 Variants 智慧按鈕 → 選擇特定變體
2. 點選圖片欄鉛筆圖示 → 上傳該變體專屬圖片
3. 調整 Sales Price 為此變體的特定定價
4. 或於 **eCommerce → Attributes → 選擇屬性** → 在屬性值設定「Default Extra Price」（適用全部含此屬性的商品）

#### 5F：設定庫存追蹤與缺貨訊息
1. 在商品表單 General Information 分頁 → 啟用 **Track Inventory**
2. 點選「Quantity on Hand」→ 輸入各變體庫存數量 → Save
3. **eCommerce 分頁**：
   - 設定缺貨時的行為：繼續銷售 或 顯示缺貨訊息
   - 輸入缺貨訊息文字（如「目前缺貨，即將補貨」）
   - 啟用「顯示可售數量」（庫存低於 5 件時顯示剩餘數量）

#### 5G：設定補貨規則
1. 在商品表單 → 點選 **Replenishment** 按鈕
2. New → 設定：
   - Min Quantity（觸發補貨的最低庫存）
   - Max Quantity（補貨目標庫存上限）
3. 系統自動計算需補貨數量
4. Save

### 注意事項
- 屬性的「Variant Creation」設定（Instantly/Dynamically/Never）一旦用於商品即不可變更
- 屬性「Extra Price」會套用至所有含此屬性的商品，若只想改單一商品價格，需在該商品的 Variants 頁面個別設定
- 補貨規則需要 Inventory App 支援

### 控制點
- 確認前台商品頁面可正確切換變體（顏色/尺寸）
- 確認各變體圖片在切換時正確顯示
- 確認缺貨商品顯示正確的缺貨訊息
- 確認特定排除組合不會出現在選擇器中

---

## SOP-06：結帳流程設定（Cart Checkout）

**影片來源：** ECM19

### 前置條件
- eCommerce App 已安裝
- 商品已上架

### 操作步驟

#### 6A：設定加入購物車後的動作
1. **Website → Configuration → Settings**
2. 捲至「Add to Cart」區塊
3. 選擇：停留在商品頁（Stay on product page）或 前往購物車（Go to cart）
4. Save

#### 6B：在商品頁面新增「Buy Now」按鈕
1. 前台進入商品頁面 → **Edit → Style 分頁**
2. 啟用 **Buy Now** 選項 → Save
3. 顧客點選 Buy Now 將直接跳至購物車（略過停留商品頁的設定）

#### 6C：設定結帳額外步驟（Extra Step）
1. 前台進入購物車頁面 → **Edit → Style 分頁**
2. 啟用 **Extra Step** 選項 → Save
3. 在額外步驟頁面上使用 Website Builder 自訂表單欄位（例如：禮品留言、交貨備註）
4. 可刪除/新增/重新排列欄位（操作方式同 SOP-聯絡表單）

#### 6D：啟用條款與條件確認框
1. 在購物車/結帳頁面 → **Edit → Style 分頁**
2. 啟用 **Terms and Conditions** 核取方塊 → Save
3. 顧客在付款前需勾選同意

#### 6E：啟用 B2B 欄位（公司名稱等）
1. 在結帳地址步驟 → **Edit → Style 分頁**
2. 啟用 **B2B Fields** → Save
3. 地址欄位將顯示公司名稱欄位

#### 6F：自訂確認按鈕文字
1. 在付款步驟頁面 → **Edit**
2. 選取「Pay Now」或「Confirm」按鈕文字 → 直接修改 → Save
3. 注意：貨到付款方式自動顯示「Confirm」，不顯示「Pay Now」

### 注意事項
- Extra Step 可完整使用表單建立功能（含條件可見性）
- 已登入且曾填寫地址的顧客，地址欄位會自動帶入
- Quick Reorder 按鈕（在購物車頁面）可讓回頭客一鍵重新訂購

### 控制點
- 測試流程：商品頁 → 加入購物車 → 確認動作符合設定
- 測試 Extra Step 顯示是否正確
- 確認條款與條件框在未勾選時無法付款

---

## SOP-07：配送方式設定

**影片來源：** ECM20

### 前置條件
- eCommerce App 已安裝
- 已確認使用的配送供應商（DHL、UPS、Bpost 或自訂規則）
- 若使用外部供應商：已在供應商網站建立帳號並取得 API 憑證

### 操作步驟

#### 7A：安裝配送供應商
1. **Website → Configuration → Settings → Delivery → Configure Delivery Methods**
2. 頁面顯示所有支援的供應商
3. 找到目標供應商 → 點選 **Install**
4. 或切換至清單檢視 → 多選供應商 → 點選 **Activate**

#### 7B：設定供應商配送方式
1. **Website → Configuration → Delivery Methods** → 選擇剛安裝的方式
2. 填寫供應商憑證（如 Bpost 的帳號與密碼，在 Provider 設定分頁）
3. **Integration 欄位**：
   - **Get Rate**：僅計算費用，手動在供應商網站建立出貨
   - **Get Rate & Create Shipment**：自動向供應商確認出貨（全流程在 Odoo 完成）
4. 設定配送費加成（Margin）
5. 設定免費配送門檻（如訂單滿 50 歐元免運）
6. 在 **Availability 分頁**：設定可服務的目標國家/地區（空白 = 全部）
7. 設定最大重量與最大體積限制
8. 點選 **Publish** 讓顧客可在結帳時看到此方式

#### 7C：建立自訂配送規則（基於規則的費率）
1. **Website → Configuration → Delivery Methods → New**
2. 輸入配送方式名稱
3. Provider 欄位選擇「Based on Rules」
4. 在 **Pricing 分頁** 新增規則：
   - 條件：重量 / 數量 / 訂單金額 等
   - 設定條件值（如 Weight ≤ 0.5 kg）
   - 設定費用公式（如：固定 €3 + €0.80 × 重量）
5. Save → 連結配送商品（此費用需對應一個已發布的 Odoo 商品）
6. 點選 **Publish**

#### 7D：設定商品重量
1. **eCommerce → Products → 選擇商品**
2. 進入 **Inventory 分頁 → Logistics 區塊**
3. 填寫 Weight（公斤）與 Volume 值
4. Save

### 注意事項
- 不發布的配送方式不會出現在顧客結帳頁面
- 自訂規則的配送費用必須連結一個「已發布」的 Odoo 商品，否則費用無法顯示在訂單上
- Click and Collect 的設定方式另見 SOP 相關章節

### 控制點
- 前台結帳測試：確認可選擇的配送方式清單正確
- 確認費率計算公式生效（特別是依重量計費的規則）
- 確認免費配送門檻在訂單金額達標時正確觸發

---

## SOP-08：付款方式設定

**影片來源：** ECM21

### 前置條件
- eCommerce App 已安裝
- 已確定使用的付款供應商（如 Adyen、Stripe 等），並已在供應商網站建立帳號
- 若使用 Click and Collect：已啟用該功能（自動產生「Pay on Site」選項）

### 操作步驟

#### 8A：尋找並安裝付款供應商
1. **Website → Configuration → Settings → Payment → Configure Payment Methods → Find a Payment Provider**
2. 系統顯示兩大類：
   - **Custom（自訂）**：Cash on Delivery（貨到付款）、Wire Transfer（銀行轉帳）、Pay on Site（現場付款）
   - **External（外部）**：Adyen、Stripe、PayPal 等（需帳號）
3. 可在搜尋列輸入支付方式名稱（如 Bancontact、Visa、Card）→ 找到對應供應商 → **Install**

#### 8B：設定付款供應商憑證
1. 安裝後點選 **Activate**（或 Configure）
2. **狀態設定**：
   - **Disabled**：停用
   - **Test Mode**：測試模式（不會真實扣款）
   - **Enabled**：正式啟用
3. 切換至 **Credentials 分頁** → 填寫從供應商網站取得的 API Key / Secret / Merchant ID 等憑證

#### 8C：設定付款行為選項
1. 在 **Configuration 分頁**：
   - **Payment Methods**：確認供應商支援的付款方式（信用卡/數位錢包等）
   - **Allow Saving Payment Method**：允許顧客儲存付款資訊供日後快速結帳（訂閱型商業適用）
   - **Capture Amount Manually**：先授權不立即扣款，待確認可出貨後再手動捕獲金額

#### 8D：設定使用限制
1. 在右側 **Availability 區塊**：
   - 設定最小/最大訂單金額（如最小 €100）
   - 限制適用幣別（多幣別時）
   - 限制適用國家
   - 限制適用 Price Lists

#### 8E：自訂確認訊息
1. 切換至 **Messages 分頁**
2. 調整各狀態（付款授權/付款確認/付款失敗等）對顧客顯示的訊息文字

#### 8F：發布付款方式
1. 確認設定完成 → 點選 **Publish**
2. 前往前台結帳頁面確認付款選項正確顯示

### 注意事項
- 測試模式下的訂單旁會顯示橘色三角形警告圖示
- 正式上線前需從 Test Mode 切換至 Enabled
- 顧客儲存付款資訊功能需謹慎啟用，確認符合 PCI 規範與隱私政策
- 外部供應商的憑證請以供應商官網提供的資料為準

### 控制點
- 在測試模式中完成完整的假交易流程（確認不實際扣款）
- 確認付款後顧客收到正確的確認頁面/訊息
- 確認金額限制正確運作（低於下限時該付款方式不顯示）
- 正式上線前將測試模式切換為 Enabled

---

## SOP-09：訂單管理（後台處理）

**影片來源：** ECM25

### 前置條件
- eCommerce App 已安裝，商品已上架並有實際訂單

### 操作步驟

#### 9A：查看訂單總覽
1. **eCommerce → Orders** 進入訂單 Dashboard
2. 三個主要狀態篩選：
   - **To Fulfill**（需出貨）：Sales Order 狀態，需安排配送
   - **To Confirm**（需確認）：Quotation Sent，顧客已選擇線下付款，等待人工確認
   - **To Invoice**（需開立發票）：已確認但未付款的訂單
3. 使用 Filter 篩選：Unpaid（未付款）/ Abandoned Cart（棄單）等

#### 9B：設定訂單自動化通知
1. **Website → Configuration → Settings**
2. 設定 **Order Assignment**：指派 Sales Team 與 Salesperson（新訂單通知接收人）
3. 設定 **Order Confirmation Email**：選擇或自訂確認 Email 模板
4. 啟用 **Follow-up Abandoned Cart**：設定棄單追蹤 Email 模板與發送時間（預設 10 小時後）
5. 啟用 **Automatic Invoice**：付款確認後自動產生發票並 Email 給顧客
6. 啟用 **Delivery Confirmation Email/SMS**：出貨後自動通知顧客

#### 9C：處理單筆訂單
1. 在 Orders Dashboard 點選目標訂單
2. 確認訂單狀態（Quotation / Quotation Sent / Sales Order）
3. 查看 Chatter（聊天紀錄）確認系統自動執行的動作（發票/付款/出貨通知）
4. 點選 **Delivery** 智慧按鈕 → **Validate** 確認出貨 → 系統自動發送配送確認通知

#### 9D：處理退貨
1. 在 Delivery 頁面 → 點選 **Return** 按鈕
2. 設定退貨數量
3. 選擇：退回庫存（Return）或 換貨同型商品（Exchange）
4. **Validate** → 商品回到庫存
5. 退款部分：前往 Accounting 模組處理信用憑單（請參考 Accounting 教學）

### 注意事項
- 棄單追蹤 Email 只能發送給：已登入顧客，或在結帳時填寫過 Email 的訪客
- 三個訂單階段（Quotation/Quotation Sent/Sales Order）代表不同的付款與結帳狀態，勿混淆
- 退款流程需在 Accounting 模組完成，本 SOP 僅涵蓋退貨庫存部分

### 控制點
- 確認測試訂單從 Quotation → Sales Order 狀態正確流轉
- 確認顧客在正確時間點收到確認 Email / SMS
- 確認退貨後庫存數量正確更新

---

## SOP-10：SEO 設定

**影片來源：** ECM10

### 前置條件
- 網站已建立，主要頁面已完成內容
- 已確認各頁面的目標關鍵字

### 操作步驟

#### 10A：設定 Meta Title 與 Description
1. 前台進入目標頁面 → **Site → Optimize SEO**
2. 在「Preview」視窗中：
   - **Title**：填寫頁面標題（建議 50-60 字元，含主要關鍵字）
   - **Description**：填寫頁面描述（建議 140-160 字元，需獨特，勿重複複製）
   - **URL**：可修改頁面 URL（修改後請同時建立重定向，見 10C）
3. Save

#### 10B：設定關鍵字與確認覆蓋率
1. 在 Optimize SEO 頁面的「Keywords」欄位輸入關鍵字 → 按 Enter 新增
2. 系統顯示關鍵字出現在 H1、H2、Title、Description、Content 的覆蓋情況
3. 根據分析結果，在頁面內容中適當加入缺少的關鍵字
4. 確認內容語意通順，避免關鍵字堆砌

#### 10C：設定圖片 Alt 標籤
1. 在頁面 Edit 模式下 → 點選圖片
2. 填寫 **Description**（圖片無法顯示時的替代文字）
3. 填寫 **Tool Tip**（滑鼠懸停時顯示的文字）
4. 使用相關關鍵字描述，省略「the」「a」等功能詞
5. 注意：使用 Odoo Library 圖片時 Description 會自動填入

#### 10D：建立 URL 重定向
1. 確認開啟開發者模式（Settings → Activate Developer Mode）
2. 複製舊頁面的 URL
3. **Website → Configuration → Redirections → New**
4. 填寫：
   - 名稱（方便識別）
   - 重定向類型（永久移動 = 301）
   - From：舊 URL 路徑
   - To：新 URL 路徑
   - 選擇適用網站（多網站時）
5. Save → 舊 URL 訪問將自動重定向至新 URL

#### 10E：確認技術 SEO 設定
- **Robots.txt**：Settings → 搜尋「robots」→ 可自訂哪些頁面不被爬蟲索引
- **Sitemap**：Odoo 自動生成並更新，無需手動操作
- **hreflang 標籤**：多語言網站時自動生成，確保各語言版本正確關聯

### 注意事項
- 每個頁面只能有一個 H1 標題
- Meta Description 不是直接的排名因素，但影響點擊率
- 重定向後不會失去原有的 SEO 排名（使用 301 永久重定向）
- SEO 效果通常需要 3-6 個月才能看出明顯成效

### 控制點
- 確認所有主要頁面均有填寫 Title 與 Description
- 確認各頁面 Title 長度在 50-60 字元之間
- 確認重定向設定後，舊 URL 可正確轉至新 URL
- 使用 Google Search Console 追蹤實際搜尋表現

---

*本文件為草稿，依據 ECM01–ECM26 影片逐字稿整理。實際操作步驟請以當前部署版本介面為準。*
