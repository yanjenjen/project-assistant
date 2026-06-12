# Claude Code 指令速查卡

> ⚠️ **適用範圍說明：本文件所有 `/ecc:xxx` 指令僅適用於 Claude Code CLI（終端機）環境。**
> 在 Cowork 對話介面中，這些指令**無法直接呼叫**，效果也不會生效。
> 若需在 Cowork 中執行相同目的的任務，請改用：
> （1）Cowork 自然語言描述任務需求，或
> （2）已建立的對應 Cowork Skill（如 `project-fast-delivery-assistant`）。

> 在終端機輸入 `claude` 進入 session 後，使用以下指令。

---

## 常用開發流程指令

| 指令 | 用途 | 什麼時候用 |
|------|------|-----------|
| `/ecc:plan` | 任務規劃 | **開始任何新任務前先跑這個** |
| `/ecc:code-review` | 程式碼審查 | 寫完一段程式後 |
| `/ecc:tdd-workflow` | TDD 開發流程 | 要寫測試驅動開發時 |
| `/ecc:security-scan` | 安全性掃描 | 交付前檢查 |
| `/ecc:e2e` | End-to-end 測試 | 整合測試 |
| `/ecc:build-fix` | 修復 build 錯誤 | CI/build 失敗時 |
| `/reload-plugins` | 重新載入 plugins | 安裝新 plugin 後 |

---

## ERP 顧問常用場景對照

| 你想做的事 | 用哪個 |
|-----------|--------|
| Odoo 客製化模組開發 | `claude` → `/ecc:plan` 先規劃 |
| 資料匯入腳本（CSV/Excel → Odoo） | `claude` → 直接描述需求 |
| API 串接規格實作 | `claude` → `/ecc:plan` |
| 自動化測試腳本 | `claude` → `/ecc:tdd-workflow` |
| 程式碼交付前審查 | `claude` → `/ecc:code-review` |

---

## 起手式（每次開新專案）

```bash
# 1. 進入專案資料夾
cd C:\你的專案資料夾

# 2. 啟動 Claude Code
claude

# 3. 開始規劃
/ecc:plan
```

---

## Hooks 自動生效的保護機制（不用手動觸發）

- ✅ 存檔後自動 format / lint
- ✅ 危險指令（rm -rf 等）自動擋截
- ✅ Session 開始時自動載入狀態

---

## 這裡（Cowork）vs 終端機（Claude Code）

| | Cowork | Claude Code CLI |
|--|--------|----------------|
| 進入方式 | 直接對話 | 終端機輸入 `claude` |
| 適合 | 顧問文件、分析、SOP、Excel/Word | 程式開發、腳本、自動化 |
| 觸發方式 | 自然語言 | `/ecc:xxx` slash command |
