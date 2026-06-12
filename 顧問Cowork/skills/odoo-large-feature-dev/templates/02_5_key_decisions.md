# 階段 2：5 大關鍵決策範本

## 用法
階段 1 問完之後，把答案彙整成一個「5 題定案表」，這份是後面所有設計的根。

## 範例表（總部代辦品案例）

| # | 議題 | 選項 | 決定 | 影響範圍 |
|---|---|---|---|---|
| 1 | 家長 partner | 1 個共用 / 每家庭一筆 | 1 個共用 | settings.gp_parent_partner_id |
| 2 | 月底 SO | 全集團 1 張 / 每校 1 張 | 每校 1 張 | settlement.line 設計 |
| 3 | 校區待收款 | A internal invoice / B 自訂 / C 傳票 | A | account_move 跨公司建立 |
| 4 | 校區倉庫架構 | A location 區分 / B warehouse 區分 | A | school_config.location_id |
| 5 | 品項主檔 | 統一 / 各校 | 統一 | product.template + is_gp 標記 |

## 通用 5 大議題清單

- 多公司架構（同公司 / 跨公司）
- 主檔來源（統一 / 分散）
- 結算單據（標準 invoice / 自訂單據）
- 庫存歸屬（warehouse 或 location）
- 客戶建模（1 個共用 partner / 多筆）

## 確認後

- 把這 5 題定案紀錄在文件第一頁
- 後面所有設計變動要回頭看這 5 題是否需要重新討論
