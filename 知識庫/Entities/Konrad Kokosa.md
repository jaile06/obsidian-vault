---
type: entity
role: "開發者 / 部落客"
tags:
  - dotnet
  - ai輔助開發
  - llm推理引擎
related_concepts:
  - "[[規範驅動開發SDD]]"
  - "[[Claude-Skill]]"
  - "[[AI確認機制]]"
sources:
  - "[[KokosaKonrad-dotLLM-CSharp推理引擎]]"
---

## 簡介

Konrad Kokosa（網路名稱：Dev Nerd）是波蘭籍 .NET 效能專家與部落客，長期研究 .NET 記憶體管理、GC、SIMD 優化。2026 年以約兩個月時間獨立完成 dotLLM，一個以 C#/.NET 10 從零建構的 LLM 推理引擎，並在過程中記錄了完整的 AI 輔助開發方法論。

## 主要觀點與貢獻

- **dotLLM 作者**：C#/.NET 10 原生 LLM 推理引擎，達到 llama.cpp CPU decode 效能的 66-88%
- **ROADMAP.md 驅動開發**：以 ~60 步結構化 Roadmap 指導 AI 實作，是「文件即方法論」的實際驗證案例
- **雙模型 PR 審查工作流**：Claude 實作、Codex + Gemini 獨立審查；不同模型有不同盲點，形成互補
- **6 個自定義 Claude Code Skill**：`/plan-step`、`/create-pr`、`/apply-pr-comments` 等，完整自動化開發循環
- **誠實紀錄 AI 極限**：AI 在架構抉擇、AVX2 暫存器優化、避免 compound tool calls 等方面仍有明確局限

## 與其他人物的關聯

- 與 [[工程師下班有約]] 同為「Claude Code 大型專案實戰」的中英文案例代表
- ROADMAP.md 方法論與 [[沈弘哲twtrubiks]] 使用的 OpenSpec 規格文件精神相通
