---
type: entity
role: "AI 設計系統生成工具（Claude Skill 套件）"
tags: [工具, 網站設計, AI技術, Claude-Skill]
related_concepts: ["[[AI設計系統生成]]", "[[網站配色系統]]", "[[Claude-Skill]]"]
sources: ["[[NextLevelBuilder-UIUXProMax-Skill]]"]
created: 2026-06-11
updated: 2026-06-11
---

## 簡介

nextlevelbuilder 開發的開源（MIT）AI 設計系統生成 skill，安裝後（`npm install -g uipro-cli` → `uipro init --ai claude`）以自然語言觸發，依產業類別秒速生成含色板、字體、樣式的完整設計系統。

## 主要觀點與貢獻

- 把 UI/UX 判斷變成可檢索資料：161 產業規則、161 色板、67 UI 樣式、57 字體配對、99 條 UX 指南
- 三層推理流程：多域並行搜尋 → 推理引擎（BM25 排序＋反模式過濾）→ 交付前驗證清單
- 支援 React/Vue/Flutter/SwiftUI 等 15 個技術棧與多家 AI 助手（.claude/.factory/…）

## 與其他人物的關聯

- 與 [[Claude AI]] 官方 frontend-design skill 同屬 [[AI設計系統生成]] 方法論，路線相反（資料驅動 vs 原則驅動）
