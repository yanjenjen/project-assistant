---
name: odoo-large-feature-dev
description: Odoo 17 大型業務需求開發完整流程（9 階段方法論）。當使用者提出涉及多模組、多角色、多單據、多流程的「大需求」時，立即使用此 skill。觸發詞包括「集團XX流程」、「公司XX結算」、「跨公司XX」、「整個系統」、「這是個大需求」、「幫我開發一個OO模組」、「OO代辦品/採購/簽核/結算流程」、或使用者貼上一段長業務需求並描述多階段業務動線。也適用於：需求文件含 Excel 規格表、跨多個 model 開發、需設計新 wizard、需設計新 picking 流程、需處理多公司 (multi-company) 架構、需設計需求估算公式、需設計庫存軌跡管理時。本 skill 提供從需求初探到交付的完整節奏，含必做步驟、產物清單、技術選型範例、驗證腳本骨架。
---

# Odoo 17 大型需求開發流程

## 何時使用此 skill

凡是符合下列任一條件，就走這套流程，不要省步驟：

- 需求文字超過 5 行、涉及 3 個以上單據或角色
- 使用者貼上 Excel 規格表、現行表單、舊系統截圖
- 跨多個 model、跨多公司、含會計處理或庫存軌跡
- 預估開發超過 1 天、Python + XML 合計超過 1,500 行
- 需要設計新 wizard、新 picking type、新計算公式

反之，**單純的 view 微調、一個欄位的新增、一條 method 的修補不適用本流程**，依 CLAUDE.md 標準 5 步流程即可。

## 核心原則（貫穿全程）

1. **先講故事再進技術** — 沒對齊業務語言前不進 model 設計
2. **規格回放** — 使用者給的 Excel / 舊單據要逐欄看過，不靠想像
3. **該系統化的系統化、該留人工的留人工** — 每次都會變的東西就留欄位給人填
4. **技術選型優先看 odoo 標準慣例** — 不為了「乾淨」捨棄 odoo 的標準追溯
5. **每環節確認關聯再下筆** — 每一塊完成都打勾，task list 隨時更新
6. **沒環境也要驗證** — 抽純邏輯做 Python mock 跑 E2E
7. **交付不只程式還有可重現的測試資料** — 商品、partner、歷史銷售匯入檔
8. **永遠用繁體中文** — 註解、欄位 string、文件、變數命名以 yc_ 為前綴
9. **採最小修改原則** — 既有模組擴充用 inherit + xpath，不重貼整段

---

## 9 階段流程

依以下順序執行。**前一階段未完成不進下一階段**。

### 階段 1：需求初探（白話拆解）

**目的**：把使用者的自然語言敘述變成系統能理解的「角色 / 動作 / 單據 / 結果」。

**必做**：
- 把整個故事拆成 N 個業務階段（A → B → C → ...），每階段標出：誰做、做什麼、產出什麼、什麼是人工點
- 整理「資料流總表」（單據名 / 建立者 / 對象 / 性質）
- 列出 4~6 個關鍵問題（足以決定系統架構的問題）

**產物**：
- 流程脈絡圖（文字版即可）
- 單據資料流總表
- 待釐清問題清單

**不可**：
- 直接跳到 model 設計
- 自行假設「應該」「大概」「通常」的業務規則

**範本檔**：`templates/01_requirement_clarification_questions.md`

---

### 階段 2：5 大關鍵收斂

**目的**：消除影響架構的歧義。**5 題不答完，不進下一階段**。

**典型 5 題**（依需求類型微調）：
1. 多公司架構？（同公司 / 跨公司）
2. 主檔來源？（統一主檔 / 各分公司獨立）
3. 會計處理方式？（內部 invoice / 傳票 / 自訂單據）
4. 庫存歸屬？（用 warehouse / 用 location）
5. 客戶/廠商建模？（1 個共用 partner / 多筆 partner）

**產物**：5 題確認紀錄（後面變更要回來修這份）

**範本檔**：`templates/02_5_key_decisions.md`

---

### 階段 3：規格回放（最容易被跳過、最不該跳過）

**目的**：從使用者給的 Excel / 舊單據挖出**真實業務邏輯**，而非用想像建模。

**必做**：
- 用 openpyxl 讀完每個關鍵 sheet 的前 30 列
- 列出獨特品名、欄位結構、計算公式（看 Excel 上的公式或附註）
- 標出原設計**漏掉**的業務邏輯

**典型發現**：
- 需求量是公式估算的（不是直接填）
- 同種品項用不同公式
- 跨校 / 跨單位的調貨機制
- 批發/合單量補齊邏輯
- 中途追加版本
- 教師 vs 學生分流

**產物**：「原設計 vs Excel 觀察」對照表（指出多少項是要追加的）

**範本檔**：`templates/03_spec_replay_method.md`

---

### 階段 4：細節再次收斂

**目的**：把階段 3 挖出來的細節，逐項問清楚。

**典型細節**：
- 計算公式：固定 / 可設定？
- 歷史資料：從系統反查 / CSV 匯入 / 兩者皆要？
- 中介流程（如調撥）：與主單耦合 / 獨立 model？
- 異常處理：規則內 / 規則外（留人工）？
- 追加變更：新單據 / 改既有單據？
- 角色/類別分流：欄位標記 / 獨立 model？

**關鍵問句**：「這個情境，要做進系統還是留人工？」每一個都要使用者明確回答。

**範本檔**：`templates/04_detail_resolution.md`

---

### 階段 5：技術選型（最容易踩雷）

**目的**：選定 odoo 慣例做法，避免後期改不動。

**典型議題與推薦**：

| 議題 | 選項 | 推薦 | 理由 |
|---|---|---|---|
| picking 自動完成 | A 純 stock.move / B 自動建 picking + auto validate / C 建 draft 讓人點 | **B** | A 失去 odoo 標準追溯；C 多一步 |
| 倉庫架構 | A warehouse / B location | 依需求 | 若 SO 出貨來源不一致用 warehouse；若只是區隔位置用 location |
| 跨公司 invoice | A 模組自建兩張 / B 依賴 inter_company_rules | A | Community 預設無 IC；自建更可控 |
| 自動 SO 開立 | A 認列營收 / B 僅作紀錄不 confirm | 看會計設計 | 避免重複認列 |
| 多公司 partner | A 共用 (company_id=False) / B 各 company 一份 | A | 共用簡單，跨公司操作不會卡 |
| 序號生成 | A ir.sequence / B 自己拼字串 | A | 標準作法 |

**特別注意**：
- Odoo 17 移除 `attrs` 與 `states`，view expression 用 `invisible="state == 'draft'"` 新語法
- decoration/invisible expression 用到的欄位必須放進 view（可設 invisible="1"）
- Wizard 開啟方式用回傳 `act_window` dict
- Odoo 17 `stock.move.quantity` 已是已完成量，設好後直接 `button_validate`
- 跨公司操作用 `with_company(c)` 而非 `sudo()`

**範本檔**：`templates/05_tech_decisions.md`

---

### 階段 6：執行計畫定稿

**目的**：在動程式前，把「會寫什麼檔」「依什麼順序」全部攤開，給使用者最後一次 OK。

**必做**：
- 列出所有 Model（自定 + 繼承）、所有 View、Data、Security、Wizard
- 標出依賴關係與開發順序
- 給出模組資料夾結構圖
- 明確問使用者：「分階段交付 or 一次做完」「最後調整？」

**產物**：執行計畫表 + 目錄結構樹

**動工前自我確認**：
- 是否已理解業務情境？
- 是否已比對既有 odoo 原生 + yc_* 公共模組？
- 是否處理多公司影響（company_id / record rule / allowed_company_ids）？
- 是否說明「新建模組 or 擴充既有」並取得確認？

**範本檔**：`templates/06_execution_plan_template.md`

---

### 階段 7：開發實作

**目的**：依執行計畫的順序逐塊完成，task list 隨時更新。

**標準順序**：
```
1. 模組骨架（manifest / __init__ / security 群組）
2. security（提早建，避免後續安裝錯）
3. data（sequence / picking type 占位 / 預設值）
4. 設定類 Model（簡單的先做）
5. 設定類 View + menu
6. 業務 Model（依依賴順序）
7. 業務 View
8. Picking 自動化邏輯（最易踩雷）
9. 跨公司 / 跨模組接軌
10. menu 整合
11. 靜態驗證
```

**寫程式的鐵則**：
- **含中文字符的檔案一律用 bash python3 寫入**，禁用 Write/Edit 直接操作
  ```bash
  python3 - << 'EOF'
  content = """..."""
  with open("/絕對路徑/檔名", "w", encoding="utf-8") as f:
      f.write(content)
  EOF
  ```
- 從 `class` 開始生成，縮排正確，可直接貼上
- 沿用既有架構，採最小修改原則
- View 用 Odoo 17 新語法（不用 attrs/states）
- 沿用 xpath inheritance，不重貼原始節點

**驗收標準（每塊完成必過）**：
- Python `py_compile` 無錯
- XML `ET.parse` 無錯
- manifest 引用檔案皆存在
- access.csv 對應 model 皆存在

**範本檔**：`templates/07_development_order.md`

---

### 階段 8：驗證（沒環境也要做）

**目的**：在沒有 Odoo dev 環境的情況下，確認邏輯正確。

**必做**：
1. **靜態驗證**：py_compile + xml ParseError + manifest 引用檢查 + access.csv 對應檢查
2. **單元測試**：把純函數邏輯（公式、計算、比例分配）抽出來測
3. **E2E 模擬**：用 Python mock 跑完整資料流，驗證**庫存軌跡守恆**等不變式
4. **Code review**：手動檢查 depends 鏈、跨公司 with_company、picking validate 邏輯

**關鍵不變式（依需求類型微調）**：
- 庫存軌跡：期初 + 採購 = 系統內各位置加總（含 customer）
- 金額一致：A 認列 = B 對應認列
- 數量守恆：A 階段輸入 = B 階段輸出

**產物**：兩支測試腳本 + 驗證結果表

**範本檔**：`templates/08_verification_scripts.md`

---

### 階段 9：交付

**目的**：交付的不只是程式，還要讓使用者能立刻測。

**必交付物**：

| 類別 | 內容 |
|---|---|
| 程式 | 放到當日日期資料夾 + 同步「最新版本/」 |
| 測試流程文件 | .docx 含 TC + E2E + 例外 + 故障排除 + 驗收簽核 |
| 匯入檔 | 商品主檔 xlsx、歷史資料 csv、設定資料 xlsx |
| 模擬測試腳本 | .py 用於驗證邏輯正確 |
| 已知限制清單 | 在文件最後標出「程式正確 ≠ 實際能跑」的潛在風險點 |

**範本檔**：`templates/09_delivery_checklist.md`

---

## 工作節奏建議

| 階段 | 估時占比 | 工具 |
|---|---|---|
| 1～2 | 10% | AskUserQuestion + 表格整理 |
| 3 | 15% | openpyxl 讀 Excel + 對照表 |
| 4～5 | 10% | AskUserQuestion |
| 6 | 5% | 表格 + 樹狀圖 |
| 7 | 40% | bash python3 寫入 |
| 8 | 15% | py_compile + 自寫 mock test |
| 9 | 5% | python-docx + openpyxl |

---

## 常見陷阱

1. **跳階段 3**：以為自己懂業務，沒看 Excel 就做 — 結果挖出來的需求是漏的
2. **混用 AskUserQuestion 與 TaskCreate**：先用 AskUserQuestion 對齊需求，再用 TaskCreate 拆任務
3. **沒在動工前最後一次給使用者 OK**：寫了一堆後使用者說「方向不對」
4. **忽略多公司**：直接寫 default_company，跨公司 invoice 過帳會失敗
5. **picking validate 用舊版 API**：Odoo 17 已改為 `move.quantity` + `move.picked = True`
6. **depends 鏈漏列**：computed 不會自動連動，要列到最底層欄位
7. **直接用 Write 工具寫含中文檔**：可能編碼錯誤，要用 bash python3
8. **以為靜態驗證通過 = 實際能跑**：要在文件最後標出「程式正確 ≠ 環境能跑」的風險

---

## 範本檔索引

| 範本 | 對應階段 |
|---|---|
| `templates/01_requirement_clarification_questions.md` | 階段 1 |
| `templates/02_5_key_decisions.md` | 階段 2 |
| `templates/03_spec_replay_method.md` | 階段 3 |
| `templates/04_detail_resolution.md` | 階段 4 |
| `templates/05_tech_decisions.md` | 階段 5 |
| `templates/06_execution_plan_template.md` | 階段 6 |
| `templates/07_development_order.md` | 階段 7 |
| `templates/08_verification_scripts.md` | 階段 8 |
| `templates/09_delivery_checklist.md` | 階段 9 |
| `checklists/pre_dev_checklist.md` | 動工前 |
| `checklists/code_review_checklist.md` | 寫完後 |
| `checklists/final_delivery_checklist.md` | 交付前 |
| `examples/yc_group_purchase_case.md` | 完整範例（總部代辦品採購） |
