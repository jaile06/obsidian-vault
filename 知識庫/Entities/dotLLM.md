---
type: entity
role: "開源工具"
tags:
  - dotnet
  - llm推理引擎
  - open-source
related_concepts:
  - "[[規範驅動開發SDD]]"
  - "[[Claude-Skill]]"
sources:
  - "[[KokosaKonrad-dotLLM-CSharp推理引擎]]"
---

## 簡介

dotLLM 是由 Konrad Kokosa 開發的開源 LLM 推理引擎，以 C#/.NET 10 從零實作，非任何 C/C++ 函式庫的包裝。v0.1.0-preview.2 於 2026 年 4 月釋出。GitHub: `kkokosa/dotLLM`，授權：GPLv3。

## 主要功能

- **支援模型**：Llama、Mistral、Phi、Qwen、DeepSeek（GGUF 格式）
- **運算後端**：SIMD CPU（AVX2/AVX-512）、CUDA GPU（PTX kernels）、混合模式
- **效能**：Decode 達 llama.cpp 的 66-88%；Prefill 仍慢 2-5x（暫存器瓶頸）
- **API**：OpenAI 相容 `/v1/chat/completions`，支援 tool calling、SSE streaming
- **進階功能**：Speculative decoding、FSM 結構化輸出（JSON/regex/GBNF）、KV-cache quantization
- **NuGet 套件**：`DotLLM.Engine`、`DotLLM.Cpu`、`DotLLM.Cuda`、`DotLLM.Server`

## 與其他人物的關聯

- 作者：[[Konrad Kokosa]]
- 定位：填補 .NET 生態系缺乏原生 LLM 推理引擎的空缺，替代 LLamaSharp（llama.cpp wrapper）
