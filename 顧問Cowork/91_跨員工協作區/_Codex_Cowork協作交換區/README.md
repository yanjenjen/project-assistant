# Codex / Cowork 協作交換區

本資料夾用於降低使用者在 Codex 與 Cowork 之間手動複製貼上的負擔。

---

## 使用前提

只有在 Cowork 與 Codex 都能讀寫本工作區檔案時，才使用此交換區。

若 Cowork 只能使用網頁對話，無法直接讀寫本機檔案，則仍需由使用者手動貼上摘要或上傳檔案。

---

## 固定流程

1. Codex 可先將任務指令寫入 `00_Codex_to_Cowork_任務指令.md`
2. Cowork 讀取任務指令後，將操作計畫寫入 `01_Cowork_to_Codex_操作計畫.md`
3. 使用者請 Codex 讀取交換區並審核
4. Codex 將審核意見寫入 `02_Codex_to_Cowork_審核意見.md`
5. 使用者請 Cowork 讀取 Codex 審核意見並執行
6. Cowork 將執行結果寫入 `03_Cowork_to_Codex_執行結果.md`
7. 使用者請 Codex 讀取執行結果並驗收
8. Codex 將驗收結果寫入 `04_Codex_to_Cowork_驗收結果.md`

---

## 快捷指令

使用者可在 Cowork 對話中輸入：

```text
-*/
```

代表：

```text
請讀取 Codex / Cowork 協作交換區的最新指令並依規則處理。
```

Cowork 收到此快捷指令時，必須先讀取：

1. `00_Codex_to_Cowork_任務指令.md`
2. `02_Codex_to_Cowork_審核意見.md`
3. `01_Cowork_to_Codex_操作計畫.md`
4. `03_Cowork_to_Codex_執行結果.md`
5. `04_Codex_to_Cowork_驗收結果.md`

再依交換區固定流程決定是產出操作計畫、依審核意見執行，或回報缺少必要資訊。

判斷順序：

1. 若 `00_Codex_to_Cowork_任務指令.md` 狀態不是「等待 Codex 填寫」，且內容含明確任務，Cowork 應依 00 產出操作計畫到 `01_Cowork_to_Codex_操作計畫.md`
2. 若 `02_Codex_to_Cowork_審核意見.md` 有「通過，可執行」或「通過，但需依修正版執行」，Cowork 才可依審核意見執行
3. 若 `04_Codex_to_Cowork_驗收結果.md` 顯示上一輪驗收通過，且 00 沒有新任務，回報「上一輪已驗收完成，等待新任務」
4. 若 00 與 02 都沒有可執行內容，才回報「等待新任務」
5. 不得只因 01 / 02 是空白模板，就判斷沒有新任務；必須先確認 00

### 快捷指令修正紀錄

原先曾規劃使用 `/*-`，但 Cowork / Claude 介面會將 `/` 開頭內容視為斜線指令或 skill 呼叫，可能出現 `Unknown skill` 而無法送出。

因此正式快捷指令改為：

```text
-*/
```

此指令可用數字鍵盤快速輸入，且不以 `/` 開頭，避免被 Cowork / Claude 介面攔截為斜線指令。

---

## 禁止事項

- 不得在此資料夾存放 A 級敏感資料
- 不得存放帳密、Token、IP、DB 連線字串或客戶機密原文
- 不得用此資料夾取代任務包內的 `00_任務說明.md`、`99_待確認事項.md`、`worklog.md`
- 不得把草稿審核意見視為正式交付成果

---

## 使用提醒

本交換區只負責 Codex / Cowork 之間的「計畫、審核、結果」交接。

真正的任務紀錄仍需回寫到對應任務包的：

- `00_任務說明.md`
- `99_待確認事項.md`
- `worklog.md`
