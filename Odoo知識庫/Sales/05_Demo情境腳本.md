# Odoo Sales 模組 - Demo 情境腳本

> 版本標示：Odoo 17（待確認）
> 學習日期：2026-07-20
> 狀態：🔄 草稿
> 說明：以影片示範情境改寫為顧問向客戶展示用腳本，情境角色沿用影片（Stealthy Wood 傢俱公司等）

---

## Demo 1（章節 Quotations）：一條龍報價到收款
**情境**：業務為客戶製作客製傢俱報價，客戶線上簽名付款後完成出貨開票。
**操作路徑**：Sales → Orders → New → Confirm → Create Invoice → Delivery
**步驟**：
1. 設定啟用線上簽名/付款/運送、發票政策=依訂購開票。
2. New 報價 → 選客戶 → 設到期日 30 天、付款條件 Immediate Payment。
3. 加產品（crochet hat）→ Add shipping（standard delivery）。
4. Preview → 客戶端 Sign and Pay → Accept and Sign → Pay。
5. 回訂單看 chatter 出現付款連結 → Create Invoice → Confirm。
6. Delivery 智慧按鈕 → Validate。
**預期結果**：訂單一次完成「確認+開票+出貨+收款」，chatter 完整留痕。
**展示重點**：現金流優先情境、客戶自助簽名付款、內部單據與會計文件分離。

---

## Demo 2（章節 Quotations）：部分出貨與早付折扣
**情境**：批發乾草供應商庫存不足，需分批出貨並鼓勵客戶早付。
**操作路徑**：Sales → Orders → Quotations → New → Delivery → Create Invoice
**步驟**：
1. 發票政策=依交付開票。
2. 報價選客戶、付款條件 2/7 net 30、加產品（500 綑，庫存僅 400）。
3. Confirm → Delivery → Validate → Create Back Order。
4. Create Invoice（僅 400 綑）→ Confirm → Pay（2% 折扣自動套用，顯示省 $381.60）。
5. 補貨後處理 back order → Validate → 再開剩餘 100 綑發票。
**預期結果**：分批出貨零重複開票，早付折扣自動計算。
**展示重點**：交付數量不確定產業（易腐/散裝）、back order 管理。

---

## Demo 3（章節 Quotations）：報價範本 + 線上報價設計
**情境**：促銷組合（四人桌+4椅）建立範本並美化外觀線上寄送。
**操作路徑**：Sales → Configuration → Quotation Templates → New → Design Template
**步驟**：
1. 建範本：命名、有效 30 天、確認信、線上簽名+50% 付款、加產品與選配、條款。
2. Design Template → Website 建置器拖曳 Cover 區塊改文字/圖片 → Save。
3. New 報價選範本自動帶入 → Send by email。
4. Customer Preview → 客戶加選配椅、Sign and Pay → 付 50%。
**預期結果**：業務數秒完成專業報價，客戶線上確認付訂金。
**展示重點**：範本省時、無需寫程式的視覺化設計、選配追加銷售。

---

## Demo 4（章節 Quotations）：PDF Quote Builder 專業報價
**情境**：HVAC 安裝報價需附產品規格表與安裝指南 PDF。
**操作路徑**：Sales → Configuration → Headers and Footers / Quotation Templates
**步驟**：
1. 產品/變體 Documents 上傳 PDF，設 Inside quote PDF、Publish on website。
2. 範本 Quote Builder 加 header + footer。
3. New 報價套範本 → Quote Builder 選 header/product/footer → Send。
4. 開 chatter PDF 預覽含頁首、報價、安裝指南、關於我們。
**預期結果**：一份含動態欄位（客戶名/日期/單號）的精美 PDF。
**展示重點**：品牌一致性、標準化文件、產品文件亦可於網站下載。

---

## Demo 5（章節 Promotions）：折扣碼 + 優惠券 + 忠誠 + 禮品卡
**情境**：綜合展示四種促銷提升回購。
**操作路徑**：Sales → Products → Discounts and Loyalty / Gift Cards and eWallet
**步驟**：
1. 折扣碼：滿 $100 打 85 折，限用次數、網站購物車輸入碼。
2. 優惠券：買 2 件 8 折，Generate and Send 給指定客戶，自動 email。
3. 忠誠卡：特定產品加碼點數，100 點兌 10% 折扣，Reward 按鈕自動加折扣行。
4. 禮品卡：買 Alpine 桌送 $60 卡，Generate 後寄送，購物車套用。
**預期結果**：四種促銷各自運作，客戶端一鍵套用。
**展示重點**：多元促銷工具、通路（Sales/Website/POS）彈性、回購誘因。

---

## Demo 6（章節 Sales Tax）：跨國稅率自動切換
**情境**：客戶從美國搬到加拿大，稅率需自動由 15% 改 5%。
**操作路徑**：Accounting → Fiscal Positions；Sales → New
**步驟**：
1. 建 Canada fiscal position（Detect Automatically + VAT Required），Tax Mapping US 15% → Canada 5%。
2. 聯絡人設 fiscal position，或報價單手動切稅。
3. New 報價加產品 → 預設 15% 自動帶入 → 改選 5% Canada → Confirm。
4. Customer Preview 顯示稅額。
**預期結果**：正確稅率自動套用至對應客戶。
**展示重點**：localization 自動化、跨境合規、會計核准內控。

---

## Demo 7（章節 Delivery）：運費規則 + 前置時間 + 代發貨
**情境**：小件固定運費、大件依重量計費、滯銷品代發貨。
**操作路徑**：Sales → Configuration → Shipping Methods；Products；Purchase Settings
**步驟**：
1. 固定運費方式（小件 $7，滿 $420 免運）；規則制（>30kg=$20、>100kg=$100，順序置頂）→ Publish。
2. 產品設 Customer Lead Time 5 天；Inventory 設 Security Lead Time 2 天。
3. 代發貨：Purchase 啟用 Dropshipping，產品 Inventory 勾 Dropship + 指派供應商。
4. New 訂單 → Confirm → 出現 Purchase 智慧按鈕 → 確認 PO → Dropship → Validate。
**預期結果**：運費自動計算、交期自動排程、供應商直送。
**展示重點**：彈性運費、準時交付緩衝、零庫存擴充商品線。

---

## Demo 8（章節 Pricelists）：多重價目表與毛利保障
**情境**：季節清倉折扣（尾數 .99）+ 保證最低毛利。
**操作路徑**：Sales → Products → Pricelists
**步驟**：
1. 建清倉價目表：outdoor 類 8 折、Rounding 10、尾數 −0.01、最低 2 件、限冬季，電商可見。
2. 建毛利價目表：based on Cost、Margin $20、指定 office chair。
3. New 報價切不同價目表 → Update Prices → Customer Preview 見 .99 尾數與折扣顯示。
**預期結果**：$75 outdoor 椅買 2 件顯示 $59.99；office chair 售價自動高於成本 $20。
**展示重點**：心理定價、毛利保障、分區/分客群定價。

---

## Demo 9（章節 Commissions）：季度階梯佣金
**情境**：業務季度目標 $10,000，達標給 $2,000，設階梯激勵。
**操作路徑**：Sales → Commissions → Commission Plans → New
**步驟**：
1. 啟用 Commissions；New 計畫 based on Targets，達標佣金 $2,000，季頻率。
2. Targets 每季 $10,000；Achievements based on amount invoiced 100%。
3. 指派業務 Mindy；移除 manager 重複計畫。
4. Tiers：50%→$500、100%→$2,000、150%→$3,500、200%→$4,000（圖表）→ Approve。
**預期結果**：依 confirmed invoices 自動計佣，超標加碼。
**展示重點**：多結構佣金追蹤、階梯激勵、個人 vs 團隊。

---

## Demo 10（章節 Integrations）：報價計算機客製試算
**情境**：傢俱組裝服務依人力/距離/風險動態試算。
**操作路徑**：Sales → New → Quote Calculator 智慧按鈕
**步驟**：
1. 選客戶 → 選報價範本（Furniture Essentials，含組裝/運送）。
2. Quote Calculator → Transport and assembly 頁改 Extra volume/車輛/距離 → 運費更新 $158。
3. 設組裝工時、on-site 時數、Risk factor → 組裝 $3,990。
4. Save 回報價，服務金額自動更新。
**預期結果**：非產品專家的業務也能精準試算複雜服務報價。
**展示重點**：試算表與報價連動、減少人為錯誤、適用客製化服務/專案。

---

## Demo 11（章節 General）：批次匯入產品（含變體）
**情境**：新資料庫快速匯入大量產品與變體。
**操作路徑**：Sales → Products → ⚙ → Import
**步驟**：
1. Products → 齒輪 → Import → 下載範本（星號=必填）。
2. 填 Name、Product Type、Product Values（辨識變體）。
3. Upload → First row as header 自動對應 → Test（綠 banner）→ Import。
**預期結果**：大量產品一次匯入，polo 變體歸為同一基礎產品。
**展示重點**：省去人工建檔、變體關聯自動處理、匯入前驗證。

```

---
