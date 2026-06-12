# 階段 7：開發實作順序

## 標準順序（依依賴關係）

```
1. 模組骨架
   ├── __manifest__.py（先寫 depends，data 暫時放空）
   ├── __init__.py（含 models / wizard）
   └── 建立 models/views/data/security/wizard 5 個資料夾

2. security
   ├── ir.model.access.csv（先建好骨架，後面填）
   └── yc_xxx_security.xml（含 group + record rule）

3. data
   ├── ir_sequence_data.xml
   ├── stock_picking_type_data.xml（若有）
   └── 其他預設值

4. 設定類 Model（不依賴其他自定 model）
   ├── product 繼承
   ├── res.config.settings 繼承
   ├── xxx.config（校區/分公司對應）
   └── xxx.formula（公式定義）

5. 設定類 View + menu

6. 業務 Model（依依賴順序）
   ├── xxx.request + line
   ├── xxx.consolidation + line（依賴 request）
   ├── xxx.transfer + line（彙整單上有快捷入口）
   ├── xxx.delivery + line
   └── xxx.settlement + line

7. 業務 View

8. Picking 自動化邏輯
   ├── transfer 自動 done
   ├── delivery 自動 done
   └── settlement 自動產出 picking + invoice

9. 跨公司 / 跨模組接軌
   ├── PurchaseOrder 擴充
   ├── StockPicking 擴充
   └── AccountMove 擴充

10. 整合測試前的靜態驗證
```

## 寫程式的鐵則

### 含中文字符檔案的寫入
**必用 bash python3，禁用 Write/Edit**：
```bash
python3 - << 'EOF'
content = """完整內容..."""
with open("/絕對路徑/檔名", "w", encoding="utf-8") as f:
    f.write(content)
EOF
```

### 縮排
- Python 4 空格
- XML 4 空格
- 從 class 開始生成，可直接貼上

### 既有模組擴充
- 用 inherit + xpath，不重貼整段
- 採最小修改原則，不任意動既有 method

### Odoo 17 view 規則
- 不用 attrs / states
- expression 用 invisible="state == 'draft'"
- decoration 用到的欄位放進 view（可 invisible="1"）

### Wizard
- 直接 return act_window dict
- 不用 env.ref().read()[0]

## 每塊完成的驗收

寫完一塊就跑：
```python
import py_compile
py_compile.compile("xxx.py", doraise=True)

import xml.etree.ElementTree as ET
ET.parse("xxx.xml")
```

## 不可

- 一次寫太多檔（一個 bash python3 寫超過 5 個檔），會增加 debug 難度
- 跳順序（如先寫 view 再寫 model），會 reference error
- 忽略 access.csv（安裝時會 access denied）
