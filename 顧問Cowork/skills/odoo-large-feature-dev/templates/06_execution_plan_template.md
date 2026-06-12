# 階段 6：執行計畫範本

## 用法
動工前最後一份對齊文件。給使用者看完拿到 OK 再開工。

## 執行計畫範本

### 模組基本
- **模組命名**：`yc_xxx`
- **依賴**：`base, product, stock, purchase, sale_management, account`
- **獨立或擴充？**：[獨立模組 / 擴充既有模組]

### Model 清單
| # | Model | 用途 |
|---|---|---|
| 1 | `xxx.template`（繼承） | 標註... |
| 2 | `yc.xxx.config` | 設定... |
| 3 | `yc.xxx.request` + `.line` | 業務單據 |
| ... | | |

### View 清單
- `xxx_views.xml`：tree + form + search
- `yyy_views.xml`：...
- `menu.xml`：應用首頁 + 一級 menu

### Data
- sequence
- picking type（如有）
- 預設值

### Security
- group：A 使用者 / B 管理員
- access.csv
- record rule（如多公司）

### 模組目錄結構
```
yc_xxx/
├── __init__.py
├── __manifest__.py
├── data/
│   ├── ir_sequence_data.xml
│   └── ...
├── security/
│   ├── ir.model.access.csv
│   └── yc_xxx_security.xml
├── models/
│   ├── __init__.py
│   └── ...
├── views/
│   └── ...
└── wizard/
    └── ...
```

### 開發順序（分階段交付選項）
| 階段 | 內容 | 可驗收項 |
|---|---|---|
| 1 | 基礎設定（含 product / settings / config / formula） | 設定畫面跑得起來 |
| 2 | 業務單據（含主流程） | 主流程能跑 |
| 3 | 接軌與分配 | 與既有模組接通 |
| 4 | 結算/報表 | 完整流程 |

### 給使用者選的最後 3 題
1. 交付方式：分階段 / 一次做完？
2. 第一階段先動工？
3. 任何最後調整？

## 不可

- 沒給使用者最後 OK 就動程式
- 模組命名隨意（必須有 yc_ 前綴）
- 跳過「擴充 or 新建」的決策
