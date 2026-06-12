# Claude一般事務 工作區規則

## 一、工作區定位

本工作區為「外層一般性事務 Claude」，定位如下：

- 支援日常文書、PPT 架構、設計草圖、流程圖、一般會議摘要、個人工作習慣觀察、AI 指令優化等通用任務
- **不是 ERP 顧問專案工作區**，不處理 ERP 導入分析、規格書、制度萃取、正式顧問交付文件
- 與 `顧問Cowork\` 工作區平行獨立，不得混用

---

## 二、與 ERP Cowork 的邊界

| 事項 | 本工作區（Claude一般事務） | ERP Cowork（顧問Cowork） |
|---|---|---|
| 定位 | 外層通用事務 | ERP 顧問專案 |
| 正式交付文件 | ❌ 不產出 | ✅ 依 CLAUDE.md 規則產出 |
| 會議紀要 | ✅ 一般口語摘要 / 非正式紀要 | ✅ 正式輔導備忘錄（erp-meeting-record-writer，未來） |
| ERP 規格書 / 制度萃取 | ❌ 不處理 | ✅ 處理 |
| Skill 觸發 | 本工作區 4 個 Skill | ERP Cowork 內層 5 個 Skill + 平台層 Skills |

**邊界原則：**
- 本工作區 Skills 輸出不得直接作為 ERP 正式交付文件
- ERP 正式分析、規格、制度文件請移至 `顧問Cowork\` 工作區處理

---

## 三、檔案操作規則

- 凡涉及建立、修改、刪除、搬移、重新命名檔案，必須先提出計畫，等使用者確認後再執行
- 資料不足時標示「待補資料」或「需確認」，不得自行推測
- 不得修改 `顧問Cowork\` 內任何檔案

---

## 四、Skills

| Skill | 定位 | 主要觸發詞 |
|---|---|---|
| `meeting-summary` | 一般會議摘要 / 非正式紀要 | `會議記錄：` / `meeting-summary：` |
| `design-sketch` | PPT 架構 / 流程圖 / Demo 草圖 | `設計草圖：` / `design-sketch：` |
| `user-research` | 使用者本人工作習慣觀察 | `了解我的習慣：` / `user-research：` |
| `prompt-engineering` | AI 指令設計 / Prompt 優化 | `優化指令：` / `prompt-engineering：` |

---

## 五、禁止事項

- 禁止未經確認就修改、刪除、搬移、重新命名檔案
- 禁止將本工作區輸出直接作為 ERP 正式交付文件
- 禁止修改 `顧問Cowork\` 內任何檔案
- 禁止啟用 hooks / agents
