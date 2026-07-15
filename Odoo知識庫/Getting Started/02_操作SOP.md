# Getting Started｜操作 SOP

> 來源：Navigate in Odoo | https://www.youtube.com/watch?v=NoxYrnnHgfk
> Odoo 版本：17 / 18（待確認）
> 學習日期：2026-07-15
> 狀態：🔄 草稿

---

## SOP-01｜認識主畫面 Home / Dashboard

**時間：00:29 - 00:36**

操作路徑：登入 → 主畫面

1. 登入後自動進入主畫面 Home
2. 畫面顯示所有已安裝的應用程式 App 圖示
3. 點擊任一 App 圖示即進入該模組

---

## SOP-02｜頂部工具列圖示說明 Top Bar Icons

**時間：00:36 - 01:32**

操作路徑：主畫面 → 右上角圖示列

圖示由左至右：

| 圖示 | 功能 | 備註 |
|------|------|------|
| 🔴 紅點 | 考勤打卡 Attendance Check-in/out | 需安裝考勤模組 Attendance App |
| 📞 電話 | VoIP 網路電話 Voice over IP | 需第三方 Provider 支援 Odoo |
| 🤖 AI | Odoo AI | 需設定 API Key |
| 💬 聊天 | Discuss 訊息模組 | 連結所有對話 |
| 🕐 時鐘 | 活動清單 Activities | 顯示所有 App 的待辦活動 |
| 🔧 工具箱 | Studio 模組 | 需安裝 Odoo Studio，可自訂 App 介面與欄位 |
| 🏢 公司 | 多公司切換 Multi-company | 僅在啟用多公司設定後出現 |
| 👤 頭像 | 個人選單 User Profile | 偏好設定、資料庫清單、登出 |

---

## SOP-03｜個人偏好設定 Preferences

**時間：03:41 - 05:22**

操作路徑：頭像圖示 → 偏好設定 Preferences

可調整項目：
- 深色模式 Dark Mode：開 / 關
- 通知設定 Notifications
- 語言 Language

**安裝新語言 Language Installation：**
1. 偏好設定 Preferences → 語言 Language 欄位
2. 點選地球圖示 🌍
3. 搜尋並選取語言（例：French）
4. 若已安裝 Odoo 網站，會詢問是否翻譯網站，不需要則略過
5. 點選新增 Add → 完成
6. 系統會詢問是否立即切換語言，選擇保留 Keep 則維持原語言

⚠️ **注意**：偏好設定頁籤的數量取決於已安裝模組。若安裝了員工模組 Employees，會出現員工相關的頁籤；若無，只顯示偏好設定 Preferences 與帳號安全 Account Security 兩個頁籤。

---

## SOP-04｜帳號安全設定 Account Security

**時間：05:22 - 05:46**

操作路徑：頭像圖示 → 偏好設定 Preferences → 帳號安全 Account Security

可操作項目：
1. 修改密碼 Change Password
2. 開啟 / 關閉雙因素驗證 Enable/Disable Two-Factor Authentication (2FA)
3. 登出所有裝置 Log Out from All Devices

---

## SOP-05｜快速導覽捷徑 Shortcuts

**時間：02:32 - 03:19**

操作路徑：頭像圖示 → 捷徑 Shortcuts **或** 鍵盤快捷鍵

快捷鍵：
- Windows：`Ctrl + K`
- Mac：`Cmd + K`

使用方式：
1. 按快捷鍵開啟搜尋框 Shortcuts popup
2. 輸入 `/` + App 名稱（例：`/sales`）→ 直接跳轉至該 App
3. 輸入關鍵字（例：`product`）→ 顯示相關功能，如 Product Variants

---

## SOP-06｜App 導覽——返回主畫面與上一頁

**時間：05:46 - 06:08**

操作路徑：任意模組頁面 → 左上角圖示

- **App 圖示**（左上角小方塊）→ 返回主畫面 Home
- **返回箭頭 ←**（同位置）→ 返回前一個頁面 Previous View

---

## SOP-07｜智慧按鈕 Smart Button

**時間：07:03 - 08:10**

操作路徑：任意單據頁面 → 頂部按鈕區

說明：
- 單據頂部的跨模組連結按鈕
- 點擊後直接跳轉到關聯模組的相關記錄
- Smart Button 的數量與類型取決於：已安裝哪些模組、此記錄與哪些其他記錄有關聯

範例：
- 銷售訂單 Sales Order → Planning 計畫 App 的 Smart Button
- 客戶頁面 Customer Form → 銷售 Sales、發票 Invoices 等多個 Smart Button

---

## SOP-08｜麵包屑導覽 Breadcrumbs

**時間：08:11 - 08:35**

操作路徑：任意頁面 → 左上角路徑列

說明：
- 顯示從入口到當前頁面的完整導覽路徑
- 可點擊任一層級直接回到該頁面

範例路徑：`報價 Quotations > 銷售訂單 Sales Order > 客戶 Customer`

⚠️ **注意**：麵包屑只記錄本次 session 的導覽歷程，不是固定的階層結構。

---

## SOP-補充｜自動儲存與手動儲存 Autosave & Manual Save（接上文）

---

# ── Using Odoo 章節 ──────────────────────────────────────
> 來源：Using Odoo（10 支影片批次處理）
> 學習日期：2026-07-15
> 狀態：🔄 草稿

---

## SOP-09｜Odoo 日曆基礎 Calendar

**來源：** https://www.youtube.com/watch?v=JJtGJTYkss4｜時間：00:00 - 06:37

**方式一：從 Chatter 快速建立會議**

操作路徑：CRM（或任意模組）→ 開啟記錄 → 滑至 Chatter → 活動 Activities 按鈕 → 活動類型選「會議 Meeting」→ 排程 Schedule

1. 點擊 Schedule → 自動跳轉至日曆 Calendar App
2. 於日曆點選空白時間格 → 快速建立活動彈窗
3. 點選「更多選項 More Options」進入完整表單

**方式二：從日曆 App 直接建立**

操作路徑：日曆 Calendar App → 點選時間格或左上角 新增 New

**完整會議表單欄位：**

| 欄位 | 說明 |
|------|------|
| 主旨 Subject | 會議名稱 |
| 參與者 Attendees | 輸入姓名後顯示對方的行程供參考（加入≠正式邀請） |
| 開始時間 Start | 會議時間 |
| 全天 All Day | 切換為全天事件 |
| 時長 Duration | 修改時長，系統自動更新結束時間 |
| 地點 Location | 實體地點 |
| Odoo 會議連結 | 點 + 即建立 Discuss 視訊連結 |
| 忙碌狀態 | 忙碌 Busy / 空閒 Available |
| 隱私 Privacy | 公開 Public / 私人 Private / 內部 Internal |
| 組織者 Organizer | 預設登入者，可指派給其他人 |
| 標籤 Tags | 會議分類標籤 |
| 重複 Recurrent | 定期重複設定 |
| 提醒 Reminder | 可設多個提醒方式（郵件/SMS），發送給所有參與者 |

**傳送邀請：** 完整表單 → 參與者欄旁的 Email 按鈕 → 選擇/編輯郵件範本 → 送出

**完成後：** 返回原記錄 Chatter → 可標記完成 Done / 重新排程 Reschedule / 取消 Cancel

---

## SOP-10｜安排活動 Schedule Activities

**來源：** https://www.youtube.com/watch?v=vyvFgOfBoPI｜時間：00:00 - 08:50

**活動圖示顏色說明（清單視圖）：**

| 顏色 | 意義 |
|------|------|
| 🟢 綠色 | 有未來待辦活動 Upcoming |
| 🟠 橘色 | 今天到期 Due Today |
| 🔴 紅色 | 已逾期 Overdue |
| ⚫ 灰色 | 無活動 No Activities |

圖示形狀也代表活動類型（電話圖示=電話活動、信封=郵件）

**查看我的活動 My Activities Dashboard：**

操作路徑：頂部工具列 → 時鐘圖示 🕐 → 「查看所有活動 View All Activities」

→ 預設清單視圖；可切換 Kanban 視圖
→ 點擊欄位標題可排序（如依到期日排序）
→ 可在此直接新增活動

**完成活動 + 安排下一個：**

1. Chatter → 點活動圖示 → 標記完成 Mark Done
2. 選擇「完成並安排下一步 Done & Schedule Next」→ 繼續填寫下一個活動

**自訂活動類型：**

操作路徑：設定 Settings → Discuss 區塊 → 活動類型 Activity Types → 新增 New

| 欄位 | 說明 |
|------|------|
| 名稱 Name | 活動類型名稱（如 Discovery Call） |
| 動作 Action | 電話/郵件/上傳文件等 |
| 儀表板可見性 Dashboard Visibility | 僅指派對象 / 全部使用者 |
| 預設使用者 Default User | 留空=由建立者指派 |
| 適用模型 Model | 哪些記錄可用此類型 |
| 預設摘要 Default Summary | 活動描述預設值 |
| 連鎖類型 Chaining Type | 建議下一個 Suggest / 自動觸發 Trigger |
| 觸發後動作 Trigger | 完成此活動後自動建立哪種下一個活動 |
| 郵件範本 Email Template | 搭配 Trigger 時使用 |

---

## SOP-11｜聯絡人基礎 Contacts Basics

**來源：** https://www.youtube.com/watch?v=mhFibjoVYmc｜時間：00:00 - 05:12

**安裝聯絡人模組：**
Apps → 搜尋「Contacts」→ 安裝 Install（即使未安裝，部分功能在資料庫中仍持續運作）

**聯絡人自動建立的情境：**
- Sales App 新增供應商 → 自動建立聯絡人
- CRM App 新增商機 → 自動建立聯絡人
- Employees App 新增員工 → 自動建立聯絡人

**建立新聯絡人：**

操作路徑：聯絡人 Contacts App → 新增 New

| 欄位 | 必填 | 說明 |
|------|------|------|
| 姓名 Name | ✅ | 唯一必填項目 |
| 公司 Company | | 若公司不存在，系統自動建立公司聯絡人 |
| 電子郵件 Email | | |
| 電話 Phone | | |
| 職位 Job Position | | |

⚠️ **注意**：設定公司欄位時，若公司名稱在資料庫中不存在，系統會自動建立一筆新的公司聯絡人記錄。

**相關聯絡人 Related Contacts（聯絡人下方頁籤 → 新增相關聯絡人）：**

| 類型 | 用途 |
|------|------|
| 聯絡人 Contact | 同一人的不同聯絡方式（個人/工作信箱）|
| 發票地址 Invoice Address | 帳單寄送地址不同時 |
| 送貨地址 Delivery Address | 倉庫/收貨地址不同時 |
| 其他 Other | 其他需求 |

---

## SOP-12｜聯絡人視圖與管理 Contacts Views & More

**來源：** https://www.youtube.com/watch?v=HxLfnOEWb6Y｜時間：00:00 - 06:33

**視圖切換（右上角按鈕）：**

| 視圖 | 說明 |
|------|------|
| 清單視圖 List View | 預設，快速總覽所有聯絡人與活動 |
| 看板視圖 Kanban View | 以名片形式顯示 |
| 地圖視圖 Map View | 有地址的聯絡人顯示地圖標記；無地址列於「未定位 Unlocated」區塊 |
| 階層視圖 Hierarchy View | 顯示公司 + 員工關聯結構；點擊紫色按鈕展開員工清單 |
| 活動視圖 Activities View | 按聯絡人顯示排定的活動 |

**管理聯絡人（清單視圖）：**

1. 勾選聯絡人旁的勾選框 → 頂部出現「操作 Actions」按鈕
2. 可執行：匯出 Export / 複製 Duplicate / 封存 Archive / 取消封存 Unarchive / 刪除 Delete / 合併 Merge

⚠️ **注意**：已被其他 App 使用的聯絡人**無法刪除**，只能封存 Archive。

**合併重複聯絡人：**

1. 清單視圖 → 勾選要合併的聯絡人
2. 操作 Actions → 合併 Merge
3. 選擇保留的「目標聯絡人 Destination Contact」
4. 確認 → 合併

**批次去重複：** 操作 Actions → 刪除重複 Deduplicate（可清除大量重複聯絡人）

⚠️ **注意**：聯絡人頁面的可見欄位與功能取決於：（1）登入者的存取層級；（2）已安裝的模組數量。

---

## SOP-13｜資料匯入匯出 Import & Export Data

**來源：** https://www.youtube.com/watch?v=Q1GTp2i_d_4｜時間：00:00 - 05:44

**匯出 Export：**

操作路徑：任意清單視圖 → 勾選記錄（或全選）→ 操作 Actions → 匯出 Export

1. 選擇格式：CSV 或 Excel
2. 勾選「我想要更新資料 I want to update data」→ 輸出檔案可直接作為匯入範本
3. 左側：可選擇欄位；右側：已選欄位（可刪除/排序）
4. 點選「匯出 Export」→ 自動下載到電腦

**匯入 Import：**

操作路徑：任意清單視圖 → 齒輪圖示 ⚙️ → 匯入記錄 Import Records

1. 點選「上傳資料檔案 Upload Data File」→ 選擇 CSV / Excel
2. Odoo 自動比對欄位；不匹配的可手動從下拉選單選擇
3. 確認「使用第一列為標題 Use First Row as Header」已勾選
4. 點選「測試 Test」→ 確認無誤後點「匯入 Import」

⚠️ **大量資料建議：** 分批上傳（每次 5,000 筆以內），避免逾時失敗

---

## SOP-14｜Chatter 對話紀錄基礎 Chatter Basics

**來源：** https://www.youtube.com/watch?v=rXtQ2D0w2eY｜時間：00:00 - 04:19

**Chatter 包含的資訊：**
- 記錄建立時間、階段變更、欄位修改歷程
- 收發的郵件訊息
- 內部備註
- 排定/已完成的活動

**右上角工具：**
- 🔍 搜尋訊息
- 📎 附加檔案
- 👥 管理追蹤者 Followers

**追蹤者 Followers 管理：**

操作路徑：Chatter → 追蹤者圖示 → 新增追蹤者 Add Followers → 輸入姓名 → 新增

- 自動追蹤者：指派的業務員自動成為追蹤者
- 手動取消追蹤：點選「追蹤 Follow」按鈕切換
- 可個別設定每位追蹤者的通知設定

**發送訊息 Send Message（外部通訊）：**

操作路徑：Chatter → 發送訊息 Send Message → 確認收件人 → 撰寫內容 → 可附件 → 送出

→ 郵件記錄自動出現在 Chatter

**記錄備註 Log Note（內部通訊）：**

操作路徑：Chatter → 記錄備註 Log Note → 可用 @ 標記同事 → 記錄 Log

→ 只有內部追蹤者可見
→ @ 標記的人自動收到通知

**訊息操作：** 滑過訊息 → 出現 emoji 反應 / ⭐收藏 / ⋯三點選單（轉發/複製連結/刪除）

---

## SOP-15｜罐頭回應 Canned Responses

**來源：** https://www.youtube.com/watch?v=uG2UD-YGl48｜時間：00:00 - 06:06

**建立罐頭回應：**

操作路徑：Discuss App → 設定 Configuration → 罐頭回應 Canned Responses → 新增 New

| 欄位 | 說明 |
|------|------|
| 捷徑 Shortcut | 輸入此文字觸發回應（如 `hello`） |
| 替換文字 Substitution | 完整回應內容（可含 HTML 格式） |

→ 點選欄位外自動儲存

**分享罐頭回應給團隊：**

- 預設：僅建立者可使用
- 分享方式：點入「授權群組 Authorized Groups」欄 → 選擇群組（如 Quality User）
- ⚠️ 即使是管理員，也必須在授權群組中或是建立者，才能使用該罐頭回應

**使用方式（任意 Chatter / Discuss / Helpdesk）：**

在訊息欄位輸入 `:` + 捷徑關鍵字 → 下拉選單出現 → 選擇 → Enter 插入完整訊息

→ 插入後仍可編輯再送出
→ 只輸入 `:` 顯示所有可用回應

**可用範圍：** Discuss / Chatter / Helpdesk / Live Chat / WhatsApp

---

## SOP-16｜摘要郵件 Digest Emails

**來源：** https://www.youtube.com/watch?v=ug7b3MJidsU｜時間：00:00 - 06:00

**啟用摘要郵件功能：**

操作路徑：設定 Settings → 電子郵件 Emails 區塊 → 勾選「摘要郵件 Digest Emails」→ 儲存 Save

**設定預設摘要郵件：**

1. 設定 Settings → Emails → 點選「您的 Odoo 定期摘要 Your Odoo Periodic Digest」右側連結箭頭
2. 設定摘要標題 Digest Title、週期 Periodicity（每日/每週/每月）
3. KPIs 頁籤：勾選/取消勾選要包含的指標（依已安裝模組不同而異）
4. 收件人 Recipients 頁籤：新增收件人 → 可全選所有使用者

**建立新摘要郵件（針對特定部門）：**

1. 設定 Settings → Emails → 設定摘要郵件 Configure Digest Emails → 新增 New
2. 命名、設定週期、選擇 KPIs（只勾選該部門相關指標）
3. 收件人：新增一行 → 使用自訂篩選（如 員工標籤 Employee Tags 包含 "sales"）→ 篩選後全選
4. 立即傳送 Send Now 或等排程自動發送

---

## SOP-17｜自訂 KPI Custom KPIs for Digest Emails

**來源：** https://www.youtube.com/watch?v=mZG-3xHtUyo｜時間：00:00 - 08:44

⚠️ **前置條件：需啟用開發者模式 Developer Mode + 安裝 Odoo Studio**

**步驟一：在 Studio 建立勾選框欄位（顯示於 KPIs 頁籤）**

1. 前往「您的 Odoo 定期摘要」→ 點選右上角 Studio 工具箱圖示
2. 拖曳「勾選框 Checkbox」至 KPIs 頁籤的「自訂 Custom」區域
3. 在屬性中命名（如 Big Opportunities）
4. 記下技術名稱（如 `x_kpi_big_opportunities`）
5. 關閉 Studio

**步驟二：建立計算欄位（提供實際數值）**

1. 技術 Technical → 資料庫結構 Database Structure → 模型 Models → 搜尋 `digest.digest`
2. 找到剛建立的 boolean 欄位 → 點入
3. 新增一行 Add a Line → 欄位名稱 = boolean 名稱 + `_value`（如 `x_kpi_big_opportunities_value`）
4. 欄位類型：整數 Integer
5. 進階屬性 → 依賴 Dependencies → 填入 boolean 欄位名稱和 `company_id`
6. 輸入計算程式碼（Python）→ 儲存並關閉

**命名規則：** `[boolean欄位名]_value` → 這個後綴讓兩個欄位自動連結

---

## SOP-18｜群組存取權限 Group Access Rights

**來源：** https://www.youtube.com/watch?v=w6GLW3IE-UU｜時間：00:00 - 06:55

⚠️ **前置條件：需啟用開發者模式 Developer Mode**

**為何用群組而非個別使用者設定：**
- 人員異動時權限自動跟著群組走
- 一次設定套用全部成員，省時省力

**建立新群組：**

操作路徑：設定 Settings → 使用者與公司 Users & Companies → 群組 Groups → 新增 New

| 頁籤 | 設定內容 |
|------|---------|
| 使用者 Users | 新增此群組的成員 |
| 選單 Menus | 此群組可看到哪些 App 選單 |
| 視圖 Views | 此群組可看到哪些視圖（建議按模型 Model 篩選後全選） |
| 存取權限 Access Rights | 每個模型的 CRUD 權限（讀取/寫入/建立/刪除） |

**存取權限 CRUD 設定：**

| 勾選 | 意義 |
|------|------|
| 讀取 Read | 可查看記錄 |
| 寫入 Write | 可編輯現有記錄 |
| 建立 Create | 可新增記錄 |
| 刪除 Delete | 可刪除記錄 |

**驗證設定：** Settings → Users & Companies → Users → 選擇使用者 → 查看群組欄位是否正確顯示

**時間：06:38 - 07:01**

規則：
- 所有文件與記錄 → **自動儲存 Autosave**
- **設定頁面 Settings → 唯一例外，需手動點選儲存 Save 按鈕**

手動儲存按鈕：
- 編輯中的文件頂部會出現「手動儲存 Save manually」按鈕
- 可點選「捨棄 Discard」取消所有未儲存變更

---

## Business Flows 章節 SOP（2026-07-15）

> 來源：Business Flows 系列 8 支影片
> ⚠️ 本章節為跨模組商業流程示範，涵蓋 Documents / Sign / Projects / Timesheets / Subscriptions / Events / POS / eLearning / Manufacturing 等多個 App，與單模組 SOP 定位不同。

---

### SOP-25｜Documents App 電子郵件別名接收文件

**所屬影片：** 72Wbk0mr0jg（文件管理行政流程）

操作路徑：文件 Documents App → 選取工作資料夾 Workspace Folder → 動作選單 Action Menu → 資訊與標籤 Info & Tags

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | 開啟 Documents App | 左側顯示工作資料夾 Workspace Folders（各部門分類） |
| 2 | 選擇目標資料夾（如 Finance） | 查看電子郵件別名 Email Alias 欄位 |
| 3 | 將此 Email 提供給廠商 | 廠商以此 Email 寄送文件，附件自動上傳至對應資料夾 |
| 4 | 或設定掃描機連接此 Email | 批次掃描文件後自動存入資料庫 |

**驗證：** 寄測試信件含 PDF 附件 → 前往 Finance 資料夾確認文件已出現

---

### SOP-26｜掃描文件拆分與轉換廠商帳單（Split PDF + AI 填入）

**所屬影片：** 72Wbk0mr0jg

操作路徑：Documents App → 開啟多頁 PDF → 使用 Split PDF 工具

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | 開啟包含多份文件的掃描 PDF | 文件工具列頂部出現 Split PDF 按鈕 |
| 2 | 逐頁預覽，點擊合併相鄰頁面 | 同一張發票的兩頁：點選第二頁使其合併到第一頁（不分開） |
| 3 | 點擊藍色勾號排除不需要的頁面 | 例如排除信件等非發票文件 |
| 4 | 選擇「建立廠商帳單 Create Vendor Bill」 | 勾選的頁面自動產生草稿廠商帳單 |
| 5 | 進入 Accounting → Vendors → Bills | 開啟剛建立的草稿帳單 |
| 6 | 點選「重新載入 AI 資料 Reload AI Data」 | Odoo AI 掃描 PDF 內容，自動填入帳單日期、到期日等欄位 |
| 7 | 確認內容無誤後點選「確認 Confirm」 | 帳單進入 Posted 狀態 |

---

### SOP-27｜合約電子簽署（Sign App）

**所屬影片：** 72Wbk0mr0jg

操作路徑：Documents App → 選取合約 PDF → 頂部工具列「簽署 Sign」

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | 開啟需要簽署的 PDF 文件 | 從 Documents App 任意資料夾 |
| 2 | 點選頂部「簽署 Sign」按鈕 | 進入 Sign 欄位設計畫面 |
| 3 | 從左側欄位清單拖入欄位 | 可用欄位：姓名 Name / 日期 Date / 文字 Text / 地址 / 簽名 Signature / 縮寫 Initials |
| 4 | 拖拽調整欄位大小（抓右下角三角形） | 確保欄位大小適合填寫 |
| 5 | 縮寫欄位 Initials：選「新增至所有頁面 Add to All Pages」 | 自動套用到所有頁面，節省設定時間 |
| 6 | 設定完成後點選「傳送 Send」 | 輸入簽署人 Email → 發送邀請連結 |
| 7 | 簽署人點選信件中「簽署 Sign」按鈕 | 進入 Odoo 線上簽署頁面 |
| 8 | 依序填入所有欄位 → 點選「驗證並傳送 Validate and Send Completed Document」 | 完成後文件自動儲存回 Documents App |

**模板管理：** 已設計的簽署模板存放於「簽署 Sign App → 模板 Templates」，不在 Documents App 中，請注意。

---

### SOP-28｜Documents 文件自動化規則設定

**所屬影片：** 72Wbk0mr0jg

操作路徑：Documents App → 動作選單 Action Menu → 自動化 Automations → 新增 New

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | 進入 Documents App 動作選單 → 自動化 | 顯示現有自動化規則清單 |
| 2 | 點選「新增 New」 | 填寫規則名稱 |
| 3 | 模型 Model | 保留 Documents |
| 4 | 觸發條件 Trigger | 可選：「標籤已新增 Tag is Added」/ 文件建立 / 狀態變更等 |
| 5 | 設定觸發標籤（如 Presentations） | 當此標籤被加入文件時觸發 |
| 6 | 動作區 Actions to Do → 新增動作 | 選擇「更新記錄 Update a Record」→ 欄位選 Folder → 設定目標資料夾（如 Marketing） |
| 7 | 儲存並新增第二個動作 | 選「建立活動 Create Activity」→ 設定類型/標題/負責人 |
| 8 | 儲存規則 | 測試：對文件加入觸發標籤 → 確認文件移動 + 活動建立 |

---

### SOP-29｜服務型產品設定（時程表計費 + 訂單觸發建立任務）

**所屬影片：** Q5XbA16x2SE（建設公司 Constru Power）

操作路徑：Inventory → Products → Products → 開啟服務型產品

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | 開啟產品（如 Architect 建築師人力） | |
| 2 | 一般頁籤 General Tab → 產品類型 Product Type | 設為「服務 Service」 |
| 3 | 開票政策 Invoicing Policy | 設為「時程表 Timesheets」（依實際工時計費） |
| 4 | 確認訂單時建立 Create on Order | 設為「任務 Task」（確認銷售訂單後自動建立） |
| 5 | 專案範本 Project Template（如有） | 選擇對應的專案範本，確保每次新建專案有標準化任務架構 |
| 6 | 儲存產品設定 | |

**驗證：** 建立含此產品的銷售訂單 → 確認後 → 頂部 Smart Button 出現「專案 Projects」和「任務 Tasks」

---

### SOP-30｜分析帳戶設定（採購 ↔ 銷售聯結）

**所屬影片：** Q5XbA16x2SE

操作路徑：Accounting App → 設定 Configuration → Settings → 搜尋「分析 Analytic」→ 啟用

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | Accounting → 設定 Configuration → Settings | 搜尋 Analytic Accounting |
| 2 | 啟用分析會計 Analytic Accounting | 儲存後採購單明細出現「分析分配 Analytic Distribution」欄位 |
| 3 | 建立採購單 RFQ | 選廠商、加入產品 |
| 4 | 明細列上點選「分析分配 Analytic Distribution」欄 | 輸入對應的銷售訂單分析帳戶代號 |
| 5 | 確認並收貨後 | 進入 Accounting → Vendors → Bills → 新增 → 選廠商 → 使用 PO 自動完成 |
| 6 | 確認帳單上分析帳戶已自動帶入 | 確保採購成本計入正確專案 |
| 7 | 回到銷售訂單 | 已透過分析帳戶關聯的採購材料自動顯示在銷售訂單明細中 |

**注意：** 欄位若不顯示，點擊明細右側三點「選擇性欄位」→ 勾選「分析分配 Analytic Distribution」

---

### SOP-31｜訂閱產品設定與定期自動開票

**所屬影片：** bj9WHRnFUso（Tech Pro 訂閱制）

操作路徑：Subscriptions 設定 → 產品設定

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | Subscriptions App → Settings | 啟用「線上付款 Online Payment」和「自動開票 Automatic Invoicing」 |
| 2 | Inventory → Products → 開啟或建立服務型產品 | 產品類型 = Service |
| 3 | 勾選「訂閱 Subscription」核取方塊 | 顯示週期訂閱選項（月/年等） |
| 4 | 選擇訂閱計畫 Subscription Plan | 設定計費週期 |
| 5 | 儲存產品 | |
| 6 | 建立銷售訂單並加入此訂閱產品 | 確認訂單後系統自動計算下次開票日期 Next Invoice Date |
| 7 | 系統依設定自動產生循環發票 | 不需手動開票 |

---

### SOP-32｜製造業 BOM 設定與 MTO 路線啟用

**所屬影片：** CLU-zOXwuwM（AirProof 無人機製造）

操作路徑：Manufacturing App → Bill of Materials | Inventory → Configuration → Settings → Routes

| 步驟 | 操作 | 說明 |
|------|------|------|
| 1 | Inventory → Configuration → Settings → 啟用多步驟路線 Multi-Step Routes | 啟用後 MTO 路線選項才會出現 |
| 2 | 從現有產品複製：開啟產品 → 齒輪 → 複製 Duplicate | 快速建立相似產品（如 Drone 4 複製為 Drone 5） |
| 3 | 產品 → 庫存頁籤 Inventory Tab → 路線 Routes | 勾選「製造 Manufacture」和「按訂單補貨 Replenish on Order (MTO)」 |
| 4 | MTO 需解除封存：Inventory → Configuration → Routes → 篩選已封存 Archived → 找到 MTO → 解除封存 Unarchive | |
| 5 | Manufacturing → Bill of Materials → 新增 | 選擇產品、加入零件 Components |
| 6 | 複製 BOM：動作選單 → 複製 Duplicate → 改選新產品 → 修改差異零件 | |
| 7 | 建立製造訂單 Manufacturing Orders | 系統自動依 BOM 列出所需零件及可用數量 |
| 8 | 零件不足時：Operations → Replenishments → 選取缺料零件 → 補貨 Replenish | 自動建立採購申請 |


---

## Getting Started 核心操作 SOP（2026-07-15）

> 來源：Create an Odoo Database + Filters and Views + Multi-Company Basics + Multi-Company Transactions

### SOP-33｜建立 Odoo 資料庫

**目的**：從零建立全新 Odoo 資料庫
**路徑**：odoo.com → Start Now, It's Free 按鈕

**步驟**：
1. 至 odoo.com → 點中央「Start Now, It's Free 立即開始，免費」
2. 選擇要安裝的 App（如 Sales、CRM），可之後再加
3. 右側顯示 15 天免費試用 banner
4. 點 Continue 繼續，填入：
   - First and Last Name 姓名
   - Company Name 公司名稱（自動成為資料庫 URL）
   - Country 國家（⚠️ 影響 Chart of Accounts，之後不可更改）
   - Company Size 公司規模
   - Primary Interest 主要用途
5. 點 Get Started / Start Now → 等待資料庫建立完成
6. 進入資料庫後看到「Activation email sent 啟用信已寄出」黃色警告 → **3 小時內**點信中連結啟用

**注意**：部分 App 會自動隨其他 App 安裝（例：Sales 安裝時會自動安裝 Invoicing）

---

### SOP-34｜新增使用者並設定偏好

**路徑**：Settings 設定 → Users & Companies 使用者與公司 → Users 使用者 → New 新建

**步驟**：
1. Settings → Users → New
2. 填入：
   - Name 姓名
   - Email Address 電子郵件（作為登入帳號）
3. Access Rights 存取權限 標籤：設定各模組的使用者等級
4. Preferences 偏好 標籤：可設定語言、時區、通知方式（Email 或系統內）、深色模式
5. 點 Save 儲存 → 系統自動寄送邀請信給新使用者
6. 若需重設密碼：回到使用者頁面 → ⚙️ 齒輪圖示 → 可選重設密碼

**注意**：Odoo 按使用者數量計費，每新增一位使用者會增加月費

---

### SOP-35｜安裝 Demo 示範資料

**目的**：安裝假資料供教育訓練或測試使用
**路徑**：Settings 設定 → Developer Mode 開發者模式 → Load Demo Data 載入示範資料

**步驟**：
1. Settings → 最下方 → Activate Developer Mode 啟用開發者模式
2. 開發者模式啟用後出現「Load Demo Data 載入示範資料」按鈕
3. 點擊後確認警告視窗
4. ⚠️ **正式資料庫禁用**：Demo 資料會覆蓋全部資料，無法復原

---

### SOP-36｜設定搜尋篩選器與儲存為預設

**路徑**：任一 App 清單頁面 → 搜尋列右側 ▼

**步驟（套用篩選）**：
1. 開啟 App（如 Sales 銷售）
2. 點搜尋列右側下拉箭頭
3. 選擇篩選條件（如：Create Date 建立日期 → 選月份）
4. 再選 Salesperson 業務員 → 可疊加多個篩選

**步驟（儲存為預設）**：
1. 套用篩選後 → 點搜尋列右側 ▼
2. 找到 Favorites 收藏夾 → Save Current Search 儲存目前搜尋
3. 輸入名稱 → 勾選 Default Filter 設為預設 → Save 儲存
4. 之後進入此 App 頁面，預設篩選自動套用

**步驟（刪除預設篩選）**：
1. 點搜尋列標籤旁的 ✏️ 鉛筆圖示
2. 選擇要刪除的收藏 → Delete 刪除

---

### SOP-37｜切換視圖（看板 / 日曆 / 樞紐 / 圖表 / 活動）

**路徑**：任一 App 清單頁 → 右上角視圖切換圖示

**視圖切換說明**：
- **List 清單視圖**（預設）：展開式列表
- **Kanban 看板視圖**：依欄位分欄；可拖曳記錄跨欄（如更換負責業務）
- **Calendar 日曆視圖**：依建立日期/到期日顯示；點擊快速預覽
- **Pivot 樞紐視圖**：交叉統計；Measures 選項增減維度；可插入 Spreadsheet
- **Graph 圖表視圖**：三種圖形（圓餅/折線/長條）；可插入 Spreadsheet
- **Activity 活動視圖**：橫軸=活動類型，縱軸=單據；紅色=逾期，綠色=待辦

---

### SOP-38｜建立子公司與設定財務本地化

**路徑**：Settings 設定 → Companies 公司 → Manage Companies 管理公司

**步驟（建立公司）**：
1. Settings → Companies → Manage Companies → New 新建
2. 填入完整公司資訊，重點欄位：
   - Country 國家：⚠️ 決定財務本地化套件（科目表），**無法更改**
   - Currency 幣別：⚠️ 第一筆交易後**永久鎖定**

**步驟（切換公司）**：
1. 右上角公司名稱 → 下拉選單
2. 勾選目標公司 → Confirm 確認
3. 右上角顯示當前活躍公司（紫色/高亮標示）
4. 多公司同時勾選時，以活躍公司為操作基準

**步驟（設定財務本地化套件）**：
1. 切換至目標公司
2. Settings → Accounting 會計 標籤
3. 頂部 Fiscal Localization 財務本地化 → Package 套件選擇
4. ⚠️ 套件選定後 Odoo 自動安裝對應科目表與稅務
5. ⚠️ 若已有自訂科目表，重設套件將清除所有科目

---

### SOP-39｜跨公司交易設定（買方公司）

**路徑**：Settings 設定 → Companies 公司 → Intercompany Transactions 跨公司交易

**前提**：已安裝 Sales、Purchase、Inventory、Accounting、Contacts

**步驟**：
1. 切換至買方公司（如 Stealthy Wood）
2. Settings → Companies section → 勾選 Intercompany Transactions
3. Create as 設定為 **OdooBot**（留下乾淨稽核軌跡）
4. 只保留買方公司在選單中（取消勾選賣方）
5. 啟用：
   - ✅ Create Purchase Orders 建立採購訂單（賣方確認報價時，自動在買方建立 RFQ）
   - ✅ Create Vendor Bills 建立廠商帳單（賣方確認發票時，自動在買方建立帳單）
6. 設定 Purchase Journal 採購日記帳：選指定的跨公司採購日記帳
7. 儲存

---

### SOP-40｜跨公司交易設定（賣方公司）

**步驟**：
1. 切換至賣方公司（如 Stealthy Pine）
2. Settings → Companies → Intercompany Transactions
3. 啟用：
   - ✅ Create Sales Orders 建立銷售訂單（買方確認 RFQ 時，自動在賣方建立報價）
4. Use Warehouse 設定為賣方的出貨倉庫
5. 設定 Sales Journal 銷售日記帳：選指定的跨公司銷售日記帳
6. 在 Contacts 聯絡人中設定買方的 Pricelist 價格表（對應正確幣別）
7. Products 產品的 Company 欄位設為空白（讓所有公司都能看見）

---

### SOP-41｜跨公司交易示範流程（PO → SO → 出貨 → 開票 → 付款）

**步驟**：
1. **【買方】** 切換至買方公司 → Purchase → New RFQ → 設定 Vendor = 賣方公司
   - 幣別自動切換為賣方幣別 → 加入產品 → Confirm Order 確認訂單
2. **【賣方】** 切換至賣方公司 → Sales → 移除「My Quotations」篩選
   - 看到 OdooBot 自動建立的報價（金額相符）→ Confirm 確認
3. **【賣方出貨】** 點 Delivery 出貨智慧按鈕 → 確認有貨 → Validate 驗貨出貨
4. **【賣方開票】** 回 Sales Order → Create Invoice → 選跨公司銷售日記帳 → Confirm
5. **【買方付款】** 切換回買方 → Accounting → 跨公司採購日記帳 → 開啟草稿帳單 → Confirm
