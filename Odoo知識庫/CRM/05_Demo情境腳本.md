# CRM 模組｜Demo 情境腳本

> 狀態：📖 草稿（依據 CRM01–CRM22 影片整理，待 Demo 環境驗證後確認）
> 主責：員工_03_流程內控助理（海瑟姆）整理，Jenny 操作驗證
> 最後更新：2026-07-20
> Demo 環境：需 Odoo Demo 環境（建議用 Odoo.com 試用帳號）

---

## Demo-01｜CRM 基礎全流程展示（20 分鐘）

**適用場景**：初次向客戶介紹 CRM 模組全貌

**Demo 故事背景**：
家具公司 StealthyWood 正在展示如何用 Odoo CRM 管理商機。業務員在展覽中認識了潛在客戶 Abigail，想要用 Odoo 跟進這個機會。

**展示步驟**：

1. **Pipeline 總覽**（2 分鐘）
   - 進入 CRM → Pipeline（移除 My Pipeline 篩選看全公司）
   - 介紹 Kanban 看板：各階段（New / Qualified / Proposition / Won）
   - 介紹商機卡片圖示：灰色時鐘（無活動）/ 綠色電話（已排活動，未到期）/ 紅色（逾期）

2. **建立 Lead → 轉換為 Opportunity**（4 分鐘）
   - CRM → Leads → New
   - 填入：Abigail / 公司名稱 / Email / 電話
   - 觀察 AI Probability 自動計算
   - 點 **Convert to Opportunity** → Create new customer
   - 商機表單：填入 Expected Revenue（如 $5,000）、Priority ⭐⭐⭐、Tags

3. **排程 Activity**（3 分鐘）
   - Pipeline 卡片 → 時鐘圖示 → Schedule an Activity
   - 選 Call，填 Summary「Go over lamp quotes」，設 Due Date
   - 指派給 Mitchell Admin（最佳業務）→ Schedule
   - 回到 Pipeline 看電話圖示出現在卡片

4. **移動商機階段**（2 分鐘）
   - 拖拉 Abigail 商機從 New → Qualified
   - 說明：Probability 自動更新
   - 也可從商機表單頂部 Status Bar 點擊移動

5. **Won → 查看報表**（4 分鐘）
   - 點 **Won** 標記成交 → 商機顯示 Won Banner
   - Sales → Teams → 查看 Invoicing Target 進度條

**關鍵訴求**：「所有活動紀錄、Email、商機歷史都在一個地方，不再找不到跟進紀錄。」

---

## Demo-02｜Activity Plan 展示（10 分鐘）

**適用場景**：客戶有標準業務流程，想讓 Odoo 自動展開活動清單

**Demo 故事背景**：
StealthyWood 接到客製家具訂單後，有一套固定的跟進流程（電話確認 → 樣品寄送 → 報價 → 生產確認）。希望用 Activity Plan 一鍵展開。

**展示步驟**：

1. **查看現有 Activity Plan**
   - CRM → Configuration → Activity Plans
   - 開啟「Custom Furniture Production Flow」
   - 說明各欄位：Activity Type / Summary / Assignment / Interval / Trigger

2. **套用 Activity Plan 到商機**
   - Pipeline → 點選 Brian's Bargains 商機
   - 時鐘圖示 → 看到 Activity Plan 選項出現
   - 選擇 Custom Furniture Production Flow → 設定 Due Date → **Schedule**
   - 向下滾動 Planned Activities → 看到所有活動一次展開

3. **說明差異**
   - 「之前手動建立 5 個活動需要 5 分鐘，現在選一次 Plan，10 秒完成」

**關鍵訴求**：「業務流程標準化，新業務也能立刻照正確流程跟進。」

---

## Demo-03｜Won / Lost + 資料分析展示（10 分鐘）

**適用場景**：說明如何用 Lost Reason 做改善分析

**Demo 故事背景**：
某個客戶 Indecisive Inc. 反覆改變主意，展示如何正確記錄 Lost，以及 AI 如何從這些資料學習。

**展示步驟**：

1. **標記 Lost**
   - Pipeline → Lost Filter → 找到 Indecisive Inc.
   - 開啟商機 → Lost Reason：「Company Changed Their Mind」→ Mark as Lost

2. **查看 Lost 商機**
   - Pipeline 搜尋列 → Filter → Lost
   - 說明：平時 Lost 不顯示，避免干擾 Active Pipeline

3. **還原商機**（模擬客戶回頭）
   - 開啟 Lost 商機 → **Restore**
   - 商機回到原始階段

4. **銷售報表**
   - CRM → Reporting → Pipeline
   - Group By：Stage → Salesperson
   - 切換 Graph / Pivot View
   - 「這就是主管定期 Review 時看的報表」

**關鍵訴求**：「每一個 Lost 都是一次學習機會，Odoo 幫你把這些資料積累成 AI 的燃料。」

---

## Demo-04｜Lead Mining + Lead Enrichment 展示（10 分鐘）

**適用場景**：客戶需要主動開發，或現有 Lead 資訊不完整

**Demo 故事背景**：
StealthyWood 想要開拓加州家具市場，同時手上有一個只有 Email 的 Lead 想了解更多資訊。

**展示步驟**：

1. **Lead Mining**
   - CRM → Pipeline → **Generate Leads**
   - 設定：Companies and Contacts / Country: USA / State: California / Industry: Consumer Discretionary
   - 設定 Seniority: Manager
   - **Generate Leads** → 出現 3 個新 Lead
   - 點開其中一個：展示預填的公司名、電話、地址、Chatter 資訊

2. **Lead Enrichment**
   - 開啟一個只有 Email 的商機
   - 點 **Enrich**
   - 展示：補全後的公司名稱、產業、員工數、技術堆疊出現在 Chatter

**關鍵訴求**：「不再只能等客戶上門，Odoo 幫你主動找到對的人，並且補全資訊省去研究時間。」

⚠️ **注意**：兩個功能都需要 IAP Credits（付費），Demo 時須確認 Demo 帳號有足夠餘額。

---

## Demo-05｜Predictive Lead Scoring + 自動指派展示（15 分鐘）

**適用場景**：有多個業務、需要自動分配商機的企業

**展示步驟**：

1. **設定 Predictive Lead Scoring**
   - CRM → Configuration → Settings → Predictive Lead Scoring
   - Update Probabilities：選擇 Email Quality + Country
   - 設定起算日期（如 Jan 1, 2025）→ Update

2. **設定 Rule-Based Assignment**
   - 啟用 Rule-Based Assignment → Repeatedly → 每 2 分鐘
   - Save

3. **銷售團隊指派規則**
   - Configuration → Sales Teams → US Sales Team
   - Assignment Rules → Edit Domain → New Rule：Country = United States
   - New Rule：Probability ≥ 20
   - Confirm

4. **個別業務規則**
   - Members Tab → 點選 Mitchell Admin
   - New Rules：Expected Revenue > 10,000
   - Save

5. **手動觸發指派**
   - Assign Leads 按鈕 → Assign Leads → 完成
   - 展示業務人員的 My Pipeline 新增了商機

**關鍵訴求**：「商機不再靠主管一個個分，Odoo 依你設定的規則，自動把對的 Lead 給對的業務。」

---

## 版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v0.1 | 2026-07-10 | 建立空殼 |
| v1.0 | 2026-07-20 | 完整填入 5 個 Demo 情境，依據 CRM01–CRM22（海瑟姆）；待 Demo 環境驗證 |
