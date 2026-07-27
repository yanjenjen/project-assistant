# Odoo 轉檔工作流與匯入範本規範

> 版本：v0.8（草稿，納入採購模組實測回饋：公司在地化設定訂為第一關卡、聯絡人範本補回email/phone基本欄位、幣別不會自動連動既有紀錄）
> 建立日期：2026-07-27｜最後更新：2026-07-27
> 狀態：🟡 草稿 — 第 7、8.1~8.7、8.3a 節均已用 Odoo 官方文件或原始碼查證（8.7 的 `account.move.line.account_id` 信心度略低，未獨立開檔覆核）；7.7（Selection 鍵值查詢路徑）仍為 NotebookLM 整理未覆核；模組相依順序（第 3 節）與命名規則（第 4 節）待第一個正式案例驗證
> 練習場域：`艾創點數位-ERP顧問/經銷商業態案例_去識別化Demo環境建置/`（邊做邊學，本文件依此案例的實務經驗逐步歸納）
> 負責角色：員工_03_流程內控助理（海瑟姆）主責歸納；員工_02_文件資料助理（小果）負責範本製作
> 適用範圍：所有需要把舊系統/來源資料轉換成 Odoo 可匯入格式的專案（企業導入案、Demo 環境建置皆適用）
> 依據來源：Odoo 19 官方文件 `applications/essentials/export_import_data.html`；Odoo 19 官方原始碼 GitHub `odoo/odoo` 19.0 分支（res_partner.py、product_template.py、product_category.py、sale_order.py、account/models/product.py、stock_quant.py）；使用者透過 NotebookLM 查證整理的部分另行標示

---

## 1. 文件目的

規範「轉檔工作流」（把來源資料轉換成 Odoo 可匯入格式，並實際匯入）的標準做法，讓每個新 Odoo 專案不用從零摸索。內容取自經銷商業態 Demo 案例的實務紀錄＋ Odoo 官方文件/原始碼查證，逐步從「單一案例觀察」收斂為「有依據的通則」。未標示 ✅ 的段落，代表尚無足夠依據，不得直接當成放諸四海皆準的通則。

---

## 2. 核心原則

**2.1 一個 Excel＝一個模組**：匯入用 Excel 範本，一個檔案對應一個 Odoo 模型（如 Contacts、Products），不同模組不合併在同一個活頁簿。表頭+明細（如報價單頭/身）視為同一模組的兩個分頁，仍算一個模組。

**2.2 MD 與 Excel 分工**：MD 負責「轉檔工作流」與「SOP 說明」（階段順序、欄位對應決策、問題與解法、進度追蹤）；Excel 負責「匯入格式」本身（實際上傳給匯入精靈的資料檔）。

**2.3 Excel 範本的交付定位**：匯入範本屬於「交付客戶填寫用」性質，比照 `專案資料夾結構與歸檔規則.md` 的 `100_專案執行與交付/140_轉檔匯入範本`（已於 2026-07-27 正式納入該規則第 9 節）存放。

---

## 3. 轉檔工作流階段架構

**3.1 通用原則（✅ 官方文件確認）**：Odoo 官方文件明訂「被參照方一定要先匯入，參照方才能匯入」——原文："To import those relations, the records of the related object need to be imported first, from their own list menu." / "Keep in mind to first import the companies, and then the people." 這條原則決定了模組匯入順序編號的排法，詳見第 8.8 節全局順序。

**3.2 經銷商業態 Demo 案例的實際執行紀錄**：⚠️ 僅為個案脈絡保留，**不建議援用**，已知有三個瑕疵——漏了產品分類步驟（先匯產品才發現缺分類，事後用 XML-RPC 補標籤）、業務員排序無通則依據（該欄位是選填 Many2one，理論上可晚點用更新匯入補上）、未涵蓋公司/幣別/會計基礎。完整順序紀錄見 `經銷商業態案例_去識別化Demo環境建置/02_Demo環境建置紀錄/Odoo資料匯入SOP.md`。**新專案請直接參考第 8.8 節，不要複製本節。**

---

## 4. Excel 匯入範本命名規則（觀察自 Demo 案例，待統一）

目前出現的命名模式：`[品項]_匯入用_v[N].xlsx`、`[品項]_匯入用_v[N]_[備註].xlsx`（備註標示比對鍵邏輯）、`[品項]_合成_v[N].xlsx`（標示合成/虛構資料）。

**待確認**：是否統一收斂成 `[企業代號]_[模組]_匯入用_v[N].xlsx`。目前 Demo 案例尚未套用企業代號前綴；正式客戶專案是否需要，待第一個正式案例確認（呼應 CLAUDE.md 第 12 節：正式交付文件檔名須含企業代號）。

---

## 5. 常見匯入眉角（觀察自 Demo 案例）

| 眉角 | 說明 |
|---|---|
| 兩列標題陷阱 | 來源資料若有「第1列中文說明＋第2列英文技術名稱」雙標題列，Odoo 只跳過第1列，第2列會被誤匯入，匯入前須先刪除第2列 |
| 模型須分開匯入 | 不能把整個 Excel 檔案一次丟給 Odoo，每個模型要各自匯入 |
| 表頭/明細用外部 ID 串接 | 主從結構（如報價單頭/身）要靠 External ID 把明細掛回正確表頭 |
| 比對鍵選擇原則 | 「內部參考」不能當更新匯入的比對鍵（會誤判為新記錄）；匯出產生的暫時性外部 ID（`__export__.xxx_hash`）當比對鍵可能觸發唯一鍵衝突；需要用資料庫 ID 比對批次更新時，優先用 XML-RPC/API 直接寫入 |
| 標籤欄位格式 | 若標籤有父層/子層結構，匯入時只填子標籤名稱本身，不要填「父層/子層」完整路徑 |
| 一次到位原則 | 匯入新一批聯絡人類資料時，同一次匯入就規劃好標準欄位（地址、幣別/價格表、付款條件），避免事後逐項補 |
| **公司在地化設定是靜默失敗地雷** | Odoo 沙盒剛建立時，`res.company` 若沿用安裝預設值（常見為美式地址/USD），系統完全不會報錯、一切照常運作，只是後續所有價格表/供應商報價都會用錯誤的幣別顯示——這種錯誤不會中斷流程，只會在事後被使用者發現時才知道整批資料要重查。**教訓來源**：經銷商業態 Demo 案例建置多週後才發現公司幣別從未設定過台灣/TWD，見 2026-07-27 的「系統基礎公司設定修正」交接紀錄 |
| **幣別/價格表變更不會自動連動既有紀錄** | 事後才變更 `res.company.currency_id`，不會讓已經寫入的 `res.partner.property_product_pricelist`、`product.supplierinfo.currency_id` 等既有欄位自動跟著改——這些是各自獨立儲存的欄位，需要逐筆重新查核，不能假設改了公司設定其他地方就會連動更新 |

---

## 6. 與其他文件的關聯

- 練習場域完整 SOP 紀錄：`艾創點數位-ERP顧問/經銷商業態案例_去識別化Demo環境建置/02_Demo環境建置紀錄/Odoo資料匯入SOP.md`
- 學習知識庫（功能面）：`skills/01_技術開發/odoo-learning-pipeline/SKILL.md`（負責逐字稿學習與知識沉澱，定位是「怎麼學會功能」；本文件是「怎麼把資料搬進去」）
- 專案歸檔結構：`00_共用規則與知識庫/01_工作區規則/專案資料夾結構與歸檔規則.md`（第 9 節「140_轉檔匯入範本」）
- 範例模組骨架：`艾創點數位-ERP顧問/00_專案資料夾範本/100_專案執行與交付/140_轉檔匯入範本/01_聯絡人主檔/`

---

## 7. 模組資料夾與 Excel 範本設計規則（✅ 核心規則，取代逐案重新調查）

**7.1 為什麼寫死成規則**：關聯欄位的匯入機制（External ID、Many2one/Many2many/One2many 寫法）是 Odoo 的系統機制，不會因專案而變；會變的只有「這個客戶用到哪些模組」。機制寫死在本節，AI 提示詞（第 9 節）只用來展開「因專案而異」的完整欄位清單。

**7.2 資料夾結構**：

```
[OO模組]/                          <- 例：01_聯絡人主檔、02_產品分類、03_產品主檔
├── 00_轉檔工作流.md               <- 本模組相依哪些前置模組、欄位對應表、匯入後檢查方式
└── 01_資料名稱.xlsx               <- 匯入用 Excel（見 7.3 分頁結構）
```

編號規則：2位數字＝匯入順序，依 3.1 節通則排定（被參照方在前），一旦排定不任意打亂，新增模組用同一序列往後接。

**7.3 Excel 內部分頁結構**：Sheet 1（主匯入表）列出該模組所有欄位，標題統一寫成「中文欄位名（Odoo欄位技術名稱 或 關聯欄位/External ID路徑）」，第一欄固定為 External ID。Sheet 2 以後（關聯查找表）僅用於不需獨立成模組的固定代碼對照表（如國家代碼）——**若關聯欄位指向的資料本身也要匯入 Odoo（如產品分類、標籤），必須獨立成自己的模組資料夾，不可只當附屬分頁**。

**7.4 External ID 設計規則（✅ 官方文件依據）**：關聯欄位三種寫法擇一——直接填名稱（`Country: Belgium`，適合手動整理的 CSV）、`欄位/Database ID`（很少用，開發者專用）、`欄位/External ID`（`Country/External ID: base.be`，官方建議「從第三方應用程式匯入資料時使用」）。**本規範採用 External ID 寫法**，命名建議 `[企業代號]_[模組代號]_[流水號]`，例如 `KD_partner_JD1001`。**待確認**：企業代號前綴確切格式，待第一個正式案例定案。

**7.5 Many2one / Many2many / One2many 寫法（✅ 官方文件原文確認）**：Many2one 欄位標題寫 `欄位名稱/External ID`；Many2many 同格逗號分隔、值間不能有空格（如 `Manufacturer,Retailer`）；One2many（表頭+明細）可用「同張 Sheet、明細列表頭欄位留空」或「兩階段匯入（先匯表頭拿 External ID，明細用 `表頭欄位/External ID` 參照）」，兩種官方文件都支援，依資料來源結構選擇。

**7.6 為什麼堅持保留 External ID 欄位（✅ 官方文件依據）**：保留此欄位可讓同一份檔案重複匯入而不產生重複記錄（"records that have already been imported are modified, instead of being created"），這是轉檔工作流常需分批多次匯入同一資料修訂版的必要條件。

**7.7 Selection（下拉選單）欄位技術鍵值查詢方法**：⚠️ NotebookLM 整理，未逐字核對 Odoo 19 實際畫面用詞。標準路徑：開發者模式 → 設定 App「技術」→「資料庫結構」→「欄位」，用模型＋欄位名稱過濾，欄位詳細畫面的「選項 (Selection Options)」清單左欄為技術鍵值、右欄為顯示標籤。進階捷徑：開發者模式下打開該欄位所在畫面，用 Debug Menu「檢視欄位」，滑鼠停在下拉選單上會跳出 `Selection: [('key1','顯示名稱1'), ...]` 提示框。

---

## 8. 核心模組關聯欄位對照表

**8.1 聯絡人主檔（res.partner）** ✅ GitHub 原始碼查證 — 對應資料夾如 `01_聯絡人主檔`

**Sheet1 基本欄位不可省略 email／phone**：即使匯入範本骨架的初版只列了關聯欄位，`name`／`email`／`phone` 這種最基本的聯絡資訊也要一起放進 Sheet1，不要只顧著設計關聯欄位而漏掉基本欄位——這是本規範自己在採購模組實測時犯過的錯（供應商草稿當初只設計了國家/標籤/付款條件，漏了email/phone，事後才補），已回頭修正 `140_轉檔匯入範本/01_聯絡人主檔` 骨架。

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `parent_id` | M2O | `res.partner` | 上層公司；匯入客戶底下的送貨地址/子聯絡人時要參照 |
| `country_id` | M2O | `res.country` | 國家 |
| `state_id` | M2O | `res.country.state` | 省/州 |
| `category_id` | M2M | `res.partner.category` | 聯絡人標籤，標籤本身須獨立成模組 |
| `industry_id` | M2O | `res.partner.industry` | 產業別 |
| `company_id` | M2O | `res.company` | 所屬公司（多公司架構才需要） |
| `user_id` | M2O | `res.users` | 業務員 |
| `bank_ids` | O2M | `res.partner.bank` | 銀行帳戶，需獨立匯入 |
| `property_payment_term_id` / `property_supplier_payment_term_id` | M2O | `account.payment.term` | 客戶/供應商付款條件——已透過 `account/models/partner.py` 查證，裝了會計模組才會出現；若要一次到位填寫（見第5節「一次到位原則」），付款條件須先於本模組匯入 |
| （待查證）供應商幣別 | 未知 | `res.currency`（推測） | ⚠️ 2026-07-27 實測發現 Odoo 表單「銷售與採購」頁籤有一個「供應商幣別」欄位，尚未查證其實際技術欄位名稱（推測可能是 `property_purchase_currency_id`，**未經原始碼確認，不可直接採用**）、也不確定跟 `product.supplierinfo.currency_id`（見8.5節）是否為同一機制或各自獨立。待終端機查證後回填此列 |

**8.2 產品分類（product.category）** ✅ GitHub 原始碼查證 — 對應資料夾如 `02_產品分類`

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `parent_id` | M2O | `product.category`（自己） | 上層分類，建立分類樹 |
| `property_account_income_categ_id` | M2O | `account.account` | 收入科目——已透過 `account/models/product.py` 查證，只有裝了會計模組才會出現，是產品分類綁定會計科目的實際欄位 |
| `property_account_expense_categ_id` | M2O | `account.account` | 費用科目，同上 |

產品分類只依賴自己（樹狀結構）與會計科目（若裝會計模組），是起手模組中依賴最少的一個，應排在產品主檔之前。

**8.3 產品主檔（product.template）** ✅ GitHub 原始碼查證 — 對應資料夾如 `03_產品主檔`

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `categ_id` | M2O | `product.category` | 產品分類——依賴 8.2 |
| `uom_id` / `uom_ids` | M2O / M2M | `uom.uom` | 銷售單位／額外包裝單位 |
| `company_id` | M2O | `res.company` | 所屬公司 |
| `seller_ids` | O2M | `product.supplierinfo` | 供應商資訊，依賴供應商（res.partner）先匯入 |
| `attribute_line_ids` | O2M | `product.template.attribute.line` | 產品屬性（變體用）——若產品有尺寸/顏色等變體，`product.attribute` / `product.attribute.value` 須先於本模組匯入，才有值可對照 |
| `product_tag_ids` | M2M | `product.tag` | 產品標籤——**product.tag 沒有父層/子層結構**（已於 Demo 案例實測驗證） |
| `taxes_id` / `supplier_taxes_id` | M2M | `account.tax` | 銷售稅／採購稅（裝會計模組才有） |
| `property_account_income_id` / `property_account_expense_id` | M2O | `account.account` | 產品層級科目，留空則用 8.2 分類層級的科目 |

**8.3a 物料清單 BOM（mrp.bom）** ✅ GitHub 原始碼查證（`mrp/models/mrp_bom.py`）— 製造業/組合商品才需要，對應資料夾如 `13_物料清單`

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `product_tmpl_id` | M2O | `product.template` | 對應的產品——依賴 8.3，必須先匯完產品主檔 |
| `product_id` | M2O | `product.product` | 若只限定特定變體才需要，留空則整個產品範本共用此 BOM |
| `bom_line_ids` | O2M | `mrp.bom.line` | 組成用料明細，`mrp.bom.line.product_id`（M2O→`product.product`）為明細的元件產品，同樣依賴 8.3 |
| `picking_type_id` | M2O | `stock.picking.type` | 限定作業類型才需要，選填 |
| `type` | Selection | — | `normal`＝製造、`phantom`＝套件式 Kit（呼應 Demo 案例「BoM Kit」踩坑紀錄） |

BOM 必須在產品主檔（8.3）建完之後、期初庫存（8.6）導入之前建立，否則庫存成本結構會不完整。

**8.4 銷售訂單／報價單（sale.order）** ✅ GitHub 原始碼查證 — 對應資料夾如 `04_報價單` / `05_訂單`

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `partner_id` | M2O | `res.partner` | 客戶——依賴 8.1 |
| `partner_invoice_id` / `partner_shipping_id` | M2O | `res.partner` | 請款/送貨地址 |
| `pricelist_id` | M2O | `product.pricelist` | 價格表 |
| `payment_term_id` | M2O | `account.payment.term` | 付款條件 |
| `user_id` | M2O | `res.users` | 業務員 |
| `team_id` | M2O | `crm.team` | 業務團隊 |
| `order_line` | O2M | `sale.order.line` | 訂單明細——依賴 8.3，典型表頭+明細結構（見 7.5） |

**8.5 採購訂單（purchase.order）** ✅ GitHub 原始碼查證，並修正 NotebookLM 版本兩處欄位技術名稱錯誤 — 對應資料夾如 `14A_採購單`

| 欄位 | 類型 | 目標模型 | 說明 |
|---|---|---|---|
| `partner_id` | M2O | `res.partner` | 供應商 |
| `payment_term_id` | M2O | `account.payment.term` | 付款條件 |
| `company_id` | M2O | `res.company` | 所屬公司 |
| `order_line` | O2M | `purchase.order.line` | 明細行 |
| `order_line/product_id` | O2M→M2O | `product.product` | 明細行產品 |
| `order_line/product_uom_id` | O2M→M2O | `uom.uom` | 明細行單位——⚠️ **修正**：NotebookLM 版本寫成 `product_uom`，實際欄位名稱是 `product_uom_id` |
| `order_line/tax_ids` | O2M→M2M | `account.tax` | 明細行稅別——⚠️ **修正**：NotebookLM 版本寫成 `taxes_id`，實際欄位名稱是 `tax_ids` |

**重要澄清**：`picking_type_id` **不是** base `purchase.order` 模型的欄位——查證 `addons/purchase/models/purchase_order.py` 並未找到此欄位，它是由 `purchase_stock`（採購+庫存整合模組）另外加上去的，只有該模組有裝才會出現。若客戶環境沒裝庫存整合，這個欄位就不存在，匯入時強行對應會找不到欄位。

**8.6 庫存單據（stock.picking / stock.quant）** — 對應資料夾如 `15_期初庫存`

⚠️ NotebookLM 建議：期初庫存優先直接寫入 `stock.quant`（庫存盤點），而非匯入完整的 `stock.picking` 單據；後者通常由採購/銷售自動產生，只有「補歷史未結單據」才需要。`stock.quant` 關聯欄位已 ✅ 用官方原始碼查證：`product_id`（M2O→`product.product`）、`location_id`（M2O→`stock.location`）、`lot_id`（M2O→`stock.lot`，批次序號才需要）、`owner_id`（M2O→`res.partner`，寄售情境才需要）。

`stock.picking` 主單欄位已 ✅ 用 `addons/stock/models/stock_picking.py` 查證：`picking_type_id`（M2O→`stock.picking.type`，極重要必填）、`location_id`／`location_dest_id`（M2O→`stock.location`）、`partner_id`（M2O→`res.partner`）。**修正**：明細行的正確欄位是 `move_ids`（O2M→`stock.move`）；NotebookLM 版本提到的 `move_ids_without_package` 在 Odoo 19 base `stock.picking` 原始碼中查無此欄位（可能是舊版本欄位名稱或表單視圖專用的介面欄位，非資料模型本身的欄位），**匯入時請改用 `move_ids`，並在匯出比對法驗證時特別留意此處**。

**8.7 會計分錄／發票（account.move）** ✅ GitHub 原始碼查證（`addons/account/models/account_move.py`）— 對應資料夾如 `16_期初應收應付`

Odoo 19 客戶發票、供應商帳單、一般分錄統一歸在 `account.move`，用 `move_type`（Selection，如 `out_invoice`/`in_invoice`/`entry`）區分。關鍵欄位：`journal_id`（M2O→`account.journal`，極重要必填）、`partner_id`（M2O→`res.partner`）、`currency_id`（M2O→`res.currency`）、`invoice_line_ids`（O2M→`account.move.line`，原始碼註記「只是 `line_ids` 的子集」，若要處理非發票的一般分錄明細須改用 `line_ids`）。`invoice_line_ids/account_id`（M2O→`account.account`，極重要必填，若沒給產品系統無法自動代入科目會報錯）此欄位為一般 Odoo 慣例，本次未逐一開啟 `account_move_line.py` 覆核，信心度較 `account.move` 主體欄位略低。**匯入時建議狀態留在「草稿」，確認借貸平衡且與舊系統報表一致後，再於系統內批次過帳**（此為實務建議，非官方文件逐字依據）。

**8.8 全局 ERP 起手模組匯入順序（整合 8.1～8.7，取代 3.2 節個案順序）**

依 3.1 節通則＋以上關聯結構，完整參考順序：

1. `01_公司與使用者`（`res.company` / `res.users`）——⚠️ **這一步是關卡，不是清單裡普通一項**：Odoo 沙盒剛建立時預設值（常見美式地址/USD）不會報任何錯，一切照常運作，只有等到後續資料都建完才會發現幣別/地區全部跑掉，屆時要逐筆回頭修正。**任何新專案／新沙盒，動手匯入任何資料之前，第一件事一定是先手動檢查並確認 `res.company` 的國家與幣別已經正確設定**，不能用「反正之後會發現」的心態跳過（教訓來源：見第5節「公司在地化設定是靜默失敗地雷」）
2. `02_會計科目表`（`account.account`）
3. `03_稅別設定`（`account.tax`）
4. `04_日記帳`（`account.journal`）
5. `05_付款條件`（`account.payment.term`）——✅ 已查證聯絡人（8.1）與銷售訂單（8.4）都會參照此模型，須排在兩者之前
6. `06_庫存位置與倉庫`（`stock.location`）
7. `07_作業類型`（`stock.picking.type`）
8. `08_聯絡人主檔`（`res.partner`，對應 8.1；含聯絡人標籤 `res.partner.category`）
9. `09_計量單位`（`uom.uom`）
10. `10_產品分類`（`product.category`，對應 8.2）
11. `11_產品屬性與變體`（`product.attribute` / `product.attribute.value`）——僅產品有尺寸/顏色等變體時需要，否則跳過
12. `12_產品主檔`（`product.template`，對應 8.3）
13. `13_物料清單 BOM`（對應 8.3a）——僅製造業/組合商品需要，否則跳過
14. `14A_採購訂單` / `14B_銷售訂單`（對應 8.5 / 8.4，只匯 Open 狀態）
15. `15_期初庫存`（對應 8.6，優先用 `stock.quant`）
16. `16_會計期初餘額與未結憑證`（對應 8.7，先草稿後過帳）

**編號使用原則**：以上是**理論上的完整參考順序**，不是每個專案都要照抄全部 16 步——例如不做製造業就跳過第13步，不需要多幣別/多稅別就簡化第2~5步。**實際專案的 `140_轉檔匯入範本` 資料夾請依「這個專案實際用到哪些模組」重新連續編號（01, 02, 03…），不要因為跳過某步就留空號或照抄本節的絕對數字**——本節數字只用來表達「誰在誰前面」的相對順序，不是強制的資料夾編號。

**待確認**：此順序尚未有任何專案完整跑過全部 16 步，待第一個正式案例套用後回頭驗證是否有理論與實務落差。

---

## 9. AI 產出「特定模組完整欄位清單」的兩步驟提示詞

機制本身（第 7、8 節）已寫死，不需每次問 AI；以下只用於「這個專案要匯的某模組，實際完整欄位清單長怎樣」。

**步驟一（排順序）**：「你是資深 Odoo 19 導入顧問，我準備導入的模組包含【依專案填入】。請列出絕對正確的資料匯入順序，用兩位數編號排序，標示對應模組與 Model，並說明每個主檔依賴哪些前置資料。」

**步驟二（展開欄位）**：「請針對『【步驟一拿到的模組，如 10_產品主檔 (product.template)】』設計 Excel 匯入結構：(1) 第一欄固定 External ID；(2) 主分頁表格列出中文欄位名／Odoo技術名稱／型態／是否必填／範例值；(3) 分析 Many2one/Many2many 欄位，列出需要哪些參照分頁，並註明哪些關聯資料本身要獨立成模組（依 7.3 節原則判斷）。」

兩步驟產出結果**必須經第 10 節匯出比對法驗證後才能定案**。

---

## 10. 匯出範本比對驗證法（✅ 定案前必要步驟，非選配）

依官方文件建議："Another useful way to find out the proper column names to import is to export a sample file using the fields to be imported."

1. 測試資料庫手動建一筆該模組最完整的資料，欄位填滿。
2. 選取該筆記錄 → Action → Export → 勾選「I want to update data (import-compatible export)」→ 匯出 Excel（此選項只顯示可匯入欄位，並自動帶 External ID）。
3. 拿系統原生範本對照第 9 節 AI 生成的欄位清單，找出兩邊落差。
4. 以系統原生範本為準修正，才正式定案為 Sheet 1 結構。

**為什麼不能省略**：AI 生成清單可能與客戶實際 Odoo 版本/客製模組有落差（欄位改名、停用、新增），系統原生匯出範本才是當下資料庫的真實結構。

---

## 11. 演進紀錄

| 日期 | 版本 | 異動內容 |
|---|---|---|
| 2026-07-27 | v0.1~v0.4 | 建立空殼框架 → 補齊模組資料夾/Excel設計規則與 res.partner/product.category/product.template/sale.order 關聯欄位表（GitHub查證）→ NotebookLM補齊 Selection查詢法與採購/庫存/會計三模組 → 修正3.2個案順序標示為「不建議援用」 |
| 2026-07-27 | v0.5 | 修正章節編號缺漏（原缺第7節）；精簡重複內容（3.2個案細節、9.5~9.7重複的來源警語合併）；新增 8.2/8.3 產品分類與產品主檔的會計科目關聯欄位（`account/models/product.py` 查證）；新增 8.6 `stock.quant`（官方原始碼查證，用於期初庫存優先於 `stock.picking`）；8.8 全局順序改為 NotebookLM 提供的 13 步驟版本，取代原 6 層版本 |
| 2026-07-27 | v0.6 | 用官方原始碼查證新增 `res.partner.property_payment_term_id`（8.1）與 `mrp.bom`/`mrp.bom.line`（新增 8.3a，皆依賴 product.template）；8.8 全局順序依 NotebookLM 建議擴充為 16 步（新增付款條件、產品屬性/變體、BOM、銷售訂單獨立列出）；新增「編號使用原則」，明訂 8.8 數字僅表達相對順序，實際專案 `140_轉檔匯入範本` 資料夾應依實際模組連續編號，不強制照抄 |
| 2026-07-27 | v0.7 | 用官方原始碼（`purchase_order.py`／`purchase_order_line.py`／`stock_picking.py`／`account_move.py`）逐一覆核 8.5~8.7，找出並修正 NotebookLM 版本三處錯誤：purchase.order 明細行欄位應為 `tax_ids`（非 `taxes_id`）與 `product_uom_id`（非 `product_uom`）；`picking_type_id` 不是 base purchase.order 欄位，須裝 purchase_stock 模組才有；stock.picking 明細行正確欄位是 `move_ids`，`move_ids_without_package` 在 Odoo 19 base 原始碼查無此欄位 |
| 2026-07-27 | v0.8 | 納入採購模組實測回饋（經銷商業態Demo案例第0週執行）：① 8.8 全局順序 Step 1（`res.company`公司在地化）由普通清單項升級為明確「關卡」，明訂任何新專案動手匯入資料前必須先手動檢查國家/幣別設定，避免靜默失敗；② 第5節新增兩列：「公司在地化設定是靜默失敗地雷」與「幣別/價格表變更不會自動連動既有紀錄」；③ 8.1 res.partner 表新增自我檢討警語：Sheet1基本欄位（`email`／`phone`）不可只列關聯欄位而省略，此為規範自己在採購模組實測時犯過的錯；④ 8.1 新增一列「（待查證）供應商幣別」欄位，標示技術名稱未經原始碼確認、僅為推測，不可直接採用 |

---

*本文件為草稿，內容會隨經銷商業態 Demo 專案的實際執行與後續案例逐步補齊。若段落標示「待確認」或「⚠️」，代表尚無足夠依據，不得自行假設補寫。*
