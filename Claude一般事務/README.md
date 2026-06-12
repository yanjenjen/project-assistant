# Claude一般事務 工作區說明

## 定位

外層一般性事務 Claude 工作區。支援日常文書、設計草圖、一般會議摘要、個人工作習慣觀察、AI 指令優化等通用任務。

與 `顧問Cowork\` 平行獨立，不處理 ERP 顧問專案正式交付文件。

---

## 資料夾結構

```
Claude一般事務/
├─ CLAUDE.md          工作區最高規則
├─ README.md          本說明文件
├─ worklog.md         工作紀錄
├─ skills/            Skill 模組區
│  ├─ meeting-summary/    一般會議摘要
│  ├─ design-sketch/      設計草圖 / PPT 架構 / 流程圖
│  ├─ user-research/      使用者工作習慣觀察
│  └─ prompt-engineering/ AI 指令設計 / Prompt 優化
├─ input/             原始輸入資料（暫存）
├─ output/            產出成果
├─ drafts/            草稿區
└─ references/        參考資料
```

---

## Skills 快速索引

| Skill | 主要觸發詞 | 說明 |
|---|---|---|
| `meeting-summary` | `會議記錄：` / `整理這段會議` / `meeting-summary：` | 一般會議摘要、非正式紀要整理 |
| `design-sketch` | `設計草圖：` / `幫我畫流程圖` / `幫我做 PPT 架構` / `design-sketch：` | PPT 架構、流程圖草稿、Demo 展示邏輯 |
| `user-research` | `了解我的習慣：` / `分析我的描述方式` / `user-research：` | 使用者本人工作習慣、學習卡點觀察 |
| `prompt-engineering` | `優化指令：` / `幫我改這個 prompt` / `prompt-engineering：` | AI 指令設計、Prompt 優化、Claude Code 指令 |

---

## 建立日期

2026-06-10
