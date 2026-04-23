# 我的第二大腦 — 快速指南

> 這份 README 是給人類看的快速使用手冊。  
> 完整 AI 規則與行為準則請見 [`AGENTS.md`](AGENTS.md)。

---

## 一眼看懂：五層架構

```text
輸入層       Notes/Clippings/       ← Web Clipper 抓取，永不修改
             Notes/Conversations/   ← 有價值 AI 對話，永不修改

沉澱層       知識庫/Concepts/        ← 概念頁
             知識庫/Entities/        ← 人物 / 組織 / 工具頁
             知識庫/Sources/         ← 來源頁
             知識庫/index.md         ← 知識庫摘要索引
             知識庫/log.md           ← 操作紀錄索引
             LifeOS/                ← 投資、健康、聯絡人等

輸出層       Writing/創作庫/         ← 文章、教案、腳本
             Writing/影片筆記/       ← 影片腳本
             Writing/教學素材/       ← 教學用素材

規則層       Templates/             ← 模板
             AGENTS.md              ← AI 規則
```

**新資訊唯一入口：** `Notes/`

---

## 常見任務

- **整理 Notes / ingest**：把新輸入整理進知識庫
- **查詢主題**：從知識庫綜合回答
- **寫文章 / 腳本**：從知識庫提取素材產出內容
- **健康檢查 / lint**：掃描孤立頁、重複概念、斷裂連結
- **同步 GitHub**：執行 `/sync-vault`

---

## 什麼內容值得存成 Conversations？

存入 `Notes/Conversations/`，檔名格式：`YYYY-MM-DD_主題關鍵字.md`

- ✅ 值得存：跨主題分析、決策過程、新洞見、架構討論
- ❌ 不用存：單純事實查詢

---

## 三種知識頁

| 類型 | 路徑 |
|------|------|
| Concept | `知識庫/Concepts/子目錄/` |
| Entity | `知識庫/Entities/` |
| Source | `知識庫/Sources/子目錄/` |

模板請見 `Templates/`。

---

**完整規則看 [`AGENTS.md`](AGENTS.md)。**
