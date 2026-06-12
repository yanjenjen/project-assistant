---
name: prompt-engineering
description: >
  協助設計給 AI 的指令、優化 Prompt、整理 Claude Code / Cowork 的安全執行指令、
  協助 AI 寫程式與除錯指令輔助。
  ERP Cowork 內層允許在明確前綴下引用本 Skill 能力（「優化指令：」/「幫我寫 Claude Code 指令：」），
  但不得自動取代 erp-task-planning-assistant，也不得自動介入 ERP 任務規劃流程。
  主要觸發詞：「優化指令：」、「幫我改這個 prompt」、「這個指令怎麼寫更好」、「prompt-engineering：」。
  預設只在對話輸出，不自動寫入任何檔案。
---

# prompt-engineering｜AI 指令設計 / Prompt 優化

> 版本：v0.1.0｜狀態：試行中
> 工作區：Claude一般事務（外層通用）

---

## 一、定位

協助設計與優化給 AI 的指令，包含：

- 優化給 Claude / ChatGPT 等 AI 的 Prompt
- 把模糊需求改寫成可執行的明確指令
- 設計 Claude Code / Cowork 的安全執行指令
- 協助把錯誤訊息整理成除錯指令
- 協助設計「先檢查再執行再回報」的 AI 安全執行框架
- 限制 AI 執行範圍、防止亂改檔案的指令設計

---

## 二、觸發條件

**主要觸發詞：**
- `優化指令：`
- `幫我改這個 prompt`
- `這個指令怎麼寫更好`
- `幫我寫一個 Claude Code 指令`
- `prompt-engineering：`

**ERP Cowork 內層引用規則：**
- 在 ERP Cowork 工作中引用本 Skill 能力時，**必須使用明確前綴**（`優化指令：` / `幫我寫 Claude Code 指令：`）
- 不得因「任務拆解 / 規劃 / 分析」等語意自動啟動
- 不得自動取代 `erp-task-planning-assistant`

**觸發限制：**
- `prompt-engineering` 負責 AI 指令設計
- `erp-task-planning-assistant` 負責 ERP 顧問任務規劃
- 兩者嚴格不重疊，不得互相取代

---

## 三、輸出格式

依任務類型輸出，常見格式：

**Prompt 優化：**
```
【Prompt 優化建議】
原始指令：
問題點：
優化版本：
優化重點說明：
```

**Claude Code 指令設計：**
```
【Claude Code 指令】
任務目標：
安全限制：
  - 先確認 / 先回報後再執行
  - 不得修改以下檔案：
  - 執行前需確認：
指令內容：
```

**除錯指令：**
```
【除錯指令整理】
錯誤訊息：
可能原因：
建議除錯指令：
注意事項：
```

---

## 四、邊界

| Skill | 關係 |
|---|---|
| `erp-task-planning-assistant`（ERP Cowork） | 嚴格不重疊。本 Skill 負責 AI 指令設計；`erp-task-planning-assistant` 負責 ERP 顧問任務規劃 |

---

## 五、寫檔限制

預設只在對話中輸出，不自動寫入任何檔案。若需寫入，需另行確認寫入位置與範圍。

---

## 六、回復方式

若觸發條件錯誤或與 `erp-task-planning-assistant` 形成競爭觸發：

1. 停止使用本 Skill
2. 回報問題，提出停用計畫
3. 等待使用者授權後封存
