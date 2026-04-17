---
type: source
original_path: "Clippings/用大神卡帕西的方法，我打造了一個會自我進化的AI知識庫.md"
author: ["[[我是戴倫]]"]
published: 2026-04-09
tags: [知識管理, Obsidian, Karpathy, 內容創作, Claude Code]
extracted_concepts: ["[[知識管理系統]]", "[[Karpathy筆記方法]]", "[[自動入庫]]", "[[知識庫健康檢查]]"]
extracted_entities: ["[[我是戴倫]]"]
---

## 摘要（3 句內）

作者在 Karpathy 發推前就已使用類似方法，這期展示融合後的完整系統：三層架構（Raw/Wiki/Schema）+ 全域索引 + 自動入庫 + 健康檢查。核心洞見：RAG 每次從零開始，沒有累積；Wiki 方法讓知識越用越厚。專為內容創作者設計，每次創作完自動提取金句、標題、爆款模式回流知識庫。

## 關鍵要點

- **RAG 的核心問題**：每次臨時檢索，沒有積累；Wiki 方法讓知識庫越用越厚
- **三層架構**：Raw（原始）/ Wiki（AI結構化）/ Schema（規則，即 CLAUDE.md）
- **全域索引 index.md**：AI 查詢第一站，告訴 AI 各庫位置與查詢順序
- **自動入庫 Ingest**：每次創作完自動提取 → 金句庫 / 標題庫 / 核心概念庫 / 暢銷內容庫
- **健康檢查 Lint**：自訂 `/vault-lint` skill，執行 10 項檢查（孤兒頁面、重複、索引過期）
- 三步驟入門：建 Raw/Wiki/Output 資料夾 → 寫 CLAUDE.md → 執行第一次 Ingest

## 此篇與知識庫哪些頁面有關

- [[Karpathy筆記方法]]
- [[第二大腦]]
- [[RAG]]
- [[自動入庫]]
- [[知識庫健康檢查]]
