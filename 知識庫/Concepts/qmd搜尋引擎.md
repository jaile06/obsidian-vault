---
type: concept
aliases: [qmd, 本地Markdown搜尋]
tags: [技術工具, 知識管理, 搜尋]
related_concepts: ["[[Karpathy筆記方法]]", "[[知識管理系統]]", "[[RAG]]"]
sources: ["[[Karpathy-LLM Wiki原文]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

[qmd](https://github.com/tobi/qmd) 是本地 Markdown 檔案的混合搜尋引擎，結合 BM25（關鍵字）+ 向量搜尋 + LLM 重新排序，全程在裝置上執行，無需雲端。

## 核心重點

- **混合搜尋**：BM25（精確詞彙）+ 向量搜尋（語意相似）
- **LLM 重排序**：搜尋結果再由 LLM 依相關性排序
- **兩種介面**：CLI（LLM 可 shell out 呼叫）+ MCP Server（LLM 原生工具）
- **適用時機**：知識庫超過數百頁，index.md 方法效率下降時

## 與 index.md 方法的比較

| 方法 | 適用規模 | 需要安裝 | 搜尋精準度 |
|------|----------|----------|-----------|
| index.md | ~100 頁 | 不需要 | 中（依目錄導航） |
| qmd | 數百頁以上 | 需要 | 高（混合搜尋） |

## 本庫現況

目前使用 index.md 方法，規模尚不需要 qmd。若未來 Sources 超過 100 篇可考慮引入。
