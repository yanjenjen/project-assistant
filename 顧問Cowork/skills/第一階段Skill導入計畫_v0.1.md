# 第一階段 Skill 導入計畫_v0.1

> 建立日期：2026-06-09
> 主責角色：員工_01_專案分析師（砂砂）
> 版本狀態：v0.1 草稿
> 適用範圍：顧問Cowork 工作區 Skills 層治理
>
> ✅ 第一階段導入完成：2026-06-10。共 12 個候選，5 個 ERP 內層安裝、4 個外層安裝、3 個平台內建 / 已吸收 / 關閉。後續進入壓測與第二階段前置準備。

---

## 一、文件定位

本文件是 Skill 導入層的治理決策中心，職責如下：

- 列出所有第一階段候選 Skill 並逐項判斷是否導入
- 標示「已具備等效功能」的項目，防止重複安裝
- 標示「需要轉寫 ERP 版」的項目，防止直接安裝通用版
- 記錄每個候選的建議放置位置與導入優先級
- 作為後續安裝授權的判斷依據

---

## 二、與 `skills/README.md` 的分工說明

| 面向 | 主要依據 | 說明 |
|---|---|---|
| Skill 技術索引（路徑、版本、測試紀錄） | `skills/README.md` | 已安裝 Skill 的實際位置與技術狀態以此為準 |
| Skill 導入決策（是否要、要不要轉寫） | 本文件 | 候選評估與安裝決策判斷以此為準 |

**衝突處理規則：若本文件與 `skills/README.md` 記載內容不一致，不得自行修正，必須停止並向使用者回報衝突內容，等待指示後再處理。**

---

## 三、欄位設計

每個候選 Skill 記錄以下欄位：

| 欄位 | 說明 |
|---|---|
| 候選編號 | C-001 ~ C-012 |
| Skill 名稱 | 原名或建議工作區命名 |
| 類型 | 通用必備 / ERP 專案需要 / 審查治理用 / Odoo 畫面分析 / 簡報 Demo 用 |
| 是否已具備等效功能 | ✅ 已具備（說明來源）/ ❌ 未具備 / ⏸ 部分具備 |
| 是否需要安裝 | ✅ 需要 / ❌ 不需要 / ⏸ 待條件確認 |
| 是否需要轉寫 ERP 版 | ✅ 需要 / ❌ 不需要 / ⏸ 待評估 |
| 建議放置位置 | 全域 / ERP 專案（分類資料夾）/ 暫不放 |
| 導入優先級 | P0（不需動作）/ P1（本批）/ P2（下批）/ P3（觀察）|
| 風險 | 短描述 |
| 建議處理方式 | 具體可執行的下一步 |

---

## 四、第一階段候選 Skill 清單

| 候選編號 | Skill 名稱 | 類型 | 導入優先級 |
|---|---|---|---|
| C-001 | docx | 通用必備 | P0（已內建，不需動作） |
| C-002 | pptx / powerpoint | 通用必備 / 簡報 Demo 用 | P0（已內建，不需動作） |
| C-003 | meeting-summary | ERP 專案需要 | 外層已安裝 / ERP 內層待轉寫 |
| C-004 | task-breakdown | ERP 專案需要 | P0（已吸收，不需動作） |
| C-005 | capture → **quick-capture** | 通用必備 | ✅ 已安裝（2026-06-09） |
| C-006 | reflect → **session-reflect** | 通用必備 | ✅ 已安裝（2026-06-09） |
| C-007 | evaluation → **consultant-output-evaluator** | 審查治理用 | ✅ 已安裝（2026-06-10） |
| C-008 | skill-security-auditor | 審查治理用 | ✅ 已安裝（2026-06-10） |
| C-009 | ui-analysis → **odoo-ui-analyzer** | Odoo 畫面分析 | ✅ 已安裝（2026-06-09） |
| C-010 | claude-design / sketch → **design-sketch** | 簡報 Demo 用 | 外層已安裝 / ERP 內層暫緩 |
| C-011 | user-research | ERP 專案需要 | 外層已安裝 / ERP 內層待轉寫 |
| C-012 | prompt-engineering | 通用必備 | 外層已安裝 / ERP 內層不安裝 |

---

## 五、12 項逐項判斷

---

### C-001 docx

| 欄位 | 內容 |
|---|---|
| 類型 | 通用必備 |
| 是否已具備等效功能 | ✅ **已內建**。Cowork 平台層 `anthropic-skills:docx` 已啟用，可產出 Word 文件 |
| 是否需要安裝 | ❌ **不需要，禁止重複安裝** |
| 是否需要轉寫 ERP 版 | ❌ 不需要（ERP 格式由 document-template-pattern-extractor + 撰寫規則控制內容層） |
| 建議放置位置 | 全域（已存在，不需動作） |
| 導入優先級 | P0（已具備，關閉此候選） |
| 風險 | 無 |
| 建議處理方式 | 標示「已內建，確認可用」，關閉此候選，不再評估 |

---

### C-002 pptx / powerpoint

| 欄位 | 內容 |
|---|---|
| 類型 | 通用必備 / 簡報 Demo 用 |
| 是否已具備等效功能 | ✅ **已內建**。Cowork 平台層 `anthropic-skills:pptx` 已啟用 |
| 是否需要安裝 | ❌ **不需要，禁止重複安裝** |
| 是否需要轉寫 ERP 版 | ❌ 不需要（ERP 簡報內容由 07_簡報與教學 Skill 控制，格式層沿用內建即可） |
| 建議放置位置 | 全域（已存在，不需動作） |
| 導入優先級 | P0（已具備，關閉此候選） |
| 風險 | 無 |
| 建議處理方式 | 標示「已內建，確認可用」，關閉此候選，不再評估 |

---

### C-003 meeting-summary

| 欄位 | 內容 |
|---|---|
| 類型 | ERP 專案需要 |
| 外層安裝名稱 | `meeting-summary` |
| 外層安裝日期 | 2026-06-10 |
| 外層 SKILL.md 路徑 | `Claude一般事務/skills/meeting-summary/SKILL.md`（已建立） |
| 外層定位 | 一般會議摘要 / 日常工作討論整理 / 課程影片摘要 / 非正式會議紀要整理 |
| 外層觸發詞 | `會議記錄：` / `整理這段會議` / `幫我做一份會議紀錄` / `meeting-summary：` |
| ERP 內層是否引用外層能力 | ❌ **不引用**。ERP 正式輔導備忘錄格式需求與通用版差異大，直接引用外層能力會繞過 WR-002 規則 |
| ERP 內層狀態 | ⏸ **第二階段轉寫候選**。不得用通用版直接產出正式 ERP 輔導備忘錄 |
| ERP 內層未來候選名稱 | `erp-meeting-record-writer` |
| ERP 內層前置條件 | WR-002 會議紀錄規則完成壓測並升版後，另行授權建立 |
| 與既有 ERP Skill 邊界 | 與 `document-template-pattern-extractor` 關係：extractor 萃取會議紀錄撰寫規則（基準）；`erp-meeting-record-writer` 依規則產出正式文件 |
| 觸發詞控管 | ERP 內層無此 Skill，外層觸發詞在 ERP 對話中使用時，輸出只能作為草稿 / 口語摘要，不得直接提交為正式交付文件 |
| 風險 | 外層通用版在 ERP 對話中被誤用為正式交付文件，可能繞過 WR-002 規則 |
| 最終處置 | 外層安裝通用版 / ERP 內層第二階段轉寫 `erp-meeting-record-writer`（前置：WR-002 壓測完成） |

---

### C-004 task-breakdown

| 欄位 | 內容 |
|---|---|
| 類型 | ERP 專案需要 |
| 是否已具備等效功能 | ✅ **已由 erp-task-planning-assistant 吸收**。包含任務拆解、範圍確認、依賴關係、P0/P1/P2 判斷與任務規劃書產出 |
| 是否需要安裝 | ❌ **不需要，禁止安裝**（重複安裝會造成觸發詞衝突） |
| 是否需要轉寫 ERP 版 | ❌ 不需要（已有 ERP 版） |
| 建議放置位置 | 不需動作 |
| 導入優先級 | P0（已具備，關閉此候選） |
| 風險 | 若仍安裝通用版 task-breakdown，可能與 erp-task-planning-assistant 的觸發詞衝突，導致 AI 啟用錯誤 Skill |
| 建議處理方式 | 標示「已由 erp-task-planning-assistant 吸收，確認不安裝」，關閉此候選 |

---

### C-005 capture → quick-capture ✅ 已安裝

| 欄位 | 內容 |
|---|---|
| 類型 | 通用必備 |
| 實際 Skill 名稱 | `quick-capture` |
| 安裝路徑 | `skills/00_通用工作流/quick-capture/SKILL.md` |
| 安裝日期 | 2026-06-09 |
| 安裝方式 | 自建（平台與 plugin 市集均無對應版本） |
| 是否已具備等效功能 | ✅ 已安裝。自建工作區 Skill，平台層查無現成版本 |
| 是否需要轉寫 ERP 版 | ❌ 不需要。屬通用工作習慣輔助，不涉及 ERP 專業內容 |
| 實際放置位置 | `skills/00_通用工作流/`（新建分類資料夾，全域通用） |
| 導入優先級 | ✅ 已完成（原 P1） |
| 狀態 | 🔶 試行中（新安裝，尚未壓測） |
| 回復方式 | 若觸發錯誤，提出停用計畫 → 使用者授權 → 封存至 `skills/99_封存/` → 更新 README.md 與本文件 |

---

### C-006 reflect → session-reflect ✅ 已安裝

| 欄位 | 內容 |
|---|---|
| 類型 | 通用必備 |
| 實際 Skill 名稱 | `session-reflect` |
| 安裝路徑 | `skills/00_通用工作流/session-reflect/SKILL.md` |
| 安裝日期 | 2026-06-09 |
| 安裝方式 | 自建（平台與 plugin 市集均無對應版本） |
| 是否已具備等效功能 | ✅ 已安裝。自建工作區 Skill，平台層查無現成版本 |
| 是否需要轉寫 ERP 版 | ❌ 不需要。屬通用工作習慣輔助 |
| 實際放置位置 | `skills/00_通用工作流/`（全域通用，與 quick-capture 同分類） |
| 導入優先級 | ✅ 已完成（原 P1） |
| 狀態 | 🔶 試行中（新安裝，尚未壓測） |
| 與 quick-capture 差異 | capture = 工作中單筆即時；reflect = 段落結束後整體彙整 |
| 回復方式 | 若觸發錯誤，提出停用計畫 → 使用者授權 → 封存至 `skills/99_封存/` → 更新 README.md 與本文件 |

---

### C-007 evaluation → consultant-output-evaluator

| 欄位 | 內容 |
|---|---|
| 類型 | 審查治理用 |
| Skill 正式名稱 | `consultant-output-evaluator` |
| 安裝日期 | 2026-06-10 |
| 安裝方式 | 自建（平台與 plugin 市集均無對應版本） |
| 是否已具備等效功能 | ✅ 已安裝。自建工作區 Skill，定位為 ERP 顧問工作成果品質評估工具 |
| 是否需要轉寫 ERP 版 | ✅ 已直接以 ERP 顧問版建立 |
| 實際放置位置 | `skills/08_治理與審查/consultant-output-evaluator/` |
| 導入優先級 | ✅ 已完成（原 P2） |
| 狀態 | 🔶 試行中（新安裝，尚未壓測） |
| 觸發設計 | 僅明確呼叫時啟動（evaluate：/ 評估一下：/ 幫我驗收：/ 審查這份：/ 幫我檢查一下：），不得自動介入任務 |
| 回復方式 | 若觸發錯誤，提出停用計畫 → 使用者授權 → 封存至 `skills/99_封存/` → 更新 README.md 與本文件 |

---

### C-008 skill-security-auditor

| 欄位 | 內容 |
|---|---|
| 類型 | 審查治理用 |
| Skill 正式名稱 | `skill-security-auditor` |
| 安裝日期 | 2026-06-10 |
| 安裝方式 | 自建（平台與 plugin 市集均無對應版本） |
| 是否已具備等效功能 | ✅ 已安裝。自建工作區 Skill，定位為 Skill 安全性靜態審查工具 |
| 是否需要轉寫 ERP 版 | ❌ 不需要（治理工具本身不需領域化） |
| 實際放置位置 | `skills/08_治理與審查/skill-security-auditor/` |
| 導入優先級 | ✅ 已完成（原 P2） |
| 狀態 | 🔶 試行中（新安裝，尚未壓測） |
| 觸發設計 | 僅明確呼叫時啟動（skill-audit：/ 審查這個 Skill：/ 檢查這個 Skill 安不安全：），不得自動介入任何安裝或執行流程 |
| 回復方式 | 若觸發錯誤，提出停用計畫 → 使用者授權 → 封存至 `skills/99_封存/` → 更新 README.md 與本文件 |

---

### C-009 ui-analysis → odoo-ui-analyzer ✅ 已安裝

| 欄位 | 內容 |
|---|---|
| 類型 | Odoo 畫面分析 |
| 實際 Skill 名稱 | `odoo-ui-analyzer` |
| 安裝路徑 | `skills/01_技術開發/odoo-ui-analyzer/SKILL.md` |
| 安裝日期 | 2026-06-09 |
| 安裝方式 | 自建 Odoo 專用版（跳過通用版，平台查無對應；直接建立 ERP 顧問版） |
| 是否已具備等效功能 | ✅ 已安裝。自建 Odoo 畫面顧問分析 Skill |
| 是否需要轉寫 ERP 版 | ✅ 已直接建立 Odoo 專用版，跳過通用版 |
| 實際放置位置 | `skills/01_技術開發/`（首次建立此分類資料夾） |
| 導入優先級 | ✅ 已完成（原 P1） |
| 狀態 | 🔶 試行中（新安裝，尚未壓測） |
| 回復方式 | 若觸發錯誤或與既有 Odoo Skill 混淆，提出停用計畫 → 使用者授權 → 封存至 `skills/99_封存/` → 更新 README.md 與本文件 |

---

### C-010 claude-design / sketch → design-sketch

| 欄位 | 內容 |
|---|---|
| 類型 | 簡報 Demo 用 |
| 外層安裝名稱 | `design-sketch` |
| 外層安裝日期 | 2026-06-10 |
| 外層 SKILL.md 路徑 | `Claude一般事務/skills/design-sketch/SKILL.md`（已建立） |
| 外層定位 | 一般設計草圖 / PPT 架構 / 流程圖 / Demo 草圖 / 文件視覺化輔助 / 系統畫面呈現建議 |
| 外層觸發詞 | `設計草圖：` / `幫我畫流程圖` / `幫我做 PPT 架構` / `Demo 畫面建議` / `design-sketch：` |
| ERP 內層是否引用外層能力 | ✅ **允許引用**。ERP 對話中可引用外層 `design-sketch` 能力，用於：PPT 架構規劃、流程圖草稿、Demo 展示邏輯、系統畫面呈現建議 |
| ERP 內層引用限制 | 不得取代 `odoo-ui-analyzer`；引用外層能力產出的設計草稿僅供參考，不得直接作為 ERP 正式交付文件 |
| ERP 內層狀態 | ⏸ **暫緩轉寫**。若 ERP 內層設計需求趨於穩定，再另建 `erp-demo-sketch-assistant` 或 `odoo-screen-layout-advisor` |
| ERP 內層未來候選名稱 | `erp-demo-sketch-assistant` 或 `odoo-screen-layout-advisor`（待需求確認） |
| 與既有 ERP Skill 邊界 | `odoo-ui-analyzer`：分析既有 Odoo 畫面（輸入分析）；`design-sketch`：產出視覺草圖或呈現建議（輸出設計）。方向相反，不重疊，不得互相取代 |
| 觸發詞控管 | ERP 內層引用外層能力時，明確使用外層觸發詞（`設計草圖：` / `幫我畫流程圖` 等）；不得用 `odoo-analyze：` 觸發設計草圖輸出 |
| 風險 | 外層觸發詞「流程圖 / Demo」在 ERP 對話中可能產出未經驗證的 Odoo 畫面建議，需注意標示為草稿 |
| 最終處置 | 外層安裝通用版 / ERP 內層允許引用外層能力 / 正式 ERP 版暫緩轉寫 |

---

### C-011 user-research

| 欄位 | 內容 |
|---|---|
| 類型 | ERP 專案需要 |
| 外層安裝名稱 | `user-research` |
| 外層安裝日期 | 2026-06-10 |
| 外層 SKILL.md 路徑 | `Claude一般事務/skills/user-research/SKILL.md`（已建立） |
| 外層定位 | 使用者本人理解 / 個人工作流觀察 / 描述方式與學習卡點分析 / 工作習慣與 AI 協作偏好；研究對象為「使用者本人（Jenny）」 |
| 外層觸發詞 | `了解我的習慣：` / `分析我的描述方式` / `我的學習卡點是什麼` / `你對我的工作方式有什麼觀察` / `user-research：` |
| ERP 內層是否引用外層能力 | ❌ **不引用**。外層研究對象是使用者本人；ERP 內層研究對象是客戶與企業流程角色。對象根本不同，不得混用 |
| ERP 內層狀態 | ⏸ **第二階段轉寫候選**。需完整重寫 ERP 客戶訪談版本，不沿用外層通用版 |
| ERP 內層未來候選名稱 | `erp-interview-researcher` |
| ERP 內層前置條件 | 有明確客戶訪談任務需求時，另行授權建立 |
| 與既有 ERP Skill 邊界 | `erp-task-planning-assistant`：任務規劃時含訪談前置問題（輕量）；`erp-interview-researcher`（未來）：系統性 ERP 流程訪談設計與記錄（深度）。兩者定位深度不同，不重疊 |
| 觸發詞控管 | 外層觸發詞（`了解我的習慣：` 等）研究對象限定為使用者本人，不得在 ERP 客戶訪談場景下使用 |
| 安全限制 | 不得在未被明確要求時主動點評使用者行為 |
| 最終處置 | 外層安裝通用版（研究對象：使用者本人）/ ERP 內層第二階段轉寫 `erp-interview-researcher`（研究對象：客戶與企業角色） |

---

### C-012 prompt-engineering

| 欄位 | 內容 |
|---|---|
| 類型 | 通用必備 |
| 外層安裝名稱 | `prompt-engineering` |
| 外層安裝日期 | 2026-06-10 |
| 外層 SKILL.md 路徑 | `Claude一般事務/skills/prompt-engineering/SKILL.md`（已建立） |
| 外層定位 | AI 指令設計 / Prompt 優化 / Claude Code 指令整理 / AI 寫程式與除錯指令輔助 |
| 外層觸發詞 | `優化指令：` / `幫我改這個 prompt` / `這個指令怎麼寫更好` / `幫我寫一個 Claude Code 指令` / `prompt-engineering：` |
| ERP 內層是否引用外層能力 | ✅ **允許，但需明確前綴**。ERP Cowork 內層可引用外層能力，僅限以下明確觸發詞啟動：`優化指令：` / `幫我寫 Claude Code 指令：` |
| ERP 內層引用限制 | 不得自動取代 `erp-task-planning-assistant`；不得在無明確前綴的情況下介入 ERP 任務規劃流程；不得因「任務拆解 / 規劃 / 分析」等語意自動啟動 |
| ERP 內層狀態 | ❌ **不在工作區 `skills/` 下安裝通用版**，只允許引用外層能力（明確前綴控管） |
| 與既有 ERP Skill 邊界 | `prompt-engineering`（外層引用）：AI 指令設計 / Prompt 優化；`erp-task-planning-assistant`：ERP 顧問任務規劃。兩者嚴格不重疊，不得互相取代 |
| 觸發詞控管 | ERP 內層引用必須使用明確前綴（`優化指令：` / `幫我寫 Claude Code 指令：`）；不接受「幫我拆解這個任務」等模糊語意觸發 |
| 風險 | 外層觸發詞在 ERP 對話中若未加前綴，可能與 `erp-task-planning-assistant` 形成競爭觸發 |
| 最終處置 | 外層安裝通用版 / ERP 內層允許明確前綴引用 / ERP `skills/` 下不安裝 |

---

## 六、特別判斷摘要

| 項目 | 判斷結論 |
|---|---|
| docx / pptx 是否已內建 | ✅ 兩者均已內建於 Cowork 平台層，**確認不重複安裝** |
| task-breakdown 是否已被吸收 | ✅ 已由 `erp-task-planning-assistant` 完整吸收，確認不安裝 |
| meeting-summary 分層策略 | 外層安裝通用版 / ERP 內層不引用（格式差異大）/ 第二階段轉寫 `erp-meeting-record-writer`（前置：WR-002 壓測） |
| evaluation / skill-security-auditor | ✅ ERP 內層已安裝（2026-06-10），狀態：試行中 |
| ui-analysis | ✅ ERP 內層已安裝 `odoo-ui-analyzer`（2026-06-09），狀態：試行中 |
| design-sketch 分層策略 | 外層安裝通用版 / ERP 內層允許引用外層能力（PPT / 流程圖 / Demo 草圖）/ 不取代 `odoo-ui-analyzer` / 正式版暫緩 |
| capture / reflect | ✅ ERP 內層已安裝 `quick-capture` / `session-reflect`（2026-06-09），狀態：試行中 |
| user-research 分層策略 | 外層安裝通用版（研究對象：使用者本人）/ ERP 內層不引用（對象根本不同）/ 第二階段轉寫 `erp-interview-researcher` |
| prompt-engineering 分層策略 | 外層安裝通用版 / ERP 內層允許明確前綴引用（`優化指令：`）/ ERP `skills/` 下不安裝 / 不取代 `erp-task-planning-assistant` |

---

## 七、第一階段全部處置結果（2026-06-10 收斂）

### P0 — 已具備，關閉候選（3 項）

| 候選 | 最終狀態 |
|---|---|
| C-001 docx | ✅ 已內建（Cowork 平台層），關閉候選 |
| C-002 pptx | ✅ 已內建（Cowork 平台層），關閉候選 |
| C-004 task-breakdown | ✅ 已由 `erp-task-planning-assistant` 吸收，關閉候選 |

### ERP 內層已安裝（5 項）

| 候選 | 實際名稱 | 安裝日期 | 狀態 |
|---|---|---|---|
| C-005 capture | `quick-capture` | 2026-06-09 | 🔶 試行中 |
| C-006 reflect | `session-reflect` | 2026-06-09 | 🔶 試行中 |
| C-007 evaluation | `consultant-output-evaluator` | 2026-06-10 | 🔶 試行中 |
| C-008 skill-security-auditor | `skill-security-auditor` | 2026-06-10 | 🔶 試行中 |
| C-009 ui-analysis | `odoo-ui-analyzer` | 2026-06-09 | 🔶 試行中 |

### 外層已安裝 / ERP 內層分層處置（4 項）

| 候選 | 外層名稱 | ERP 內層狀態 | ERP 未來候選名稱 | 觸發條件 |
|---|---|---|---|---|
| C-003 meeting-summary | `meeting-summary` | ⏸ 待轉寫（WR-002 壓測完成後） | `erp-meeting-record-writer` | WR-002 升版授權 |
| C-010 design-sketch | `design-sketch` | ⏸ 暫緩 | `erp-odoo-demo-sketch`（候選） | 有明確 Odoo Demo 需求時 |
| C-011 user-research | `user-research` | ⏸ 待轉寫（有客戶訪談需求時） | `erp-interview-researcher` | 有正式客戶訪談任務時 |
| C-012 prompt-engineering | `prompt-engineering` | ❌ 不安裝（避免與 `erp-task-planning-assistant` 衝突） | 無 | — |

---

## 八、風險

| 風險代號 | 描述 | 影響 | 預防措施 |
|---|---|---|---|
| R-01 | 內建 Skill 與自訂 Skill 觸發詞衝突 | AI 可能啟動錯誤 Skill | 每個新 Skill 安裝前確認觸發詞無衝突 |
| R-02 | 通用版 Skill 產出不符 ERP 顧問標準 | 輸出格式與顧問語氣不符，可能污染正式交付物 | 需要轉寫 ERP 版的項目，不得跳過轉寫直接用通用版 |
| R-03 | 本文件與 skills/README.md 不同步 | 安裝後若只更新 README.md，兩表分岐 | 安裝後需同時更新本文件的導入狀態欄位，標示為「✅ 已安裝（日期）」 |
| R-04 | Skill 數量膨脹超出追蹤能力 | 觸發條件相互干擾，README.md 管理負擔增加 | 每批安裝不超過 3 個；每個安裝後需完成至少一次試行測試才評估下一批 |

---

## 九、回復方式

**場景：安裝後發現 Skill 觸發錯誤**
1. 停止使用該 Skill
2. 向使用者回報觸發問題描述
3. 提出停用計畫，等確認後封存至 `skills/99_封存/`
4. 更新本文件與 skills/README.md

**場景：本文件與 skills/README.md 衝突**
1. 停止所有安裝動作
2. 向使用者回報衝突項目與兩表各自記載內容
3. 等使用者確認哪一表為準，再修正指定表

**場景：P1 Skill 試行後需升版或調整**
1. 員工_01 提出升版計畫（範圍、內容、ERP 轉寫必要性）
2. 使用者確認後執行，同步更新本文件與 skills/README.md

---

## 十、本週是否建議建立此文件

✅ **建議本週建立（已執行）。**

理由：docx / pptx 已內建確認、task-breakdown 已吸收確認、meeting-summary 等待條件明確等三個關鍵判斷，若不落地為正式文件，下次任務仍需重新確認，造成浪費。

---

## 十一、本週是否建議安裝第一批 Skill

⏸ **建議本週先確認 P1 候選是否可在平台安裝，安裝動作下一輪再授權執行。**

P1 候選（尚未安裝，需使用者授權後才可執行）：

| 候選 | 建議名稱 | 理由 |
|---|---|---|
| C-005 capture | 待確認平台版本 | 通用工作習慣，全域，低風險 |
| C-006 reflect | 待確認平台版本 | 通用工作習慣，全域，低風險 |
| C-009 ui-analysis | 建議先試通用版 | ERP 顧問分析 Odoo 畫面截圖有實際需求 |

> 以上三項為 P1 候選，安裝前仍需提出計畫、確認觸發詞不衝突、使用者明確授權後才可執行。

---

*本文件由 員工_01_專案分析師（砂砂）建立，適用範圍為顧問Cowork工作區 Skills 層治理。*
