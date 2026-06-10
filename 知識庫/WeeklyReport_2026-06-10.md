---
title: 知識庫健康檢查報告
type: report
created: '2026-06-10'
---

# 知識庫健康檢查報告 2026-06-10

> Skill 4 全庫掃描。範圍：全 vault 246 個 md（排除 .git / .obsidian / .venv / media / scripts）。
> 知識庫現況：Concepts 45 ｜ Entities 35 ｜ Sources 65。

---

## 0. 架構檢查

- ✅ 五層架構資料夾（Notes / 知識庫 / LifeOS / Writing / Templates）齊全。
- ✅ 已刪除根目錄多餘的空 `Clippings/`（僅含 Google Drive 的 desktop.ini，疑為 Obsidian Web Clipper 預設路徑誤建）。**待辦：** 檢查 Web Clipper 儲存路徑是否指向 `Notes/Clippings`。
- ⚠️ `index.md` 標示 Concepts（44），實際檔案 45 個 — 計數漂移，需核對 [[index-concepts]]。

---

## 1. 斷裂連結（知識庫層，可修復）

### 1a. 檔名不一致（修復後孤立頁面問題一併解決）

| 斷鏈 | 出現位置 | 原因 / 建議 |
|------|----------|-------------|
| `[[Konrad Kokosa]]` ×9 | index.md、index-entities.md、[[規範驅動開發SDD]]×2、[[dotLLM]]、KokosaKonrad source ×2、log/2026-04 ×2 | 實際檔名為 `KonradKokosa.md`（無空格）。**建議改名為 `Konrad Kokosa.md`**，9 處連結（含 Archive 內 1 處）即全部接通 |
| `[[Lewis搞事日记]]` ×2（簡體） | [[Lewis搞事日記-Karpathy知識庫SKILL]] | 實際檔名為繁體 `Lewis搞事日記.md`。建議改正連結為繁體 |

### 1b. `conv:` 前綴連結（×13，目標檔案皆存在）

`[[conv:YYYY-MM-DD_xxx]]` 寫法 Obsidian 無法解析；對應檔案都在 `Notes/Conversations/`，拿掉 `conv:` 前綴即可。

出現位置：[[第二大腦]]、[[五層知識庫架構]]、[[OpenSpec]]×2、[[XOOPS開發規範]]×2、[[Obsidian PDF擷取]]、log/2026-05 ×6。

### 1c. 缺 Entity 頁的工具連結

| 連結 | 次數 | 主要出現位置 |
|------|------|--------------|
| `[[Claude]]` | 6 | 提示詞工程、ChatGPT、AI工具總覽 等 |
| `[[Canva]]` | 6 | 網站設計各頁 |
| `[[Coolors]]` | 5 | 網站設計各頁 |
| `[[Gemini]]`、`[[Perplexity]]`、`[[microsoft]]` | 各 2 | ChatGPT、AI工具總覽、MarkItDown |
| `[[Obsidian]]`、`[[Dataview]]`、`[[Marp]]`、`[[Gamma]]`、`[[Unsplash]]`、`[[Pexels]]`、`[[DiceBear]]`、`[[OpenClaw]]` | 各 1 | 散見各 Source |

建議：高頻者（Claude、Canva、Coolors）建 Entity 頁；單次出現者去除 `[[]]` 改為純文字。

### 1d. 輸入層斷鏈（Notes/ 永不修改，僅記錄）

- Archive：`[[范凯说AI]]`（簡體 vs 實體頁繁體「范凱说AI」）、`[[沈弘哲]]`、`[[Lewis 搞事日记]]`、`[[裝修小武郎]]`（無對應 Entity）、`[[microsoft]]`
- Conversations：`[[OpenSpec 如何整合到 XOOPS 開發專案]]` ×2、`[[OpenSpec安裝初始化]]`、`[[Obsidian]]`、`[[PDF擷取]]`、`[[知識輸入]]`

### 1e. 誤報排除（不處理）

AGENTS.md `[[Page Name]]`、[[Markdown語法]] / [[Memex]] / [[知識庫健康檢查]] 內的 `[[wikilink]]` 字面示例、Templates/週計畫.md 的 Templater 語法。

---

## 2. 孤立頁面

| 頁面 | 狀態 | 解法 |
|------|------|------|
| [[Konrad Kokosa]]（原 KonradKokosa.md） | 完全孤立（連 index 都沒引用到） | 1a 改名後自動解決 |
| [[Lewis搞事日記]] | 僅 index/log 引用 | 1a 修正簡體連結後自動解決 |

---

## 3. 重複概念

未發現。線型函數 / 一次函數 / 常數函數為刻意拆分的數學概念，已正確互連。

---

## 4. 矛盾資訊 / 資料損壞

- ⚠️ [[小資族理財入門]] 第 50 行有亂碼：「何時引入主動投資或**�**槓桿？」— 建議修正為「或**開**槓桿」。
- 未發現頁面間實質矛盾。

---

## 5. 過薄頁面

**真正過薄（關鍵要點 < 3）：**

| 頁面 | 備註 |
|------|------|
| [[Lewis搞事日記-Karpathy知識庫SKILL]] | 關鍵要點僅 2 點 |
| [[阿西出海-8個必裝AISkill分類]] | ingest 時已註記「無逐字稿，內容較薄」 |
| [[PowerAppsTW-CopilotCowork投資儀表板自動化]] | 同上 |

**格式偏離模板（內容充實，非過薄，低優先）：**
[[Claude Code設定四層]]（用「四層架構」）、[[知識庫健康檢查]]（用「檢查項目」）、[[AI思維重構影片資源]]（用「影片清單」）、會考解析 ×22（用「高頻考點」等自訂結構）。

---

## 6. 知識缺口（延伸問題無對應頁）

36 個 Concept 頁有未解答的延伸問題。**跨頁重複出現、值得優先補頁的主題：**

1. **暗色模式配色** — [[網站配色系統]]、[[對比度測試]]、[[色彩角色]] 三頁都問到
2. **SDD 應用於非軟體領域** — [[OpenSpec]]、[[規範驅動開發SDD]] 都問到
3. **AGENTS.md / CLAUDE.md 規範整合** — [[OpenSpec]]、[[XOOPS開發規範]] 都問到
4. **115 年會考命題預測** — 自然、數學命題趨勢頁都問到
5. **RAG vs Fine-tuning** — [[RAG]]
6. **Prompt 模板設計（System vs User Prompt）** — [[提示詞工程]]、[[Obsidian Skill]]

完整清單見各 Concept 頁「延伸問題」區塊。

---

## 修復建議優先序

1. 🔴 改名 `KonradKokosa.md` → `Konrad Kokosa.md`（解 9 處斷鏈 + 1 孤立頁）
2. 🔴 修正 `[[Lewis搞事日记]]` 簡→繁 ×2（解 2 處斷鏈 + 1 孤立頁）
3. 🔴 修正 [[小資族理財入門]] 亂碼
4. 🟡 移除 13 處 `conv:` 前綴
5. 🟡 核對 index.md Concepts 計數（44 vs 45）
6. 🟢 高頻工具建 Entity 頁（Claude / Canva / Coolors），低頻去連結
7. 🟢 檢查 Obsidian Web Clipper 儲存路徑設定
