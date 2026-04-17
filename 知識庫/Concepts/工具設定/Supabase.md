---
type: concept
aliases: ["Supabase資料庫"]
tags: [工具設定, 資料庫, MCP, 程式開發]
related_concepts: ["[[MCP]]", "[[Claude-Skill]]", "[[RAG]]"]
related_entities: ["[[三師爸Sense Bar]]"]
sources: ["[[Claude基本功EP09-Supabase串接資料庫]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

Supabase 是基於 PostgreSQL 的開源雲端資料庫服務，提供官方 MCP 支援，讓 Claude Code 可以用自然語言直接操控資料庫，無需手動撰寫 SQL 或 API 整合代碼。

## 核心重點

- **官方 MCP 支援**：這是在 Claude Code 環境中選用 Supabase 而非 Firebase 的主要原因——[[MCP]] 讓自然語言直接操控資料庫成為可能
- **免費方案限制**：閒置 7 天會自動暫停；解法是用 Claude Scheduled 任務每週自動查詢，保持活躍
- **與 GitHub 整合**：需用 GitHub 帳號註冊，因為網站通常掛 GitHub Pages，帳號一致管理方便
- **隱私原則**：資料會經過 Claude 處理，教育場景應去識別化，只保留座號不要姓名

## 不同視角 / 矛盾之處

- 免費方案的閒置暫停機制是刻意設計（節省資源），但對教學場景的長期穩定性是痛點
- PostgreSQL 標準讓遷移容易，但也代表 Supabase 只是入口，底層邏輯仍需理解 SQL

## 延伸問題

- Supabase 免費方案的資料量上限為何？超過後如何規劃升級？
- 與 [[RAG]] 架構結合時，Supabase 可扮演什麼角色（向量資料庫）？
- Scheduled 任務除了防止暫停，還有哪些自動化維護應用？
