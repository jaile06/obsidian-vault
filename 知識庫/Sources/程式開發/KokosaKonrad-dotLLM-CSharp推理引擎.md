---
type: source
original_path: "Notes/Clippings/Introducing dotLLM - Building an LLM Inference Engine in C  Konrad 'Dev Nerd' Kokosa.md"
author:
  - "[[Konrad Kokosa]]"
published: 2026-04-14
tags:
  - dotnet
  - llm推理引擎
  - ai輔助開發
  - claude-code
extracted_concepts:
  - "[[規範驅動開發SDD]]"
  - "[[Claude-Skill]]"
extracted_entities:
  - "[[Konrad Kokosa]]"
  - "[[dotLLM]]"
---

## 摘要（3 句內）

Konrad Kokosa 以 C#/.NET 10 從零建立 LLM 推理引擎 dotLLM，歷時約兩個月，核心方法是「結構化 AI 輔助開發」。以 ROADMAP.md（~60 步分階段計畫）+ CLAUDE.md（AI 工作憲章）+ 雙模型 PR 審查（Codex + Gemini）構成完整工作流，並為 Claude Code 設計 6 個自定義 Skill 自動化開發循環。是罕見的「一人兩個月完成系統級 C# LLM 引擎」案例，同時記錄 AI 輔助開發在效能調教上的極限與突破。

## 關鍵要點

**dotLLM 技術面：**
- 原生 C#/.NET 10，非 llama.cpp wrapper；GGUF 模型載入、tokenizer、attention、取樣、SIMD CPU、CUDA GPU 全部純 C# 實作
- 分層架構：Core → Cpu/Cuda → Models/Tokenizers → Engine → Server/CLI
- Decode 吞吐達 llama.cpp 的 66-88%（記憶體頻寬瓶頸）；Prefill 仍慢 2-5x（AVX2 暫存器壓力問題）
- OpenAI 相容 API、Speculative decoding、FSM/PDA 結構化輸出、KV-cache quantization

**AI 輔助開發方法論：**
- **ROADMAP.md 是最高 ROI 投資**：~60 個步驟分 7 個 Phase，每步有明確範圍、依賴與接受標準；沒有 Roadmap，AI 就沒有方向感
- **CLAUDE.md 是 AI 憲章**：180+ 行定義 AI 在專案中的工作方式（不允許 managed 陣列存 tensor、SIMD 規範等），加上 22 份子系統設計文件
- **6 個自定義 Skill**：`/plan-step`、`/create-pr`、`/apply-pr-comments`、`/finish-pr-comments`、`/merge-pr`、`/plan-issue`；完整自動化從規劃到 merge 的循環
- **雙模型 PR 審查**：Claude 寫代碼，Codex + Gemini 獨立審查；不同模型有不同盲點，Codex 善找邏輯 bug，Gemini 善發現架構問題
- **計畫與執行分離**：`/plan-step` 進入 Plan Mode，人工確認後才執行；AI 不能未經確認自行動手
- **AI 失敗邊界**：架構決策（選哪種 attention）仍需人類判斷；避免 compound tool calls 的提醒屢次失效

## 此篇與知識庫哪些頁面有關

- [[規範驅動開發SDD]]：ROADMAP.md 的結構化分步計畫與 SDD 精神高度一致；補充「一人兩個月完成系統級項目」的實戰驗證
- [[Claude-Skill]]：6 個自定義 Skill 完整展示 Skill 在大型專案中的真實應用規模
- [[OpenSpec]]：概念相近，都是「先規格後實作」，但 dotLLM 用 ROADMAP.md 自行管理，而非 OpenSpec 工具
- [[AI確認機制]]：plan-step 進入 Plan Mode 的設計與「先提案再執行」完全一致
