---
type: source
original_path: "Notes/Clippings/用 OpenSpec 做了一個公車追蹤器！Spec-Driven Development 完整心得 OpenSpec SDD ClaudeCode 輕量 vibe-coding.md"
author:
  - "[[沈弘哲twtrubiks]]"
published: "2026-03-19"
tags:
  - openspec
  - spec-driven-development
  - ai-coding
  - claude-code
extracted_concepts:
  - "[[OpenSpec]]"
  - "[[規範驅動開發SDD]]"
extracted_entities:
  - "[[沈弘哲twtrubiks]]"
---

## 摘要（3 句內）

作者以台北公車追蹤器為實作案例，完整走完 OpenSpec 的 explore→propose→apply→archive 四步核心流程。文章深入解釋 archive 的 git 類比（specs = main branch、changes = feature branch、archive = git log），以及 delta spec 的獨特設計。結論：OpenSpec 是目前 SDD 工具中最輕量、最適合初學者完整跑完流程的選擇。

## 關鍵要點

- **四個核心指令**（按順序）：`explore` → `propose` → `apply` → `archive`
  - `explore`：引導式探索，討論架構、框架、API
  - `propose`：產生 proposal.md、spec ID、design.md、tasks.md
  - `apply`：按 task 分批執行（可切小塊，每完成一項 commit）
  - `archive`：將 changes 資料夾搬到 archive，並更新主 specs（節省 context）
- **Git 類比**：specs = main branch；changes = feature branch；delta spec = git diff；archive = git log
- **delta spec 獨特性**：只有 OpenSpec 有，用自然語言記錄 add/modify/remove/rename 變更
- **archive 的目的**：避免污染對話串，讓 AI 只看最新主 specs，節省 context window
- **兩種使用策略**：①完整走四步流程；②只用 propose 產出文件，再自行用 AI 執行
- **小 bug 不需走流程**：有 git commit 記錄即可，不必每次都用 OpenSpec
- **與 SpecKit 比較**：SpecKit 產出太多文件讓人不想繼續；OpenSpec 輕量，作者第一次完整跑完的工具

## 此篇與知識庫哪些頁面有關

- [[OpenSpec]] — 本篇核心工具，最詳細的流程說明
- [[規範驅動開發SDD]] — 方法論
- [[Claude-Skill]] — OpenSpec 初始化後會把 skill/command 放進 Claude Code 資料夾
