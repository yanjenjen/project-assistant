# 建大下單平台｜拆單邏輯 程式碼軌跡

> 整理日期：2026-08-03
> 用途：說明「經銷商結帳時，系統如何把購物車拆成多張建大訂單（母子單）」的實際程式邏輯
> 程式碼位置：`kenda-local\stack\odoo\addons\kenda_platform\`（本機開發環境的真正原始碼，非前端 minified bundle）

---

## 一句話總結

**拆單 = 先看經銷商所在地區決不決定要拆 → 決定要拆的話，再依商品的「包裝部門代號」分組 → 每一組各自成一張子單、各自取號，全部掛在同一個母單（PO 單號）底下。**

---

## 進入點

- API：`POST /api/cart/checkout`
- 檔案：`controllers/cart.py`，`KendaCartController.checkout`（第 83 行）
- 觸發時機：經銷商在前台結帳（購物車 → 送出訂單）

---

## 拆單規則（程式內註解原文，第 6～12 行）

```
判斷一：dealer.area_code in SPLIT_REGIONS（NMR=台灣, VVV=越南內銷）→ 需拆單
        其他地區 → 全部進同一張單，不拆
判斷二（SPLIT_REGIONS 才執行）：
        以「成代對應的包裝部門代號(pack_dept_code)」為鍵
        相同 pack_dept_code → 同一張子單（同倉出貨）
        不同 pack_dept_code → 各自一張子單
```

## 步驟拆解

### 1. 判斷一：地區是否要拆單（`cart.py` 第 22、97 行）

```python
SPLIT_REGIONS = {'NMR', 'VVV'}  # NMR=台灣, VVV=越南內銷
use_region_split = (dealer.area_code or '') in SPLIT_REGIONS
```

- 經銷商 `area_code` 是 `NMR`（台灣）或 `VVV`（越南內銷）→ 才會進入拆單流程
- 其他地區的經銷商 → 購物車裡所有商品，不論倉別，全部合併成同一張訂單

### 2. 判斷二：依包裝部門代號分組（第 102～118 行）

```python
groups = {}
for l in lines_data:
    ...
    ql = QL.search([('quote_line_no', '=', qln)], limit=1)
    item = {..., 'pack_dept_code': ql.product_id.pack_dept_code or ''}
    key = item['pack_dept_code'] if use_region_split else '__single__'
    groups.setdefault(key, []).append(item)
```

- 逐一比對購物車每一行商品對應的報價行（`kenda.quote.line`），取得該商品的 `pack_dept_code`（包裝部門代號，代表出貨倉別）
- 若判斷一結果是「要拆」：用 `pack_dept_code` 當分組鍵，代號相同的商品歸同一組（同倉出貨、同一張子單）
- 若判斷一結果是「不拆」：全部商品用固定鍵 `'__single__'`，等於只有一組

### 3. 建立母單（第 120～126 行）

```python
po_no = _next_seq(env, 'po', 'PO', 6)
grp = env['kenda.order.group'].sudo().create({...})
```

- 不論拆成幾組，先建立一張 `kenda.order.group`（訂單群組 = 母單），取得一組 `po_no`（母單號）
- 母單記錄客戶希望交期、指配地點等「整批共用」的資訊

### 4. 每一組 → 一張子單，各自取號（第 128～163 行）

```python
for key, items in groups.items():
    plat_no = _next_seq(env, 'plat', '', 6)   # 平台單號
    erp_no  = _next_seq(env, 'erp', 'P', 6)   # ERP 單號
    order = env['kenda.order'].sudo().create({
        'group_id': grp.id,                    # 掛在同一個母單底下
        'split_pack_code': pack_dept,          # 記錄這張子單是哪個包裝部門/倉別
        ...
    })
```

- 每個分組各自建立一張 `kenda.order`（子單），各自取得獨立的平台單號、ERP 單號
- 子單透過 `group_id` 掛回同一個母單（`kenda.order.group`）
- 子單上的 `split_pack_code` 欄位記錄該子單對應的包裝部門代號，方便追蹤是依哪個規則拆出來的

### 5. 同步 Mock ERP（第 156～163 行，best-effort）

```python
try:
    erp_client.create_order(env, {...})
except Exception:
    pass
```

- 每建立一張子單，同步呼叫 mock ERP 介接留同步紀錄
- 失敗不會擋住主流程（訂單照樣成立），單純記錄同步狀態

### 6. 回傳結果（第 165～172 行）

- 母單狀態改為 `pushed`
- API 回傳：母單號（`po_no`）、拆出幾張子單（`order_count`）、每張子單的完整明細

---

## 相關資料表欄位

檔案：`models/kenda_order.py`

| 欄位 | 所在 Model | 說明 |
|---|---|---|
| `group_id` | `kenda.order` | 子單指向所屬母單 |
| `order_ids` | `kenda.order.group` | 母單的一對多子單清單（第 94 行） |
| `order_count` | `kenda.order.group` | 拆單數，compute 欄位（第 95 行） |
| `split_purpose` | `kenda.order` | 拆分-報價用途（一般/促銷/呆貨） |
| `split_quote_no` | `kenda.order` | 拆分-報價單號 |
| `split_has_waste` | `kenda.order` | 拆分-是否含廢胎費 |
| `split_pack_code` | `kenda.order` | 拆分-包裝代號（即結帳時分組用的 `pack_dept_code`） |

> 註：`split_purpose` / `split_quote_no` / `split_has_waste` 這三個欄位在目前 `checkout` 程式碼裡是預留欄位（建立子單時寫入空值），目前實際生效的拆單鍵只有 `split_pack_code`（包裝部門代號）。若之後要依「報價用途」「是否含廢胎費」等條件也拆單，程式邏輯需要再擴充。

---

## 備註

- 本文件對應的程式碼是**本機開發環境**（`kenda-local\stack\odoo\addons\kenda_platform\`）現況，尚未逐行核對客戶正式站（aiuptop.com）程式碼是否完全一致。
- 前端（React SPA）沒有保留原始碼，只有編譯後的 minified bundle，因此拆單邏輯的唯一可讀原始碼在後端（Odoo addon）這一份。
