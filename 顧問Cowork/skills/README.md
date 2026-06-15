# skills/ — ERP 顧問 Cowork Skills 管理說明

## 定位

`skills/` 是 AI 員工的**執行能力模組區**，不是一般文件資料夾。
每個 Skill 定義一類工作的觸發條件、執行流程與產出規則，
由 Claude / Cowork 在任務開始時識別並啟用。

---

## 目標分類架構（邏輯規劃，資料夾依需求建立）

| 分類資料夾 | 中文名稱 | 用途說明 | 建立狀態 |
|---|---|---|---|
| `00_通用工作流` | 通用工作流 | 快速捕捉、回顧沉澱、通用工作習慣輔助 Skill | ✅ 已建立 |
| `01_技術開發` | 技術開發 | ERP 系統模組開發、技術規格、說明書產出、Odoo 畫面顧問分析 | ✅ 已建立 |
| `02_文件與交付` | 文件與交付 | 文件範本萃取、格式規則、交付文件品質輔助 | ✅ 已建立 |
| `03_流程與內控` | 流程與內控 | 流程建模、內控點辨識、例外情境分析 | 未建立 |
| `04_需求與規格` | 需求與規格 | 需求訪談、GAP 分析、規格書撰寫 | ✅ 已建立 |
| `05_專案管理` | 專案管理 | 時程規劃、里程碑追蹤、風險判斷、最小可交付成果收斂 | ✅ 已建立 |
| `06_資料治理與檔案管理` | 資料治理與檔案管理 | 檔案命名、資料分類、歸檔建議、敏感資料初判、Excel / CSV / 匯入資料前置治理 | ✅ 已建立 |
| `07_簡報與教學` | 簡報與教學 | 教育訓練簡報製作、說明文件產出 | 未建立 |
| `08_治理與審查` | 治理與審查 | ERP 顧問成果品質評估、Skill 安全審查 | ✅ 已建立 |
| `99_封存` | 封存 | 停用或已替代的 Skill 封存區 | 未建立 |

> 原則：有 Skill 要放入時才建立資料夾，不預建空殼。

---

## Skill 索引表

| Skill 名稱 | 中文說明 | 邏輯分類 | 實際路徑 | 版本 | 狀態 | 最後更新 |
|---|---|---|---|---|---|---|
| `quick-capture` | 快速捕捉決定 / 待辦 / 風險 / 阻塞點 | `00_通用工作流` | `skills/00_通用工作流/quick-capture/` | v0.1.0 | 🔶 試行中（新安裝，尚未壓測） | 2026-06-09 |
| `session-reflect` | 任務段落結束後的整體狀態回顧 | `00_通用工作流` | `skills/00_通用工作流/session-reflect/` | v0.1.0 | 🔶 試行中（新安裝，尚未壓測） | 2026-06-09 |
| `odoo-ui-analyzer` | Odoo 畫面顧問分析（欄位 / 控制點 / 需求確認點） | `01_技術開發` | `skills/01_技術開發/odoo-ui-analyzer/` | v0.1.0 | 🔶 試行中（新安裝，尚未壓測） | 2026-06-09 |
| `consultant-output-evaluator` | ERP 顧問工作成果品質評估 | `08_治理與審查` | `skills/08_治理與審查/consultant-output-evaluator/` | v0.1.0 | 🔶 試行中（新安裝，尚未壓測） | 2026-06-10 |
| `skill-security-auditor` | Skill 安全性靜態審查（觸發、寫檔、衝突、回復） | `08_治理與審查` | `skills/08_治理與審查/skill-security-auditor/` | v0.1.0 | 🔶 試行中（新安裝，尚未壓測） | 2026-06-10 |
| `odoo-module-spec-writer` | Odoo 模組系統功能說明書製作 | `01_技術開發` | `skills/odoo-module-spec-writer/` | 版本未標示 | ✅ 啟用（暫放根目錄） | 2026-05-27 |
| `odoo-large-feature-dev` | Odoo 大型功能開發方法論（9 階段） | `01_技術開發` | `skills/odoo-large-feature-dev/` | 版本未標示 | ✅ 啟用（暫放根目錄） | 2026-05-27 |
| `document-template-pattern-extractor` | 公司範例模板規則萃取器 | `02_文件與交付` | `skills/02_文件與交付/document-template-pattern-extractor/` | v0.1.0 | 🔶 試行中（已完成初步實測：規格書規則萃取、會議紀錄規則萃取各一次） | 2026-06-04 |
| `erp-meeting-record-writer` | ERP 顧問輔導備忘錄草稿產出器 | `02_文件與交付` | `skills/02_文件與交付/erp-meeting-record-writer/` | v0.1.0 | 🔶 試行中（已通過 skill-security-auditor 安全審查，S-001 小修完成；尚未完成實際任務壓測） | 2026-06-12 |
| `erp-interview-researcher` | ERP 顧問訪談前問題設計助理 | `04_需求與規格` | `skills/04_需求與規格/erp-interview-researcher/` | v0.1.0 | 🔶 試行中（已通過 skill-security-auditor 安全審查，S-001 小修完成；尚未完成實際任務壓測） | 2026-06-12 |
| `erp-task-planning-assistant` | ERP 顧問任務規劃助理 | `04_需求與規格` | `skills/04_需求與規格/erp-task-planning-assistant/` | v0.1.0 | 🔶 試行中（已完成 T1 正式規劃 / T2 暫定規劃 / T3a 快捷語啟動 / T3b 情況B拒絕 四項測試通過；可提出 v1.0 升版計畫，尚未升版） | 2026-06-06 |
| `project-fast-delivery-assistant` | 專案趕工交付助理 | `05_專案管理` | `skills/05_專案管理/project-fast-delivery-assistant/` | v0.2.0 | 🔶 試行中（未壓測） | 2026-06-04 |
| `file-naming-and-classification-advisor` | 文件命名與歸檔建議 | `06_資料治理與檔案管理` | `skills/06_資料治理與檔案管理/file-naming-and-classification-advisor/` | v0.1.0 | 🔶 試行中（已完成一次檔名清單測試，尚未完成實際改名／搬移測試） | 2026-06-03 |

---

## Skill 命名規則

格式：`{動作}-{對象}-{產出類型}`，全小寫，連字號分隔。

| 元素 | 說明 | 範例 |
|---|---|---|
| 動作 | 此 Skill 執行什麼動作 | `write`, `extract`, `analyze`, `map`, `validate` |
| 對象 | 作用對象是什麼 | `odoo-module`, `document-template`, `gap-analysis` |
| 產出類型 | 產出形式 | `spec`, `pattern`, `report`, `checklist` |

版本資訊記錄於本索引表，不加入資料夾名稱或 SKILL.md header。

---

## 封存規則

觸發封存的條件（任一成立）：
- 此 Skill 對應的工作類型已停止
- 已有新版 Skill 替代
- 超過 1 年未被實際使用

封存流程：
1. 提出計畫，經使用者確認
2. 將 Skill 資料夾移至 `skills/99_封存/`，資料夾名稱加封存日期，例如：`odoo-module-spec-writer_archived_20270101`
3. 更新本索引表，將狀態改為「封存」並記錄日期

---

## 現有 Odoo Skills 搬移策略

### 目前策略：邏輯分類先行，物理搬移暫緩

`odoo-module-spec-writer` 與 `odoo-large-feature-dev` 目前維持根目錄位置。
索引表已標註邏輯分類，待分類子資料夾機制驗證成功後再評估搬移。

### 搬移觸發條件（七項，須全部達成）

1. 已成功建立至少 1 個分類子資料夾內的新 Skill
2. 該新 Skill 已被 Claude / Cowork 正確讀取
3. 該新 Skill 已完成至少 1 次實際任務測試
4. 本 README 索引已能正確記錄分類、路徑、用途、狀態
5. 搬移前已列出所有受影響路徑
6. 搬移前已設計回復方案
7. 使用者明確同意搬移

### 驗證運作機制（依序執行）

```
Step 1  驗證新 Skill 子資料夾可被讀取
Step 2  驗證 Cowork 能透過本 README 判斷該使用哪個 Skill
Step 3  提出 Odoo Skills 搬移前影響評估
Step 4  使用者確認搬移計畫
Step 5  一次只搬一個 Skill，搬移後更新索引
Step 6  搬移後執行真實任務測試
Step 7  測試通過後才評估搬移第二個 Skill
```

### 回復機制

若搬移後出現以下任一狀況，立即執行回復：
- Cowork 找不到已搬移的 Skill
- 能觸發但無法讀取 SKILL.md
- 輸出不符合原 Skill 定義的流程或格式規則

回復步驟：將資料夾搬回原路徑 → 還原索引表 → 回報使用者 → 釐清原因前不再嘗試搬移。

---

## skills-index.md 建立門檻

當 Skill 數量達 **5 個以上**，或跨越 **3 個以上分類**時，建立獨立的 `skills-index.md`。
目前 Skill 數量已達 5 個，且跨越 4 個分類；建議下一步建立獨立 `skills-index.md`，本次先維持 README 兼任索引，避免同一輪異動過大。
