# CRM 模組｜操作 SOP

> 狀態：📖 知道（依據 CRM01–CRM22 影片整理）
> 主責：員工_03_流程內控助理（海瑟姆）
> 最後更新：2026-07-20
> Odoo 版本：待確認（推測 Odoo 17/18）

---

## SOP-01｜建立 Lead（潛在客戶）

> 來源：CRM16 Lead and Opportunity Basics | https://www.youtube.com/watch?v=BSEf-EldDIA
> 前提：CRM Settings → Leads 必須啟用

**操作路徑**：CRM → Leads → New

1. 點選 New，填入 Lead 名稱（如：Tables for Bill）
2. 填入聯絡人、公司、電話、Email
3. 查看 Probability 欄位（AI 自動計算）；需要時可手動調整 %
4. 點 AI 按鈕可查看評分依據
5. ⚠️ 不要將 Probability 設為 100%，否則轉換時會報錯

---

## SOP-02｜Lead 轉換為 Opportunity

> 來源：CRM16 | https://www.youtube.com/watch?v=BSEf-EldDIA

**操作路徑**：Lead 表單 → Convert to Opportunity（頂部按鈕）

1. 開啟 Lead 表單
2. 點選 **Convert to Opportunity**
3. 選擇 Conversion Action：
   - **Convert to Opportunity**：建立新商機
   - **Merge with existing opportunities**：與現有商機合併
4. 指派 Salesperson、Sales Team
5. 選擇 Customer：**Create a new customer** 或 **Link to existing customer**
6. 點 **Create Opportunity** → 自動在 Contacts 建立客戶與聯絡人記錄

---

## SOP-03｜在 Pipeline 排程 Activity

> 來源：CRM02, CRM04, CRM14 | https://www.youtube.com/watch?v=pPNuQNZzSLY

**操作路徑（快速）**：Pipeline 卡片 → 時鐘圖示 → Schedule an Activity

1. 點擊商機卡片右下角圖示（灰色時鐘 = 尚無活動）
2. 選擇 Activity Type（Call / Meeting / Email / To-Do / Document）
3. 填入 Summary（摘要）、Due Date、Assigned To、Notes
4. 選擇後續動作：
   - **Open Calendar**：開啟日曆繼續設定
   - **Schedule**：記錄活動
   - **Schedule and Mark as Done**：記錄並立即完成
   - **Done and Schedule Next**：完成並立即排下一個
   - **Cancel**：取消

**活動狀態顏色**：
- 🟢 綠色：期限在未來
- 🟡 黃色：今天到期
- 🔴 紅色：已逾期
- ⬜ 灰色：尚無活動

**商機卡片活動圖示（判讀下一步類型）**：
- ⏰ 灰色時鐘：尚無活動
- 📞 電話圖示：已排 Call
- 👥 人物圖示：已排 Meeting
- ✉️ 信封圖示：已排 Email
- ✅ 勾選圖示：待辦事項 To-Do
- 📄 紙張/上傳圖示：文件或報價單相關活動

**階段（Stage）標題列判讀**：
- 標題右側顯示該階段商機的 Expected/Projected Revenue 加總，拖入新商機會即時更新
- 標題上方彩色狀態條：綠＝已排未來活動、黃/橘＝今天到期、紅＝已逾期、灰＝該階段無任何活動商機；點擊色條可直接篩選對應商機
- 來源：CRM02 All About Activities | https://www.youtube.com/watch?v=rr4kezi9w28、CRM04 Scheduling Activities | https://www.youtube.com/watch?v=pPNuQNZzSLY

---

## SOP-04｜分享可預約時段

> 來源：CRM04 | https://www.youtube.com/watch?v=pPNuQNZzSLY

**操作路徑**：Activity → Open Calendar → Share Availabilities

1. 在排程 Activity 時點 **Open Calendar**
2. 點選 **Share Availabilities**
3. 點選日曆上可用時段（可多選）
4. 點 **Copy Link**，貼給客戶
5. 客戶點連結 → 選擇時間 → 填入資訊 → Confirm → 自動建立活動

---

## SOP-05｜建立自訂 Activity 類型

> 來源：CRM05 Custom Activities | https://www.youtube.com/watch?v=FSG9fOkxxBM

**操作路徑**：CRM → Configuration → Activity Types → New

1. 填入 **Name**（如：Follow-up Email）
2. **Action**：選擇對應動作（Phone Call / Meeting / Upload Document / None）
3. **Dashboard Visibility**：Own Activities（只本人）/ All Activities（全員可見）
4. **Default User**：指定預設負責人（空白 = 當前負責人）
5. **Default Summary**：快速說明活動目的
6. **Schedule**：設定活動期限（基於完成日或期限日，N 天後）
7. **Default Notes**：詳細說明給執行人員
8. **Chaining Type**（串連類型）：
   - **Suggest Next Activity**：完成後建議下一個（使用者自決）
   - **Trigger Next Activity**：完成後自動觸發下一個
9. **Keep Done**：勾選後，完成的活動仍會保留可見（便於主管持續追蹤團隊完成紀錄），預設不勾則完成後可能從畫面消失
10. 點 **Save**

---

## SOP-06｜建立 Activity Plan（活動計畫）

> 來源：CRM06 Activity Plans | https://www.youtube.com/watch?v=7QmhZrmA7SA

**操作路徑**：CRM → Configuration → Activity Plans → New

1. 為每一行活動設定：
   - **Activity Type**：選擇活動類型
   - **Summary**：本計畫特定的說明
   - **Assignment**：Ask at Launch（由商機負責人）/ Default User（固定指定人）
   - **Interval / Unit**：幾天/週/月
   - **Trigger**：Before plan date / After plan date
2. 套用計畫：Pipeline → 商機 → 時鐘圖示 → 選擇 Activity Plan → 設定日期 → **Schedule**

---

## SOP-07｜標記商機為 Won（成交）

> 來源：CRM07 Won and Lost Opportunities | https://www.youtube.com/watch?v=u6kfb1oyneU

**操作路徑**：商機表單右上 → **Won** 按鈕

- Won 後：Probability 自動變 100%，顯示綠色 Won Banner
- Pipeline 中持續可見

---

## SOP-08｜標記商機為 Lost 並還原

> 來源：CRM07 | https://www.youtube.com/watch?v=u6kfb1oyneU

**標記遺失**：商機表單右上 → **Lost** 按鈕

1. 選擇 **Lost Reason**（如：Too Expensive / Company Changed Their Mind）
2. 可輸入 **Closing Note**
3. 確認 → 商機自動從 Pipeline 隱藏

**還原遺失商機**：
1. Pipeline 搜尋列 → Filter → **Lost**
2. 開啟商機 → 點 **Restore**
3. 商機回到原始階段，Lost Banner 消失

---

## SOP-09｜建立銷售團隊

> 來源：CRM08 Sales Teams | https://www.youtube.com/watch?v=27UYtZJ9HKI
> 前提：Settings → Multi Teams + Rule-Based Assignment 已啟用

**操作路徑**：CRM → Configuration → Sales Teams → New

1. 填入 **Team Name**、**Team Leader**
2. 設定 **Email Alias**（發到此 Email 自動建立商機）
3. 設定 **Accept Emails From**（Everyone / Partners / Followers / Employees）
4. 設定 **Invoicing Target**（月度業績目標）
5. **Assignment Rules**：Edit Domain → New Rule → 設定篩選條件
6. **Members Tab**：Add → 選擇業務人員
7. 完成後點 **Assign Leads** 立即指派

**進階：個別業務員專屬指派規則**
除了團隊層級的 Assignment Rules（Domain），還可在 **Members** 分頁點開個別業務員，設定該人專屬規則。
例如：New Rule → Expected Revenue > 10,000（該業務只接高價值商機）。
若勾選 **Skip Auto Assignment**，該業務將跳過系統自動重複指派（但主管手動點 **Assign Leads** 時仍會分派給他）。
- 來源：CRM21 Predictive Lead Scoring | https://www.youtube.com/watch?v=cSML0JkQ0Hg

---

## SOP-10｜設定 Predictive Lead Scoring 與自動指派

> 來源：CRM21 | https://www.youtube.com/watch?v=cSML0JkQ0Hg

**操作路徑**：CRM → Configuration → Settings → Predictive Lead Scoring

1. 點 **Update Probabilities**
2. 選擇計算因子（Stage + Sales Team 固定，可另加 Phone Quality / Email Quality / Country / Language 等）
3. 設定 Lead 起算日期
4. 點 **Update**

**啟用自動指派**：
1. 勾選 **Rule-Based Assignment**
2. Running → **Repeatedly**，設定頻率（建議 1–2 分鐘）
3. 點 **Save**

---

## SOP-11｜安裝 Gmail Mailbox Plugin

> 來源：CRM11 | https://www.youtube.com/watch?v=E6cAjrgHdJo
> 前提：Settings → Integrations → Mail Plugin 已啟用

1. Gmail → 右側欄 **+** → 搜尋 Odoo → 安裝 Odoo Inbox Add-in → Allow → Done
2. 開啟 Email → 點右側 Odoo O 圖示 → Login → 輸入 Database URL
3. 搜尋聯絡人 → Opportunity 區塊點 **Create** → 自動建立商機
4. 或 Task 區塊 → Create → 選擇既有 Project 或建立新 Project（如：Leads de muebles）→ 系統開新分頁進入該任務
5. 若只想把郵件記錄到既有聯絡人（不建商機）：點聯絡人詳細資料旁的放大鏡圖示搜尋聯絡人 → 點聯絡人名稱旁的信封圖示（變綠色勾勾即完成）→ 該郵件會顯示在該聯絡人的 Chatter 中
6. Task 建立後可回到 Project 看板：點 **+ Stage** 新增階段（如：Leads nuevos），再把任務卡片拖曳到新階段管理

---

## SOP-12｜安裝 Outlook Mailbox Plugin

> 來源：CRM12 | https://www.youtube.com/watch?v=SlO4C3EeG-4
> 前提：Settings → Integrations → Mail Plugin 已啟用

1. Odoo Settings → Mail Plugin → 點 ? → 下載 Outlook XML manifest
2. Outlook → Email → 應用程式圖示 → Get Add-ins → My Add-ins → Add from File → 上傳 XML
3. 點選 Odoo Inbox Add-in → Login → 輸入 Database URL
4. 搜尋聯絡人 → 點 Mail 信封圖示（記錄 Email，變綠色勾勾即完成，會顯示在該聯絡人 Chatter 中）或 + 建立 Opportunity（實際開啟的是 Lead 表單，若 CRM 已啟用 Leads 功能）

---

## SOP-13｜建立網站 Lead 表單

> 來源：CRM17 | https://www.youtube.com/watch?v=y3ZVeeM3WEc
> 前提：Website App 已安裝；CRM Settings → Leads 已啟用

1. Website App → 目標頁面 → 點 **Edit**
2. 點選 Submit 按鈕 → Action 改為 **Create an Opportunity**
3. 設定 **Sales Team** 和 **Salesperson**
4. ⚠️ 建立 Opportunity 時公司名稱為必填

---

## SOP-13b｜從 Events（活動報名）自動建立 Lead

> 來源：CRM18 Lead Generation - Events, Appointments, Website Visitors | https://www.youtube.com/watch?v=HFQ1c-VV3Qw
> 前提：CRM Settings → Leads 已啟用

**操作路徑**：Events → Configuration → Lead Generation → New

1. 輸入規則名稱（如：Annual）
2. **Create**：保留 Per Attendee（依每位參加者）
3. **When**：設為 Attendees created（參加者建立時）
4. 視需要限定特定 Event / Event Category / Attendees 條件（留白＝套用所有活動，即通用規則）
5. 選填 Tags、Salesperson、Sales Team
6. ⚠️ **Lead Type** 必須設為 **Lead**（否則規則不會生成 Lead）
7. 測試：前台完成活動報名 → CRM → Leads 中應可看到新 Lead

---

## SOP-13c｜從 Appointments（線上預約）自動建立 Opportunity

> 來源：CRM18 | https://www.youtube.com/watch?v=HFQ1c-VV3Qw

**操作路徑**：Website → Configuration → Appointments → New

1. 輸入預約類型標題（如：free consultation）
2. 切到 **Options** 分頁 → 勾選 **Create Opportunities**
3. 完成後點 **Go to Website** → 將頁面由 Unpublished 切換為已發佈
4. 測試：前台完成預約（輸入姓名/Email/電話並 Confirm）→ CRM → New 階段應可看到新 Opportunity

---

## SOP-13d｜Website Visitors（網站訪客）自動轉 Lead

> 來源：CRM18 | https://www.youtube.com/watch?v=HFQ1c-VV3Qw
> 前提：需 IAP Credits（訪客轉Lead：1 credit/筆）；新帳號通常有 20 free credits

**步驟一：啟用功能**
CRM → Configuration → Settings → 拉到底勾選 **Visits to Leads**

**步驟二：建立 Visit to Lead Rule**
CRM → Configuration → Visit to Lead Rules → New

1. 輸入規則名稱（如：Belgian technology visitors）
2. **Traffic Conditions**：設定 Country、Industries 等條件（留白＝不限）
3. 不勾 **Filter by Company Size** ＝ 不限公司規模
4. **Type** 改為 **Lead**
5. 指定 **Sales Team**
6. 系統會依訪客 IP、可辨識公司資訊、產業、地區判斷是否生成 Lead

⚠️ 每個符合條件且可辨識公司身份的訪客會消耗 1 credit，建議規則不要設太寬鬆，避免浪費點數。

---

## SOP-14｜使用 Lead Mining 主動挖掘潛客

> 來源：CRM20 | https://www.youtube.com/watch?v=-nN9zMkI15s
> 前提：Lead Mining 為 IAP 付費功能

**操作路徑**：CRM → Pipeline → **Generate Leads**

1. 選擇 **Companies** 或 **Companies and Contacts**
2. 設定 Country / State / Industries / Size Filter
3. 選填 Role 或 Seniority（Companies and Contacts 模式）
4. 指定 Sales Team / Salesperson / Default Tags
5. 點 **Generate Leads**

---

## SOP-15｜Lead Enrichment（從 Email 補全資訊）

> 來源：CRM19 | https://www.youtube.com/watch?v=GX_RyFvvxlY
> 前提：CRM Settings → Lead Enrichment 已啟用；需 IAP Credits

1. 開啟商機表單（至少有 Email）
2. 點 **Enrich** 按鈕
3. 自動補全：公司名稱、地址、電話、員工數、產業、技術堆疊
4. 資訊出現在 Chatter 與表單欄位

---

## SOP-16｜Partner Autocomplete 建立聯絡人

> 來源：CRM15 | https://www.youtube.com/watch?v=B9ErlstQ1Ac
> 前提：Settings → Partner Autocomplete 已啟用；需 IAP Credits（1 credit/次）

1. Contacts → New → 切換到 **Company**
2. Name 欄位輸入公司名稱開頭
3. 下拉選單出現 → 點選
4. 自動帶入電話、地址、網站、Logo、Tax ID

---

## SOP-17｜查看銷售團隊報表

> 來源：CRM10 | https://www.youtube.com/watch?v=uypSO1MBMrw

**操作路徑**：Sales → Teams

1. 查看各團隊摘要卡片（Open Opps / Overdue / Quotations / Orders to Invoice）
2. 點數字 → 進入詳細 Kanban 或 List 檢視
3. 切換視圖：Kanban / List / Graph / Pie Chart / Pivot
4. Group By：Sales Team → Salesperson → Stage（可多層巢狀）
5. Filter：Ongoing / Won 等
6. 搜尋列 → Save Current Search → 命名儲存
7. Download → 匯出 Excel

---

## SOP-18｜建立行銷歸因報表（Marketing Attribution）

> 來源：CRM13 | https://www.youtube.com/watch?v=lKvueXqSNmQ
> 前提：行銷活動已設定 UTM 參數

**操作路徑**：CRM → Pipeline → 清除預設 Filter → 搜尋列設定

1. 清除搜尋列預設 Filter
2. Add Custom Filter → Active = true（只看活躍 Lead）
3. 切換到 **List View**
4. 搜尋列 → Group By：Campaign → Source → Country
5. 切換 Graph / Pie Chart / Pivot 查看不同視角
6. Save Current Search → 命名（如：Marketing Attribution Report）→ 可勾 Shared
7. Download → 匯出 Excel

---

## SOP-19｜設定 Gamification 挑戰

> 來源：CRM22 | https://www.youtube.com/watch?v=XL4-or5_T9Y
> 前提：Gamification 模組已安裝；需啟用 Developer Mode

**修改目標定義**：Settings → Gamification Tools → Goal Definitions → 選擇目標
- Computation Mode 改為 **Sum**（金額）或 **Count of Records**（數量）→ Save

**建立挑戰**：Settings → Gamification Tools → Challenges → New

1. 命名挑戰
2. Who：New Rule → Sales Team Members / contains [業務名稱]
3. Periodicity：Monthly / Weekly
4. Start Date / End Date
5. Display Mode：Individual Goals
6. Goals Tab → Add a Line → 選 Goal Definition → 設定 Target（如 $20,000）
7. Rewards Tab → For every succeeding user → 選 Badge
8. Advanced Options → Report Frequency → Weekly
9. 點 **Start Challenge**

---

## 版本紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v0.1 | 2026-07-10 | 建立空殼 |
| v1.0 | 2026-07-20 | 完整填入 19 個 SOP，依據 CRM01–CRM22（海瑟姆） |
| v1.1 | 2026-07-22 | 比對 Notion 舊22篇逐字稿筆記後補齊缺口：新增 SOP-13b/13c/13d（活動報名/線上預約/網站訪客轉Lead三條 Lead 生成管道）；補強 SOP-03（活動圖示＋階段彩色狀態條＋預估營收判讀）、SOP-05（Keep Done欄位）、SOP-09（個別業務員專屬指派規則）、SOP-11/12（聯絡人信封圖示連結＋Project看板拖曳管理）（海瑟姆） |
