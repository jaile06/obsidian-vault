---
type: source
original_path: "Notes/Clippings/LLM Wiki - Andrej Karpathy.md"
author: ["Andrej Karpathy"]
published: "2026"
tags: [知識管理, LLM, Wiki, 第二大腦]
extracted_concepts: ["[[Karpathy筆記方法]]", "[[知識管理系統]]", "[[RAG]]", "[[第二大腦]]", "[[Memex]]", "[[Marp]]", "[[Dataview]]", "[[qmd搜尋引擎]]"]
extracted_entities: ["[[Andrej Karpathy]]", "[[NotebookLM]]", "[[ChatGPT]]", "[[Obsidian]]"]
---

## 摘要

Karpathy 提出「LLM Wiki」模式：與其用 RAG 每次重新檢索，不如讓 LLM 持續維護一個結構化 Wiki，每新增來源就整合入庫，知識隨時間累積而非每次從頭推導。

## 關鍵要點

- **三層架構**：Raw Sources（不可修改）→ Wiki（LLM 擁有）→ Schema（CLAUDE.md / AGENTS.md）
- **核心差異 vs RAG**：Wiki 是持久累積的人工製品；RAG 每次從頭推導，知識不積累
- **三種操作**：Ingest（消化入庫）、Query（查詢，好答案也可存回 Wiki）、Lint（健康檢查）
- **兩個特殊檔案**：`index.md`（內容導向目錄，AI 先讀這裡）、`log.md`（時序記錄，附 grep 技巧）
- **工作模式**：LLM 在一側，Obsidian 在另一側，即時瀏覽更新。「Obsidian = IDE，LLM = 程式設計師，Wiki = 程式碼庫」
- **選配工具**：qmd（本地 markdown 混合搜尋）、Obsidian Web Clipper、Marp（投影片）、Dataview（動態表格）
- **精神來源**：Vannevar Bush 的 Memex（1945），人工整理連結的私人知識庫

## 此篇與知識庫哪些頁面有關

- [[Karpathy筆記方法]]（本文是原始定義來源，補充操作細節）
- [[知識管理系統]]（三層架構 = 本庫架構直接依據）
- [[RAG]]（明確指出 Wiki 方法的替代性與優勢）
- [[第二大腦]]（個人知識累積的願景）
- [[Andrej Karpathy]]（作者，補充其原文觀點）
- [[知識庫健康檢查]]（Lint 操作的原始描述）
