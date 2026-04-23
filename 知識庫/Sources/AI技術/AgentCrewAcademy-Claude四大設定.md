---
type: source
original_path: Notes/Clippings/Claude 一直忘規則、不了解你？這四個設定一次解決.md
author:
  - '[[AgentCrew Academy]]'
published: '2026-04-17'
tags:
  - ClaudeCode
  - 工具設定
  - CLAUDE.md
  - Hooks
  - Memory
extracted_concepts:
  - '[[Claude Code設定四層]]'
  - '[[Context Window]]'
extracted_entities:
  - '[[AgentCrew Academy]]'
---

## 摘要（3 句內）

Claude 一直忘規則的根本原因是自然語言指令只是「建議」，模型可以選擇性忽略。解法是依風險等級分四層：CLAUDE.md 放通用默契、Rules 按路徑按需載入、Memory 讓 Claude 記錄動態狀態、Hooks 以程式碼強制攔截不可逾越的底線。進化路徑不需一步到位，從 CLAUDE.md 開始，視情況漸進升級到 Rules 和 Hooks。

## 關鍵要點

- **CLAUDE.md < 200 行**：超過會稀釋模型注意力，導致規則被遺忘
- **Rules 條件載入**：在規則上標記路徑，只有在特定情境才注入 context，節省空間
- **Memory = Claude 的動態筆記**：記臨時狀態、被糾正的行為、進行中的工作，跨對話保留
- **Hooks = 硬性約束**：程式碼層級，100% 觸發，適用於「忘了就代價大」的場景（寄信、刪檔、外洩 API key）
- **漸進式建置**：不需一開始就設 Hooks，從 CLAUDE.md 開始，問題出現再升級
- **全程不手打**：用 `/init`、請 Claude 上網參考別人的設定、對話中累積 → 全由 Claude 代勞

## 此篇與知識庫哪些頁面有關

- [[Claude Code設定四層]]
- [[Context Window]]
- [[AgentCrew Academy]]
- [[Claude-Skill]]
