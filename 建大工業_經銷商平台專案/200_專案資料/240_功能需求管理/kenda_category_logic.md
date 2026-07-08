# 建大經銷商平台 — 類別邏輯說明

> 文件位置：200_專案資料/240_功能需求管理/kenda_category_logic.md
> 最後更新：2026-07-08（新增第六節資料更新流程 Runbook）
> 狀態：已與建大確認（2026-07-07 會議）；①②③本機+遠端 aiuptop.com 全部部署並驗證完成（2026-07-08）
> 環境連線資訊請見：300_連線方式/建大工業_對應環境連線資訊.md

---

## 一、兩個獨立分類維度

系統中存在**兩套互相獨立**的分類，不可混用：

| 維度 | 代碼集合 | 儲存位置 | 用途 |
|------|----------|----------|------|
| **客戶分類** | BC / MC / AC / OTHER | 經銷商主檔 `dealer.categories` | 標記經銷商類型，用於 badge 顯示、banner 圖片選擇 |
| **產品細分類** | B1/B2/M1/M2/I1/I2/A1/A2/R1/OB/EB/EM/EV/OTHER | 產品主檔 `product.category` | 標記產品所屬細項類別 |

---

## 二、客戶分類（現行標準）

| 代碼 | 說明 |
|------|------|
| BC | 自行車（Bicycle）經銷商 |
| MC | 摩托車（Motorcycle）經銷商 |
| AC | 汽車（Automobile）經銷商 |
| OTHER | 不固定，多種產品都可能採購 |

---

## 三、產品細分類對照表

| 客戶分類（參考）| 產品細分類代碼 | 說明 |
|---|---|---|
| BC | B1 | 自行車胎（一般）|
| BC | B2 | 自行車胎（其他子類）|
| BC | OB | 襯帶 |
| BC | EB | 電動自行車胎 |
| MC | M1 | 摩托車胎（一般）|
| MC | M2 | 摩托車胎（其他子類）|
| MC | I1 | 工業外胎 ★ |
| MC | I2 | 工業內胎 ★ |
| MC | EM | 電動摩托車胎 |
| AC | R1 | 子午線胎 |
| AC | A1 | 汽車胎（一般）|
| AC | A2 | 汽車胎（其他子類）|
| AC | I1 | 工業外胎 ★ |
| AC | I2 | 工業內胎 ★ |
| AC | EV | 電動汽車胎 |
| OTHER | OTHER | 不固定 |

> ★ **I1 / I2 同時屬於 MC 和 AC**：MC 與 AC 類型的經銷商都可以銷售工業胎，這是業務上的多對多關係，非資料錯誤。
> 客戶分類欄（左欄）僅供參考，兩個維度互相獨立。
> **2026-07-08 補充**：整張對照表都是「某類客戶通常會買哪些產品細分類」的參考關係，不是硬性綁定——不只 I1/I2，全部列都適用。Badge 分兩套獨立設計：客戶 badge 看客戶主檔的客戶類別欄位（顯示 BC/MC/AC/OTHER）；產品 badge 看產品主檔的細分類代碼（顯示 B1/M1/R1...等）。ER 圖確認：建大系統的「客戶主檔」有自己的 `prodcutType` 欄位（客戶分類來源），跟「各公司報價產品主檔」的 `productType` 欄位（產品分類來源）是完全不同的表、不同的欄位，資料庫結構上就是分開的。

---

## 四、版本歷史

| 版本 | 代碼集合 | 狀態 |
|------|----------|------|
| 版本1 | BC / MC / PCR / IC | ❌ 已廢棄，請勿使用 |
| 版本2 | BC / MC / AC / OTHER | ✅ 現行（客戶分類）|
| 版本3 | B1/B2/M1/M2/I1/I2/A1/A2/R1/OB/EB/EM/EV/OTHER | ✅ 現行（產品細分類）|

版本1 → 版本2 的變化：PCR 改名為 AC；IC（工業用）不再作為客戶分類，改為產品細分類 I1/I2。

---

## 五、程式碼殘留待處理

### ① 前端 BMAP 缺 OTHER key（高優先，有畫面影響）—— ✅ 本機+遠端皆已修復並驗證（2026-07-08）
- 檔案：`stack/web/html/assets/index-BnEs5qT0.v14.js`（原 v12→v13→v14，因 `/assets/` immutable cache 規則每次改動都要換新檔名，`index.html` 已改指向 v14）
- 修法：確認本機 `kenda_product_category` 主檔與經銷商關聯表只剩 `AC/BC/MC/OTHER` 四碼（無 PCR/IC/RADIAL 殘留）後，採「乾淨修法」——`BMAP` 整組改成 `{"BC":"/img/banner-bc.jpg","MC":"/img/banner-mc.jpg","AC":"/img/banner-default.jpg","OTHER":"/img/banner-default.jpg"}`，移除已廢棄的 `PCR`/`IC`/`RADIAL` key
- OTHER banner 圖：沿用 `banner-default.jpg`（跟 AC 共用公司介紹圖，比照舊版 IC/RADIAL 的處理方式）
- 本機驗證：nginx 已吐出新 BMAP、瀏覽器截圖確認 banner 正常顯示、console 無 app 端錯誤（僅有瀏覽器擴充功能自身雜訊，與此無關）
- **✅ 遠端 aiuptop.com 已部署並驗證（2026-07-08）**：確認遠端 v13.js 與本機修復前的 v12.js 位元組完全相同（md5一致），故直接拿本機修好的 v14.js 內容部署到遠端、檔名同步命名為 `index-BnEs5qT0.v14.js`，`index.html` 改指向 v14。用 OTHER 分類客戶帳號 R02166 登入 `https://kenda_demo_web.aiuptop.com/shop` 實測，banner 正常顯示 `banner-default.jpg`、無破圖、console 無 app 端錯誤。

### ② 匯入來源修正：改用「✨各公司報價產品主檔」—— ✅ 本機已完成（2026-07-08）

**已跟建大確認**：「集團產品主檔」之後不會再用，「✨各公司報價產品主檔」是唯一/最終產品主檔來源。621 筆公司別對不齊問題已請使用者暫緩處理，先擱置不深挖（Excel 清單見下方）。

**根因**：`kenda-local\import-data\upsert_import.py` 的產品匯入迴圈原本讀 `rows('產品主檔')`——這個分頁名稱在目前 Excel 匯出檔裡**已不存在**（`m.get()` 找不到會靜默回傳空陣列，迴圈整個不執行），欄位索引也是舊版 13 欄排法、分類值檢查用已廢棄的 `('BC','MC','PCR','IC')`。也就是說這隻 script 早已完全沒有在更新 `kenda.product`，連帶報價單身寫入時 `product_id` 全部落空。

**修法**：把 Prod 迴圈改成讀 `rows('✨各公司報價產品主檔')`（14 欄，見下方「資料更新流程」的欄位對照），`category` 直接存 productType 原始代碼（不做白名單過濾，因為 `kenda_product.py` 的 `category` 欄位本來就是 Char 不是 Selection，見該檔案 15-18 行註解）。

**驗證結果**（2026-07-08，本機 `kenda_demo` DB）：`product 更新 2695 / 新增 0`，商品總數 2921→2998（未刪除任何記錄，non-destructive upsert）。`category` 分佈已出現新版代碼（R1 559、B1 551、M1 451、B2 288、I1 203、A1 148、OB 57、EB 31、EM 17、M2 5、I2 2、OTHER 6），`None`（無分類）482 筆——這對應「✨各公司報價產品主檔」本身就缺分類、或該商品不在此表裡的情況，不是匯入 bug。

**✅ 舊代碼殘留已清除（2026-07-08，本機+遠端）**：DB 裡曾有 198 筆產品的 `category` 停留在已廢棄的版本1代碼——`PCR`107 / `BC`45 / `MC`28 / `IC`18。這些是更早期（`category` 還是 Selection、用 `('BC','MC','PCR','IC')` 白名單時）匯入殘留的髒資料，其 product_code 不在目前「✨各公司報價產品主檔」裡，所以匯入來源修正的那次 upsert 沒有覆蓋到它們。跟前面 621 筆公司別對不齊是不同問題（那個是「查得到但沒匯入」，這個是「已匯入但值是舊代碼」）。已在 odoo shell 用 `env['kenda.product'].sudo().search([('category','in',['PCR','BC','MC','IC'])]).write({'category': False})` 清成 NULL（未分類），不硬湊新代碼。清完後 `category` 分佈：`None`（未分類）680 筆（= 原本 482 缺分類 + 這次清掉的 198）、其餘全是新版代碼（R1 559/B1 551/M1 451/B2 288/I1 203/A1 148/OB 57/EB 31/EM 17/M2 5/I2 2/OTHER 6），DB 裡已無任何版本1殘留代碼。

**✅ 遠端 aiuptop.com 已部署並驗證（2026-07-08）**：查證發現遠端 `kenda_product.py` 的 `category` 欄位還停留在**更舊的 schema**——是 `Selection`，選項只有 `CATEGORY_SEL = [('BC',...),('MC',...),('PCR',...),('IC',...)]` 四個版本1代碼，連 B1/M1 這些新代碼都不支援（Odoo 的 `fit()` 過濾機制會靜默把不在選項清單裡的值濾掉）。遠端 DB 當時的分類分佈剛好也是 `PCR 107/BC 45/MC 28/IC 18/None 2801`（跟本機清理前殘留的198筆數字完全一樣），代表遠端從沒真正跑過新版分類邏輯。

部署步驟：① SFTP 同步 `kenda_product.py`（Selection→Char，與本機一致）+ `kenda_dealer.py`（死碼清理）+ `security/ir.model.access.csv` 到 `/odoo/custom/addons/kenda_platform/`（各自先備份成 `.bak_20260708`）② 跑 `sudo -u odoo /odoo/odoo-server/odoo-bin -c /etc/odoo-server.conf -d kenda_demo -u kenda_platform --stop-after-init` 升級模組（log 確認 `Module kenda_platform loaded in 0.57s` 無錯誤）③ `systemctl restart odoo-server` ④ 上傳修好的 `upsert_import.py` + 本機轉出的最新 `excel_data_new.json` 到遠端 `/tmp/`，透過 `odoo-bin shell --no-http` 執行 `exec(open('/tmp/upsert_import.py').read())`——結果與本機一致（`product 更新 2695`）⑤ 清除遠端殘留的198筆舊代碼（同本機做法）。

驗證：遠端分類分佈與本機一致（`None 681/R1 559/B1 551/M1 451/B2 288/I1 203/A1 148/OB 57/EB 31/EM 17/M2 5/I2 2/OTHER 6`）；瀏覽器登入 `https://kenda_demo_web.aiuptop.com/shop` 確認商品卡片正確顯示 I1/A1 等新版分類徽章。

### ②b catalog.py fallback 仍用版本1邏輯（中優先，資料不乾淨）—— 🔍 已找到根本原因，待建大確認子問題
- 檔案：`stack/odoo/addons/kenda_platform/controllers/catalog.py`（行 15-30, 82）
- 問題：category 為空的商品在 `/quotes` API 用舊推斷法吐出 BC/PCR/MC；在 `/products`（商品總覽）則直接從列表消失（不只是分類徽章問題）
- **2026-07-08 完整根因（來源：與建大林柏豪對話確認）**：
  1. `產品類別`(productType) 這個欄位**建大自己的 ERP 完全沒有**，是專為這次下單平台專案臨時請業務人工補的新資訊
  2. 「✨各公司報價產品主檔」（現行分類資料唯一來源）的生成方式：取〔報價單身〕依 公司別+成代 DISTINCT 後 LEFT JOIN〔集團產品主檔〕，再由業務手動補 產品類別/產品系列/包裝部門代號 這3欄——**這張表本來就只涵蓋「曾出現在報價單裡」的成代**
  3. 林柏豪明確表示：目前提供的「各公司報價產品主檔」**是拿測試階段用的報價單反推出來的子集，不是正式完整的產品分類清單**
  4. 精確比對兩張表（`集團產品主檔` 2921筆 vs `✨各公司報價產品主檔` 2318筆）：缺口 **603 筆**，全數已匯入本機平台（`kenda_product` 表 0 筆漏匯），且缺口不限舊資料——含 2025-11-28、2026-02-09 才維護過的商品
  5. **結論：不是資料錯誤/匯入 bug，是建大的分類工作本身還沒做到全量**
- **待建大確認的子問題（2026-07-08 已提出，尚未回覆）**：目前提供的〔報價單身〕涵蓋到的成代，是否都已經在「各公司報價產品主檔」對應到分類資料？（也就是「至少測試用的報價單商品分類有沒有補齊」，跟「全量2921筆何時補齊」是兩個獨立問題）
- **下一步（等建大回覆子問題後再做）**：跟建大確認這 603 筆商品是否要開放給經銷商訂購——要開放就請業務補分類，不開放就維持現況隱藏；`_derive_category` 舊推斷 fallback 建議屆時直接移除（改顯示「未分類」而非硬湊 BC/PCR/MC），程式碼尚未變動

**2026-07-08 深入排查與架構性結論：**
- 用「報價單身」（實際報價紀錄，2710組不重複〔公司別,成代〕）比對「✨各公司報價產品主檔」（2423組），找到 **621 組缺分類**。細拆後：**15組是真的完全沒有分類資料，606組其實資料存在，只是「公司別」欄位跟報價單身對不上**（例：Y0000478，報價單身寫公司別F，但各公司報價產品主檔登記在公司別1）。範例與完整清單已產出 Excel：`200_專案資料\230_內部專案檔案\0708_0625下單平台資料交換-問題成代排查.xlsx`（分頁「完全無分類_15筆」「公司別對不齊_606筆」）
- **621筆已暫緩處理**，先擱置不深挖
- **更根本的架構問題（尚未拍板，需先跟建大確認）**：林柏豪明確表示「集團產品主檔」以後應該不會再用，「各公司報價產品主檔」才是最終產品主檔。但**本機平台目前的匯入邏輯（`kenda-local\import-data\convert_new.py`）是拿「集團產品主檔」當基礎在匯商品**——這正是 603 筆商品被匯進平台卻沒分類的根本原因。若改成「以各公司報價產品主檔為匯入來源」：
  1. 那 603 筆商品會直接不匯入平台（但這些商品現在本來就因無分類而在商品總覽消失，對經銷商體驗幾乎無差別）
  2. 621 筆缺分類問題會**結構性消失**（各公司報價產品主檔裡的每一筆本來就都有 productType）
- **✅ 2026-07-08 已跟建大確認**：集團產品主檔目前應該用不到了，確定以「各公司報價產品主檔」為最終產品主檔
- **✅ 已完成（2026-07-08）**：見上方「② 匯入來源修正」小節，`upsert_import.py` 已改讀「✨各公司報價產品主檔」並驗證過

### ③ 死碼（低優先，統一清理）—— ✅ 本機+遠端皆已清除（2026-07-08）
- `kenda_dealer.py`（行 10-15）：`PRODUCT_CATEGORY_SEL` 含版本1代碼，無處引用 → 已從 `stack/odoo/addons/kenda_platform/models/kenda_dealer.py` 刪除，遠端同步部署（見②的部署步驟，跟 `kenda_product.py` 一起 SFTP+模組升級）
- 前端 `bd` 陣列：寫死的版本1篩選器，已無處渲染 → 已從 JS bundle 移除（連帶把版號從 v13 推到 v14，因為改動了已被瀏覽器抓取過的 v13 檔案內容，必須換新檔名避免 immutable cache 問題），遠端同步部署（見①）

---

## 六、資料更新流程（Runbook）— 建大給新的 Excel 之後怎麼重新匯入

目的：以後建大更新 `下單平台資料交換*.xlsx` 時，照這份步驟做就好，不用重新解釋分類邏輯或重新反推程式碼。

**唯一權威產品分類來源** = Excel 分頁 `✨各公司報價產品主檔`（14 欄，依序）：
`公司別(subCompany) / 成品代號(partNumber) / 產品類別(productType) / 產品系列(productKind) / 包裝部門代號(packingDeptCode) / 品名(productName) / 規格(productSpec) / 尺寸(tireSize) / 花紋(pattern) / 層數強度(plyRating) / TT-TL / TPI / 維護日期(updatedAt) / 維護人員(updateBy)`

`集團產品主檔` 分頁**不要用**（已跟建大確認之後不會再維護，且本來就沒有 category/series 欄位）。

**步驟**：
1. 確認新 Excel 檔案路徑，更新 `kenda-local\import-data\convert_new.py` 第 9 行 `SRC` 指向新檔（若檔名/路徑沒變則跳過）
2. 本機執行轉檔：`cd kenda-local\import-data && python convert_new.py`（重新產生 `excel_data_new.json`）
3. 複製進 Odoo 容器：
   ```
   docker cp kenda-local\import-data\excel_data_new.json stack-odoo-1:/tmp/excel_data_new.json
   docker cp kenda-local\import-data\upsert_import.py stack-odoo-1:/tmp/upsert_import.py
   ```
4. 在 odoo shell 執行 upsert（non-destructive，不會刪資料，安全可重跑）：
   ```
   printf "exec(open('/tmp/upsert_import.py').read())\nquit()\n" | docker exec -i stack-odoo-1 odoo shell -c /etc/odoo/odoo.conf -d kenda_demo --no-http
   ```
   （Git Bash 需要 `MSYS_NO_PATHCONV=1` 前綴，否則 `/etc/odoo/odoo.conf` 會被誤轉成 Windows 路徑）
5. 確認結尾印出的 `=== UPSERT 完成 ===` 統計數字合理（新增/更新筆數不應該是 0 除非真的沒異動）
6. 瀏覽器驗證 `http://localhost:8080` 商品總覽 / 客戶 banner 顯示正常

**如果未來 Excel 分頁改名或欄位順序又變了**：`upsert_import.py` 裡的 `rows('✨各公司報價產品主檔')` 呼叫和 `r[0]..r[13]` 索引要跟著改，比對方法是打開新 Excel 看該分頁第 0-1 列（英文代碼列），跟本文件開頭的欄位對照表逐一核對，不要用猜的。

**若要同步推到遠端 aiuptop.com**（觸及客戶正式站，動手前務必明確跟使用者確認）：
- 連線資訊見 `300_連線方式/建大工業_對應環境連線資訊.md`；SSH 密碼每次由使用者當場提供，不存檔案
- **先唯讀查證遠端現況再動手**——不要假設遠端跟本機同步。2026-07-08 這次就發現遠端 `kenda_product.py` 的 schema 比本機舊了一整個版本（Selection vs Char），照抄本機腳本會被 Odoo 靜默濾掉新代碼
- addon 檔案：SFTP 到 `/odoo/custom/addons/kenda_platform/`（先備份成 `.bak_<日期>`）→ `sudo -u odoo /odoo/odoo-server/odoo-bin -c /etc/odoo-server.conf -d kenda_demo -u kenda_platform --stop-after-init` → `systemctl restart odoo-server`
- 資料匯入：SFTP `upsert_import.py`+`excel_data_new.json` 到 `/tmp/` → `sudo -u odoo /odoo/odoo-server/odoo-bin shell -c /etc/odoo-server.conf -d kenda_demo --no-http` 餵 `exec(open('/tmp/upsert_import.py').read())`
- 前端 JS：先下載遠端現有 `index-BnEs5qT0.v<N>.js` 跟本機對應舊版本比對 md5，若一致才能直接拿本機修好的版本上傳（換新版號檔名，改 `index.html` 指向），不一致要先查清楚差異來源，不能盲目覆蓋
- 每步做完立即查驗（DB 分類分佈、瀏覽器實測），不要一次全推完才驗證
