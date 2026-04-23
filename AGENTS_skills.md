# Skills 詳細流程

> 此檔案不自動注入。AI 在觸發對應 Skill 時才讀取。

---

## Skill 1: 資訊攝入與整理（Ingest & Organize）

當我要求你整理 `Notes`，或當 `Notes/Clippings/`、`Notes/Conversations/` 有新內容時，請執行以下流程。

### ⚠️ AI 確認機制 — 先列方案，確認後再執行

**第一階段：分析 & 提案（不動任何檔案）**

1. 讀取新文件。
2. 列出以下計畫給使用者確認：
   - 將建立哪些新的 Source / Concept / Entity 頁（含建議檔名、放哪個子目錄）
   - 將更新哪些現有頁面（列出具體變更）
   - 每份筆記建議的歸檔位置
   - 建議新增的標籤
   - 可與庫內哪些現有檔案交叉引用、合併或補連結
   - 如果有不確定的分類，明確標注「⚠️ 不確定」
3. **等使用者確認**（使用者可修改分類、合併建議）。

**第二階段：執行（使用者確認後）**

4. 在 `知識庫/Sources/` 建立 **Source 頁**。
5. 提取概念 → `知識庫/Concepts/`（已存在則**補充合併**，不重建）。
6. 提取人物 / 組織 / 工具 → `知識庫/Entities/`（已存在則**補充合併**）。
7. 在所有相關頁面加上雙向連結 `[[頁面名稱]]`。
8. 更新 `知識庫/index.md`（新增或整理條目）。
9. 在 `知識庫/log.md` 最上方新增一筆 ingest 記錄。
10. 若本次流程已明確完成且你要求同步，執行：
    `git add . && git commit -m "sync: YYYY-MM-DD ingest" && git push`
11. 原始檔案處理完成後，將其從 `Notes/Clippings/` 根目錄**移動**至 `Notes/Clippings/Archive/`，**不刪除**。根目錄只保留尚未處理的新 Clipping，Archive 為永久 Raw 存檔。

### 合併規則（避免重複建檔）

- Ingest 前**必讀** `知識庫/index.md`，確認是否已有相同或相似概念。
- 同一概念不同說法（如「Prompt Engineering」vs「提示詞工程」）→ 合併到同一頁，用 `aliases` 欄位。
- 同一人物不同稱呼 → 合併，用 `aliases`。
- 同一來源若已存在 → 補充而非重建。
- **絕對不允許建立重複頁面**。

---

## Conversation 入庫規則

以下情況的 AI 對話值得保存至 `Notes/Conversations/`：

- 包含跨主題的分析或比較
- 產出有價值的決策過程紀錄
- 有原文 / 其他頁面未提到的新洞見
- 重大架構決策或設計討論

**檔名格式**：`YYYY-MM-DD_主題關鍵字.md`

---

## Skill 2: 知識查詢與整合（Query & Synthesize）

當我向你提問時，請執行以下流程：

1. 先讀 `知識庫/index.md`，找出相關頁面。
2. 優先檢索並讀取相關的 `知識庫/Concepts/`、`知識庫/Entities/`、`知識庫/Sources/`、`LifeOS/` 與必要的 `Writing/` 內容。
3. 綜合多篇筆記的觀點後回答。
4. 如果在查詢過程中發現某些筆記之間有關聯但缺乏連結，請主動提議幫我補齊關聯。
5. **若這次回答有獨立保存價值**（例如分析、比較、跨頁面綜合、新洞見），可提議將其整理為新頁面保存。

### 保存新知規則

若這次回答值得保存：

1. 存至合適的 `知識庫/Concepts/` 子目錄，或其他更合理的目錄。
2. 加上完整 frontmatter（`type: analysis` 或 `type: concept`）。
3. 在 `知識庫/index.md` 新增條目。
4. 在 `知識庫/log.md` 記錄。
5. 若你確認要同步，再進行 git commit + push。

### 判斷標準

- 回答只是事實查詢（如「誰是 Karpathy？」）→ 不存。
- 回答包含新綜合、跨頁面整合、原文未明說的洞見 → 可提議存檔。
- 未經你確認，不直接新增、移動或改寫檔案。

---

## Skill 3: 內容輸出與創作（Content Output）

當我要求你「寫一篇文章」或「規劃腳本」時：

1. 從 `知識庫/`、`LifeOS/`、`Writing/` 等沉澱層提取相關素材作為基礎。
2. 產出完整的內容初稿。
3. 若內容完成且你確認保存，將最終稿件存入 `Writing/` 對應子目錄。
4. 建立與原始知識來源之間的雙向連結。
5. 檢查輸出內容是否產生新的概念、來源、人物，必要時回流到知識庫。

### Writing 輸出回流

輸出層（`Writing/`）的內容完成後，自動檢查：

1. 是否產生了新概念 → 回流到 `知識庫/Concepts/`
2. 是否引用了新外部來源 → 建立 Source 頁
3. 是否提到新人物 / 組織 / 工具 → 建立或更新 Entity 頁
4. 同樣遵守「先列方案 → 確認 → 執行」流程

---

## Skill 4: 知識庫健康檢查（Lint & Maintenance）

當我要求執行「健康檢查（Lint）」時：

1. 掃描 `Notes/`、`知識庫/`、`LifeOS/`、`Writing/`、`Templates/` 五個區域。
2. 找出資訊孤島（沒有被任何頁面引用，或 frontmatter 中關聯欄位皆為空的筆記）。
3. 檢查是否有重複探討同一概念但未合併的筆記。
4. 找出矛盾資訊（同一概念在不同頁面有衝突描述）。
5. 找出知識缺口（Concepts 頁「延伸問題」尚無對應頁面）。
6. 找出過薄頁面（Concepts 頁「核心重點」少於 3 點）。
7. 找出斷裂連結（`[[頁面名稱]]` 引用但檔案不存在）。
8. 產出一份 Lint / Weekly Report 供我檢閱。
9. 檢查並提議更新全局的 `知識庫/index.md`。

### 每週健康檢查（每週一 08:00 自動執行）

1. 找出孤立頁面。
2. 找出矛盾資訊。
3. 找出知識缺口。
4. 找出過薄頁面。
5. 找出斷裂連結。
6. 產出 `知識庫/WeeklyReport_YYYY-MM-DD.md`
7. 更新 `知識庫/log.md`

---

## Wiki 三種頁面格式

### Concepts 頁（概念）
```markdown
---
type: concept
aliases: []
tags: []
related_concepts: []
related_entities: []
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

## 定義

## 核心重點

## 不同視角 / 矛盾之處

## 延伸問題
```

### Entities 頁（人物 / 組織 / 工具）
```markdown
---
type: entity
role: ""
tags: []
related_concepts: []
sources: []
---

## 簡介

## 主要觀點與貢獻

## 與其他人物的關聯
```

### Sources 頁（來源）
```markdown
---
type: source
original_path: "Notes/Clippings/..."
author: []
published: ""
tags: []
extracted_concepts: []
extracted_entities: []
---

## 摘要（3 句內）

## 關鍵要點

## 此篇與知識庫哪些頁面有關
```
