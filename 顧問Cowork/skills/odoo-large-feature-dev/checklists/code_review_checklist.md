# Code Review 檢核（執行階段 8 之前）

## Python
- [ ] 所有 .py 通過 py_compile
- [ ] 所有 class 從 class 開始、縮排正確、可直接貼上
- [ ] 沒有任意修改與本次需求無關的 method 或資料結構

## XML
- [ ] 所有 .xml 通過 ET.parse
- [ ] **沒用 attrs / states**
- [ ] expression 用 invisible="..."、readonly="..."、required="..." 新語法
- [ ] decoration/invisible 用到的欄位都放進 view（可 invisible="1"）

## Model
- [ ] _name 命名一致（dot 分隔）
- [ ] _description 必填
- [ ] _order 適當設定
- [ ] _inherit 從 [\"mail.thread\", \"mail.activity.mixin\"] 加入（業務單據）

## Computed
- [ ] @api.depends 列到「最底層」欄位
- [ ] 跨層 chain 已測過：改最底層欄位 → 最上層是否自動重算
- [ ] store=True 是否合適（read-heavy 設 store=True；計算成本低可不 store）

## Method
- [ ] 按鈕 method 用 action_xxx 命名
- [ ] @api.model_create_multi 用於 create
- [ ] sequence 用 ir.sequence.next_by_code
- [ ] 跨公司操作用 with_company（不要用 sudo）

## Picking
- [ ] action_confirm + action_assign 後直接設 move.quantity + move.picked = True
- [ ] button_validate 用 with_context(skip_immediate=True, skip_backorder=True)
- [ ] picking_type_id 從 settings 取得，缺則 UserError 提示

## Security
- [ ] ir.model.access.csv 對每個 model 都有 group 對應
- [ ] record rule 已覆蓋多公司隔離

## Manifest
- [ ] data 列出所有 xml 與 csv（依依賴順序）
- [ ] depends 完整
- [ ] license 設好

## 中文檔案
- [ ] 含中文的檔案用 bash python3 寫入
- [ ] UTF-8 encoding 一致
- [ ] 所有 string、note、help 用繁體中文
