---
type: entity
role: "AI開發平台"
tags: [AI工具, Google, 免費工具]
related_concepts: ["[[AI影片轉逐字稿]]", "[[多模態]]"]
sources: ["[[ChuckChiang-GoogleAIStudio逐字稿教學]]"]
created: 2026-04-23
updated: 2026-04-23
---

## 簡介

Google 提供的免費 AI 開發與試用平台，內建 Gemini 系列模型（含 Gemini 2.5 Pro）。支援多模態輸入，包含文字、圖片、音訊、YouTube 影片連結。

## 主要觀點與貢獻

- **影片逐字稿提取**：貼上 YouTube 網址 → 輸入提示詞 → Gemini 直接解析音訊輸出文字（詳見 [[AI影片轉逐字稿]]）
- **免費額度**：每日提供免費 token，20 分鐘以內影片通常不超限
- **模型選擇**：建議使用 Gemini 2.5 Pro Preview（精度最高）

## 與其他人物的關聯

- 常與 [[NotebookLM]] 搭配：Google AI Studio 負責前處理（無字幕影片轉逐字稿），NotebookLM 負責後端 RAG 分析
