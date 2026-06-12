# 階段 3：規格回放方法

## 用法
使用者給的每份 Excel / 舊單據都要逐欄看過。**不看就直接設計，會漏業務邏輯**。

## 操作流程

### Step 1：列出所有 sheet
```python
import openpyxl
wb = openpyxl.load_workbook(f, data_only=True)
for sn in wb.sheetnames:
    ws = wb[sn]
    print(f"  - '{sn}': {ws.max_row} rows x {ws.max_column} cols")
```

### Step 2：每個關鍵 sheet 讀前 30 行
```python
ws = wb['某 sheet']
for i, row in enumerate(ws.iter_rows(values_only=True, max_row=30)):
    print(i+1, row)
```

### Step 3：標出欄位結構（誰填、什麼公式）
範例觀察：

| 欄位 | 來源 | 性質 |
|---|---|---|
| 在校生去年訂購量 | 系統 | **已統整數據，勿自行調整** |
| 新生問卷 | 各校填 | **各校填入** |
| 待招缺額 | 各校填（建議尺寸：幼幼2-4、小4-6、中6+） | **各校填入** |
| 加訂需求 = F × 1.5 | 公式 | 自動 |
| 需求量 = G+H+I | 公式 | 自動 |
| 庫存量 | 各校填（人工點貨） | **各校填入** |
| 下單量 = 需求量 − 庫存量 | 公式 | 自動 |

### Step 4：列「原設計 vs Excel 觀察」對照表

| 原設計 | 現實狀況 | 需要調整 |
|---|---|---|
| 「各校填需求量」 | 需求量是公式算的，校只填部分 | 拆開「校填欄位」與「公式欄位」 |
| 沒有「歷史銷售」概念 | 公式吃這個 | 加 historical_sales model |
| 沒有跨校調貨 | 彙整時常發生 | 加 transfer model |
| 沒有批發補量 | 統採會湊整批 | 加 manual 欄位 |
| 沒有總部備用 | 採購表都有 | 加 hq_reserve 欄位 |
| 沒有追加版本 | 中途會補 | 用 is_supplement 標記 |

## 不可

- 跳過此步直接做設計
- 只看一個 sheet 就下結論
- 忽略 Excel 上紅字、附註、特殊規則
