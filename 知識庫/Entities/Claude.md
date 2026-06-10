---
type: entity
role: "AI 助手（Anthropic）"
tags:
  - AI工具
related_concepts:
  - "[[提示詞工程]]"
  - "[[Claude-Skill]]"
  - "[[Claude Code設定四層]]"
  - "[[Claude Design]]"
  - "[[MCP]]"
sources:
  - "[[AI工具總覽]]"
  - "[[Karpathy筆記術-Claude Code建立知識庫]]"
  - "[[EP08-Obsidian打造AI筆記流]]"
created: 2026-06-10
updated: 2026-06-10
---

## 簡介

Anthropic 開發的 AI 助手，以資安等級高、程式撰寫能力強著稱。產品線涵蓋 Claude Code（終端編程代理）、[[Claude Design]]（視覺設計）與 [[Claude-Skill]]（工作流打包），是本知識庫五層架構工作流的核心執行引擎。

## 主要觀點與貢獻

- [[AI工具總覽]]：七款主流 AI 工具比較中定位為「資安等級高、寫程式表現最優」
- Claude Code 是 [[Karpathy筆記方法]] 與本庫知識管理流程的主要工具（[[Karpathy筆記術-Claude Code建立知識庫]]、[[EP08-Obsidian打造AI筆記流]]）
- 透過 [[MCP]] 串接外部工具，以 [[Claude Code設定四層]]（CLAUDE.md / Rules / Memory / Hooks）客製行為

## 與其他人物的關聯

- 與 [[ChatGPT]]、Gemini、Perplexity 為競爭產品
- 常與 [[NotebookLM]] 分工：Claude 負責生成與編程，NotebookLM 負責大量資料的 RAG 整理
