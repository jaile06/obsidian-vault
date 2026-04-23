---
type: concept
aliases: [影片逐字稿, 無字幕影片轉文字]
tags: [知識管理, AI工具, 逐字稿]
related_concepts: ["[[知識管理系統]]", "[[多模態]]"]
related_entities: ["[[Google AI Studio]]", "[[NotebookLM]]", "[[Chuck Chiang]]"]
sources: ["[[ChuckChiang-GoogleAIStudio逐字稿教學]]"]
created: 2026-04-23
updated: 2026-04-23
---

## 定義

利用多模態 AI 模型（如 Gemini 2.5 Pro）直接處理 YouTube 影片音訊，輸出純文字逐字稿，解決 YouTube 無內建字幕時無法匯入 NotebookLM 的問題。

## 核心重點

- **工具**：[[Google AI Studio]]（免費）搭配 Gemini 2.5 Pro Preview
- **操作流程**：加號 → YouTube Video → 貼上網址 → Add to Prompt → 輸入「提取影片逐字稿」→ 執行
- **限制**：每日免費 token 有限，建議用於 20 分鐘以內的影片
- **下游應用**：複製逐字稿 → 貼至 [[NotebookLM]] 新筆記本「貼上文字」欄位，即可進行 RAG 分析

## 不同視角 / 矛盾之處

- Google AI Studio 免費額度每日重置，長影片或批量轉稿需注意 token 消耗
- Gemini 直接處理影片 URL，免下載；但需影片為公開狀態

## 延伸問題

- 超過 20 分鐘的影片是否有替代方案（如本地 Whisper）？
- 逐字稿品質與原 YouTube 自動字幕相比如何？
