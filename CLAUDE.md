# 我的第二大腦 — CLAUDE.md

## 關於我
- 我是資深程式設計師
- 這個 vault 是我的教學第二大腦

## 語言偏好
- 所有回應請使用繁體中文
- 筆記內容也用繁體中文

---

## 資料夾結構

| 資料夾 | 類型 | 用途 |
|---|---|---|
| `Clippings/` | 原始資料（外部） | Web Clipper 抓取的文章、影片逐字稿 — **永遠不修改** |
| `創作庫/` | 原始資料（自創） | 自己的教案、教材、影片字幕 — **永遠不修改** |
| `知識庫/Concepts/` | AI 管理 | 概念頁 |
| `知識庫/Entities/` | AI 管理 | 人物 / 組織頁 |
| `知識庫/Sources/` | AI 管理 | 來源頁（每篇原文對應一頁） |
| `知識庫/index.md` | AI 管理 | 知識庫總目錄 |
| `知識庫/log.md` | AI 管理 | AI 操作記錄 |
| `每日筆記/` | 個人使用 | 每日紀錄、週計畫 |
| `Templates/` | 個人使用 | 各種筆記的固定格式 |

---

## Ingest 流程（有新原始資料時執行）

**全自動，無需確認，直接執行完畢。**

每次 Clippings/ 或 創作庫/ 有新內容，依序完成：

1. 讀取新文件
2. 在 `知識庫/Sources/` 建立一個 **Source 頁**
3. 提取文中出現的概念 → `知識庫/Concepts/`（已存在則補充，不重建）
4. 提取文中出現的人物 / 組織 → `知識庫/Entities/`（已存在則補充）
5. 在所有相關頁面加上雙向連結 `[[頁面名稱]]`
6. 更新 `知識庫/index.md`（新增新頁面條目）
7. 在 `知識庫/log.md` 最上方新增一筆 ingest 記錄
8. `git add . && git commit -m "sync: YYYY-MM-DD ingest" && git push`

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
original_path: "Clippings/..."
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
   - 存至 `知識庫/Concepts/`子目錄
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
