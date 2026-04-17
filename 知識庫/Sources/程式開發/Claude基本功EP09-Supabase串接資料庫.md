---
type: source
original_path: "Notes/Clippings/Claude基本功EP09免費Supabase串起你的資料庫_用自然語言操控資料庫，完全免費的開發新邏輯.md"
author: ["[[三師爸Sense Bar]]"]
published: "2026-04-13"
tags: [Supabase, 資料庫, MCP, Claude-Code, 程式開發]
extracted_concepts: ["[[Supabase]]", "[[MCP]]"]
extracted_entities: ["[[三師爸Sense Bar]]"]
---

## 摘要（3 句內）

Supabase 是有官方 MCP 支援的免費 PostgreSQL 雲端資料庫，在 Claude Code 環境下可用自然語言直接操控，是 Firebase 的最佳替代選擇。用自然語言一句話即可讓 Claude 建立資料表、串接前端網頁、推播至 GitHub，完成完整的 Web App 開發流程。免費方案閒置 7 天會暫停，可透過 Claude Scheduled 任務每週自動查詢解決。

## 關鍵要點

### 選 Supabase 而非 Firebase 的原因

- Supabase 有**官方 MCP** 支援 → Claude Code 可直接用自然語言操控資料庫
- Firebase 無官方 MCP → 需手動 API 整合，無法自然語言操控
- Supabase 底層是 PostgreSQL（開源標準），可移植性高

### 安裝流程

1. 用 GitHub 帳號註冊 Supabase（網站要掛 GitHub，帳號一致較方便）
2. 建立專案 → 設定 Database 密碼 → 伺服器選亞洲
3. 產生 Personal Access Token（名稱：`claude code MCP`，永不過期）
4. 將 Token 貼給 Claude Code → 重啟 Claude Code → 開新 Session 連線

### 自然語言開發示範

- 一句話描述需求（文字雲網頁 + 資料庫串接 + QR Code）→ Claude 自動規劃、建資料表、寫前端、測試、Push 到 GitHub
- 資料分析：用自然語言請 Claude 從資料庫抓取資料並整理

### 閒置暫停問題解法

- 免費方案 7 天無使用 → 資料庫暫停
- 解法：在 Claude Code 設定 **Scheduled 任務**，每週一自動查詢兩個專案，保持活躍

### 隱私注意事項

- 資料會透過 Claude AI 處理，避免輸入個資
- 學校場景：只保留座號，不要姓名等敏感資料（去識別化）

## 此篇與知識庫哪些頁面有關

- [[Supabase]] — 本集核心工具
- [[MCP]] — Supabase 官方 MCP 是選用原因，也示範自然語言操控資料庫
- [[Claude-Skill]] — Scheduled 任務設定屬於自動化排程應用
