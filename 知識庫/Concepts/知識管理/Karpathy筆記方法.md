---
type: concept
aliases: [Karpathy Wiki Method, Raw-Wiki方法]
tags: [知識管理, AI筆記, Obsidian]
related_concepts: ["[[第二大腦]]", "[[知識管理系統]]", "[[RAG]]"]
related_entities: ["[[Andrej Karpathy]]"]
sources: ["[[Karpathy筆記術-Claude Code建立知識庫]]", "[[EP08-Obsidian打造AI筆記流]]", "[[Karpathy-LLM Wiki原文]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

Andrej Karpathy 提出的個人知識庫方法：用 Raw + Wiki 雙層結構，由 LLM 自動維護索引與頁面連結，無需 RAG 或向量資料庫。

## 核心重點

- **Raw**：存放所有原始資料（文章、PDF），永遠不修改
- **Wiki**：AI 整理後的結構化知識，分 Concepts / Entities / Sources 三種頁面
- **Index.md**：知識庫總目錄，AI 查詢時先讀這頁，不需掃描全部檔案
- **Log.md**：AI 每次操作記錄，避免重複處理
- **claude.md**：系統說明書，每次啟動自動讀取
- AI 自動發現跨文章連結，形成 Graph View

## 不同視角 / 矛盾之處

- 與傳統 RAG 的最大差異：不需向量資料庫，靠 LLM 讀目錄索引查資料，適合 ~100 篇個人規模
- 規模超過數百篇後，token 成本顯著上升，此時需考慮改用 RAG

## 延伸問題

- 如何設計 claude.md 讓 AI 更精準地執行 ingest？
- Wiki 頁面粒度如何拿捏（太細碎 vs 太籠統）？
