# 階段 5：技術選型問題清單

## Odoo 17 常見議題與推薦

### Picking 自動完成
| 選項 | 說明 | 推薦 |
|---|---|---|
| A 純 stock.move | 不掛 picking，valuation 與追溯薄弱 | ✗ |
| **B 自動建 picking + auto validate** | 標準慣例，使用者只按一鍵 | ✓ |
| C draft 讓人按 validate | 多一步、容易忘 | ✗ |

實作要點：
```python
picking = self.env["stock.picking"].create({...})
self.env["stock.move"].create({..., picking_id: picking.id})
picking.action_confirm()
picking.action_assign()
# Odoo 17：移除 quantity_done，改用 stock.move.quantity
for move in picking.move_ids:
    move.quantity = move.product_uom_qty
    move.picked = True
picking.with_context(skip_immediate=True, skip_backorder=True).button_validate()
```

### 倉庫架構
| 情境 | 推薦 |
|---|---|
| SO 出貨來源因角色不同 | warehouse |
| 只是位置區隔（同公司） | location |

### 跨公司 invoice
| 選項 | 推薦 |
|---|---|
| A 依賴 inter_company_rules | 看環境 |
| **B 模組自己建兩張** | 不依賴外部，更可控 |

實作要點：
```python
inv = self.env["account.move"].with_company(hq_company).create({
    "move_type": "out_invoice",
    "company_id": hq_company.id,
    "partner_id": school_partner.id,
    ...
})
inv.action_post()

bill = self.env["account.move"].with_company(school_company).create({
    "move_type": "in_invoice",
    "company_id": school_company.id,
    "partner_id": hq_partner.id,
    ...
})
bill.action_post()
```

注意：partner 的 `company_id` 必須設為 `False`（共用）才不會卡住。

### Odoo 17 View 規則
- ✗ 不用 `attrs`、`states`
- ✓ `invisible="state == 'draft'"`
- ✓ `readonly="state in ('done', 'cancelled')"`
- expression 用到的欄位即使不顯示也要放進 view（`invisible="1"`）

### Wizard 開啟
```python
# ✓ 標準作法
return {
    "type": "ir.actions.act_window",
    "name": "...",
    "res_model": "...",
    "view_mode": "form",
    "target": "new",
    "context": {"default_xxx": self.id},
}

# ✗ 不要這樣
action = self.env.ref("module.action_xxx").read()[0]
action["context"] = {...}
```

### Computed depends 鏈
- depends 必須列到「最底層」欄位
- 跨層 computed（如：A → B → C），A 的 depends 要列 C 的所有觸發欄位
- 寫完後測一次：改 C → A 是否自動重算？

### Sequence 用法
```python
# 一般序號
vals["name"] = self.env["ir.sequence"].next_by_code("xxx.code") or "/"

# 含年月的序號（用 with_context）
seq = self.env["ir.sequence"].with_context(
    ir_sequence_date=date(year, month, 1)
).next_by_code("xxx.code")
```

## 不可

- 用 Odoo 16 之前的舊 API（attrs / states / quantity_done 等）
- 自己拼字串當序號（破壞 sequence 邏輯）
- 沒用 with_company 處理跨公司操作
