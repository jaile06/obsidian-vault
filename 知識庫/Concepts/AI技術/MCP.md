---
type: concept
aliases: ["Model Context Protocol", "模型上下文協議"]
tags: [AI技術, Claude-Code, 工具串接]
related_concepts: ["[[Context Window]]", "[[Claude-Skill]]", "[[RAG]]"]
related_entities: ["[[NotebookLM]]"]
sources: ["[[Claude基本功EP04-NotebookLM五大進階應用]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

MCP（Model Context Protocol）是讓 Claude 能夠呼叫外部工具與服務的協議標準。透過安裝對應的 MCP Server，Claude Code 可以直接操作 NotebookLM、Obsidian、GitHub 等平台，執行超出本地文件範圍的任務。

## 核心重點

- **協議層**：MCP 定義了 Claude 與外部工具之間的溝通格式，類似 API 的橋梁
- **Context Window 成本**：每個已安裝的 MCP 都會佔用 [[Context Window]] 空間，即使未使用；建議只安裝工作最核心的幾個
- **額度分離**：透過 MCP 操作第三方工具時，外部平台的操作花第三方帳號額度（如 NotebookLM 花 Google 額度），Claude 本身的推理和檔案處理花 Claude 額度
- **常見 MCP 應用**：NotebookLM（RAG 知識整理）、Obsidian（筆記寫入）、GitHub（版本控制）、[[Supabase]]（資料庫操控）、網頁搜尋
- **官方 vs 非官方**：有官方 MCP 的工具（如 Supabase）穩定性與安全性更高；Firebase 無官方 MCP，因此在 Claude Code 環境中較難自然語言操控

## 不同視角 / 矛盾之處

- MCP 大幅擴展 Claude 能力，但裝太多會讓 Context Window 擁擠，降低推理品質
- 各 MCP Server 品質不一，需評估可信度再安裝

## 延伸問題

- 如何評估一個 MCP 是否值得安裝（成本效益分析）？
- MCP 與直接呼叫 API 的差異為何？
- [[Claude-Skill]] 與 MCP 如何搭配使用？
