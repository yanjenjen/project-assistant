# 階段 8：驗證腳本骨架

## 用法
沒 Odoo 環境，靠純 Python mock 驗證邏輯。

## 兩支必備腳本

### 1. test_simulation.py — 單元測試
測試純函數邏輯：

```python
class TestRunner:
    def __init__(self):
        self.results = []
        self.passed = 0
        self.failed = 0

    def assert_equal(self, label, actual, expected, tolerance=0.0001):
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            ok = abs(actual - expected) <= tolerance
        else:
            ok = actual == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        self.results.append((status, label, actual, expected))

    def section(self, title):
        self.results.append(("---", title, "", ""))

    def report(self):
        print(f"通過 {self.passed} / 失敗 {self.failed}")
        for status, label, actual, expected in self.results:
            if status == "---":
                print(f"\n--- {label} ---")
            else:
                mark = "✓" if status == "PASS" else "✗"
                print(f"  {mark} {label}")

t = TestRunner()

# Section 1：公式
t.section("公式")
t.assert_equal("standard", compute_formula(...), 15)

# Section 2：計算邏輯
t.section("計算邏輯")
t.assert_equal("...", ..., ...)

t.report()
```

### 2. test_e2e_flow.py — 完整流程模擬
用 dataclass mock Odoo records，跑端對端流程：

```python
from dataclasses import dataclass, field
from collections import defaultdict

@dataclass
class Product:
    id: int
    name: str

@dataclass
class Company:
    id: int
    name: str

# ... 其他 dataclass

class StockLedger:
    """簡易庫存帳本，驗證庫存軌跡守恆"""
    def __init__(self):
        self.stocks = defaultdict(lambda: defaultdict(float))

    def move(self, src, dst, product, qty):
        self.stocks[src][product] -= qty
        self.stocks[dst][product] += qty

    def qty(self, loc, product):
        return self.stocks[loc][product]

ledger = StockLedger()

# 模擬整條流程
# 1. 設定階段
# 2. 採購到貨
# 3. 入庫分配
# 4. 出貨
# 5. 月底結算

# 驗證點
assert ledger.qty(loc, product) == expected
assert sum(...) == expected_total

print("E2E 全部通過")
```

## 必驗證的不變式

依需求類型勾選：

- **庫存軌跡守恆**：期初 + 採購 = 系統內各位置加總（含 customer）
- **金額一致**：A 公司認列 = B 公司對應認列
- **數量守恆**：A 階段輸入 = B 階段輸出
- **狀態流轉合法**：每個狀態轉換都有對應 method、且不能逆向

## 靜態驗證腳本

```python
import os, py_compile
import xml.etree.ElementTree as ET

errors = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        full = os.path.join(root, f)
        if f.endswith(".py"):
            try:
                py_compile.compile(full, doraise=True)
            except py_compile.PyCompileError as e:
                errors.append(f"PY: {full}: {e}")
        elif f.endswith(".xml"):
            try:
                ET.parse(full)
            except ET.ParseError as e:
                errors.append(f"XML: {full}: {e}")

if errors:
    print("錯誤：")
    for e in errors:
        print(f"  {e}")
else:
    print("全部通過")
```
