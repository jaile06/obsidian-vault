# 我的第二大腦 — AGENTS.md

## 關於我
- 我是資深程式設計師，也是教學內容創作者
- 這個 vault 是我的「五層架構」第二大腦

## 語言偏好
- 所有回應請使用繁體中文
- 筆記內容也用繁體中文

---

## 五層資料夾架構

| 層級 | 資料夾 | 類型 | 用途 |
|------|--------|------|------|
| 輸入 | `Notes/Clippings/` | 原始資料（外部） | Web Clipper 抓取的文章、影片逐字稿 — **永遠不修改** |
| 輸入 | `Notes/Conversations/` | 原始資料（AI 對話） | 與 AI 的有價值對話 — **永遠不修改** |
| 沉澱 | `知識庫/Concepts/` | AI 管理 | 概念頁（按主題子目錄分類） |
| 沉澱 | `知識庫/Entities/` | AI 管理 | 人物 / 組織 / 工具頁 |
| 沉澱 | `知識庫/Sources/` | AI 管理 | 來源頁（每篇原文對應一頁，按主題子目錄分類） |
| 沉澱 | `知識庫/index.md` | AI 管理 | 知識庫總目錄 — AI 查詢的第一站 |
| 沉澱 | `知識庫/log.md` | AI 管理 | AI 操作記錄 |
| 沉澱 | `LifeOS/` | 個人使用 | 投資、健康、聯絡人等生活工作資料 |
| 沉澱 | `LifeOS/每日筆記/` | 個人使用 | 每日紀錄、週計畫 |
| 輸出 | `Writing/創作庫/` | 輸出層 | 自己的教案、教材、影片字幕 |
| 輸出 | `Writing/影片筆記/` | 輸出層 | 影片腳本與筆記 |
| 輸出 | `Writing/教學素材/` | 輸出層 | 教學用素材檔案 |
| 規則 | `Templates/` | 個人使用 | 各種筆記的固定格式 |

---

## Ingest 流程（有新原始資料時執行）

### ⚠️ AI 確認機制 — 先列方案，確認後再執行

每次 `Notes/Clippings/` 或 `Notes/Conversations/` 有新內容時：

**第一階段：分析 & 提案（不動任何檔案）**

1. 讀取新文件
2. 列出以下計畫給使用者確認：
   - 將建立哪些新的 Source / Concept / Entity 頁（含建議檔名、放哪個子目錄）
   - 將更新哪些現有頁面（列出具體變更）
   - 如果有不確定的分類，明確標注「⚠️ 不確定」
3. **等使用者確認**（使用者可修改分類、合併建議）

**第二階段：執行（使用者確認後）**

4. 在 `知識庫/Sources/` 建立 **Source 頁**
5. 提取概念 → `知識庫/Concepts/`（已存在則**補充合併**，不重建）
6. 提取人物 / 組織 → `知識庫/Entities/`（已存在則**補充合併**）
7. 在所有相關頁面加上雙向連結 `[[頁面名稱]]`
8. 更新 `知識庫/index.md`（新增新頁面條目）
9. 在 `知識庫/log.md` 最上方新增一筆 ingest 記錄
10. `git add . && git commit -m "sync: YYYY-MM-DD ingest" && git push`

### 合併規則（避免重複建檔）

- Ingest 前**必讀** `知識庫/index.md` 確認是否已有相同或相似概念
- 同一概念不同說法（如「Prompt Engineering」vs「提示詞工程」）→ 合併到同一頁，用 `aliases` 欄位
- 同一人物不同稱呼 → 合併，用 `aliases`
- **絕對不允許建立重複頁面**

---

## Conversation 入庫規則

以下情況的 AI 對話值得保存至 `Notes/Conversations/`：

- 包含跨主題的分析或比較
- 產出有價值的決策過程紀錄
- 有原文/其他頁面未提到的新洞見
- 重大架構決策或設計討論

**檔名格式**：`YYYY-MM-DD_主題關鍵字.md`

---

## Writing 輸出回流

輸出層（Writing/）的內容完成後，自動檢查：

1. 是否產生了新概念 → 回流到 `知識庫/Concepts/`
2. 是否引用了新外部來源 → 建 Source 頁
3. 是否提到新人物 → 建 Entity 頁
4. 同樣遵守「先列方案 → 確認 → 執行」流程

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

### Entities 頁（人物 / 組織）
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

---

## Query 流程（回答問題時執行）

1. 先讀 `知識庫/index.md`，找出相關頁面
2. 讀取相關 Concepts / Entities / Sources 頁，綜合後回答
3. **若這次回答有獨立保存價值**（分析、比較、跨頁面綜合、新洞見），自動將其存為新頁面：
   - 存至 `知識庫/Concepts/` 子目錄
   - 加上完整 frontmatter（type: analysis 或 concept）
   - 在 index.md 新增條目
   - 在 log.md 記錄
   - git commit + push
4. **判斷標準**：回答只是事實查詢（如「誰是 Karpathy？」）→ 不存；有新綜合或原文未明說的洞見 → 存

---

## 每週健康檢查（每週一 08:00 自動執行）

1. 找出孤立頁面（frontmatter 中所有關聯欄位皆為空）
2. 找出矛盾資訊（同一概念在不同頁面有衝突描述）
3. 找出知識缺口（Concepts 頁「延伸問題」尚無對應頁面）
4. 找出過薄頁面（Concepts 頁「核心重點」少於 3 點）
5. 找出斷裂連結（`[[頁面名稱]]` 引用但檔案不存在）
6. 產出 `知識庫/WeeklyReport_YYYY-MM-DD.md`
7. 更新 `知識庫/log.md`

---

## 回答風格
- 回答要簡潔，不要冗長
- 每次回答都要附上建議（下一步行動或改善方向）
