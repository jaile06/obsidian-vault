# 我的第二大腦 — 快速指南

> 這份 README 是給「我忘了怎麼用這個 vault」時的快速參考。

---

## 一眼看懂：五層架構

```
輸入層       Notes/Clippings/       ← Web Clipper 抓取，永不修改
             Notes/Conversations/   ← 有價值的 AI 對話，永不修改

沉澱層       知識庫/Concepts/        ← 概念頁（AI 管理）
             知識庫/Entities/        ← 人物 / 組織 / 工具（AI 管理）
             知識庫/Sources/         ← 每篇原文一頁（AI 管理）
             知識庫/index.md         ← 知識庫入口（AI 管理）
             知識庫/log.md           ← 操作記錄（AI 管理）
             LifeOS/                ← 投資、健康、聯絡人等個人資料

輸出層       Writing/創作庫/         ← 教案、教材、影片字幕
             Writing/影片筆記/       ← 影片腳本
             Writing/教學素材/       ← 教學用素材

規則層       Templates/             ← 各種筆記的固定格式
             AGENTS.md              ← AI 行為規則（完整版）
```

**新資訊唯一入口**：`Notes/`

---

## 常見任務怎麼做

### 1. 我剪藏了新文章 → 整理進知識庫

對 Claude 說：**「整理 Notes」** 或 **「ingest」**

Claude 會：
1. 讀取 `Notes/Clippings/` 的新檔案
2. **列出計畫**（建哪些頁、改哪些頁）
3. **等你說 ok** 才執行
4. 處理完後把原檔移至 `Notes/Clippings/Archive/`

---

### 2. 我想查詢 / 研究某個主題

直接問 Claude 問題。

Claude 會先讀 `知識庫/index.md`，再綜合相關頁面回答。  
若分析結果有保存價值，Claude 會提議存成新頁面（你確認後才存）。

---

### 3. 我想寫文章 / 腳本

對 Claude 說：**「幫我寫一篇關於 X 的文章」**

Claude 會從知識庫提取素材 → 產出初稿 → 徵詢後存入 `Writing/` 對應子目錄。

---

### 4. 我想做知識庫健康檢查

對 Claude 說：**「執行健康檢查」** 或 **「lint」**

Claude 會掃描五個區域，找出：
- 孤立頁面、重複概念、矛盾資訊
- 知識缺口、過薄頁面、斷裂連結

產出一份 Report 供你檢閱。

---

### 5. 同步到 GitHub

執行 Skill：**`/sync-vault`**

---

## 重要規則（別讓 AI 踩雷）

| 規則 | 說明 |
|------|------|
| 先提案再執行 | 任何寫檔、移檔、補連結，Claude 必須先列方案等你確認 |
| 先查 index | 新增頁面前必須先讀 `知識庫/index.md`，不建重複頁 |
| 不修改輸入層 | `Notes/Clippings/` 與 `Notes/Conversations/` 原始內容永遠不動 |
| 實際結構優先 | AGENTS.md 與現況不符時，以 repo 實際路徑為準 |

---

## 有價值的 Conversation 什麼時候存？

存入 `Notes/Conversations/`，檔名：`YYYY-MM-DD_主題關鍵字.md`

✅ 值得存：跨主題分析、決策過程、新洞見、架構討論  
❌ 不用存：單純事實查詢（「誰是 X？」）

---

## 三種知識庫頁面格式

| 頁面類型 | 放在哪 | frontmatter type |
|---------|--------|-----------------|
| 概念頁 | `知識庫/Concepts/子目錄/` | `concept` |
| 人物/組織/工具頁 | `知識庫/Entities/` | `entity` |
| 來源頁 | `知識庫/Sources/子目錄/` | `source` |

格式模板詳見 `AGENTS.md` 底部。

---

*完整 AI 行為規則請見 [AGENTS.md](AGENTS.md)*
