---
type: source
original_path: "Clippings/矽谷大神 Karpathy 筆記術！十分鐘學會如何用 Claude Code 建立個人知識庫.md"
author: ["[[Paula 寶拉]]"]
published: 2026-04-14
tags: [Obsidian, 知識管理, AI筆記, Claude Code, Karpathy, 第二大腦]
extracted_concepts: ["[[第二大腦]]", "[[知識管理系統]]", "[[RAG]]"]
extracted_entities: ["[[Paula 寶拉]]", "[[Andrej Karpathy]]", "[[Claude]]"]
---

## 摘要（3 句內）

實作 Andrej Karpathy 分享的個人知識庫方法：Raw（原始資料）+ Wiki（AI整理）雙層結構，不需 RAG 也不需向量資料庫。Wiki 分三種頁面類型（Concepts / Entities / Sources），AI 靠讀 Index 目錄快速查詢，無需掃描所有檔案。適合個人規模（~100篇），建置簡單、維護成本低。

## 關鍵要點

- **Raw / Wiki 雙層結構**：Raw 存原始資料，Wiki 是 AI 管理的整理層
- **三種 Wiki 頁面**：Concepts（概念）/ Entities（人物）/ Sources（來源）
- **Index.md**：知識庫總目錄，AI 每次先讀這頁再找資料
- **Log.md**：記錄每次 AI 操作歷史
- **claude.md**：給 AI 看的說明書，每次啟動自動讀取
- **vs. 傳統 RAG**：不需向量資料庫，靠 markdown + index 就夠，設定簡單
- 知識越用越豐富：問答結果存回 Wiki，缺口由 AI 建議補充
- 限制：Claude Code 需付費、100篇以上效果遞減、token 成本隨規模增加

## 此篇與知識庫哪些頁面有關

- [[第二大腦]]
- [[知識管理系統]]
- [[RAG]]
- [[Karpathy筆記方法]]
- [[EP08-Obsidian打造AI筆記流]]
