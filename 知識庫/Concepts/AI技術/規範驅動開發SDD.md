---
type: concept
aliases:
  - SDD
  - Spec-Driven Development
  - 規範驅動開發
tags:
  - spec-driven-development
  - ai-coding
  - ai-workflow
related_concepts:
  - "[[OpenSpec]]"
  - "[[AI確認機制]]"
  - "[[提示詞工程]]"
  - "[[Claude-Skill]]"
related_entities:
  - "[[Konrad Kokosa]]"
sources:
  - "[[twtrubiks-OpenSpec公車追蹤器心得]]"
  - "[[QQ-限制AI自由度AI編程]]"
  - "[[大雷-OpenSpec工具評測]]"
  - "[[KokosaKonrad-dotLLM-CSharp推理引擎]]"
  - "[[ZEDOTECH-OpenSpec實戰VSCode示範]]"
created: 2026-04-22
updated: 2026-04-23
---

## 定義

規範驅動開發（Spec-Driven Development, SDD）是一種 AI 輔助開發哲學：**先有規格，才有代碼**。核心主張是透過「限制 AI 的自由度」——流程化、規範化、可驗證化——換取輸出的可控性與可稽核性。

## 核心重點

- **反直覺洞見**：最聰明的 AI 編程方式不是給 AI 最大自由度，而是透過結構化約束讓 AI 更可靠
- **三化原則**：流程化（固定執行步驟）、規範化（書面共識文件）、可驗證化（任務清單可逐項確認）
- **與 AI 確認機制的共同精神**：先提案再執行，人類在代碼動手前審查計畫，保留決策控制權
- **典型工具**：[[OpenSpec]]（輕量、適合現有專案）、SpecKit（適合新專案）、gstack、Superpowers
- **適用場景**：中大型功能迭代、跨越多個 session 的長期開發、需要審計軌跡的團隊協作

## AI 輔助開發方法論（補充自 dotLLM 案例）

[[Konrad Kokosa]] 以兩個月獨立完成系統級 C# LLM 推理引擎 [[dotLLM]]，驗證了「文件即方法論」的核心命題：

- **ROADMAP.md 是最高 ROI 投資**：~60 個步驟分 7 個 Phase，每步有明確範圍、依賴與接受標準。沒有 Roadmap，AI 就沒有方向感，會重複做錯方向的事
- **CLAUDE.md（或 AGENTS.md）是 AI 憲章**：180+ 行定義 AI 的工作邊界與編碼規範，加上 22 份子系統設計文件；AI 實作前必讀相關設計文件
- **計畫與執行分離**：`/plan-step` 進入 Plan Mode，人工確認後才執行；這與 [[AI確認機制]] 的「先提案再執行」完全一致
- **雙模型 PR 審查**：Claude 實作、Codex + Gemini 獨立審查；不同模型有不同盲點（Codex 善找邏輯 bug，Gemini 善發現架構問題），互補形成安全網
- **自定義 Skill 自動化循環**：6 個 Claude Code Skill（`/plan-step`、`/create-pr`、`/apply-pr-comments` 等）讓從規劃到 merge 的整個循環可重複執行
- **AI 的極限**：架構抉擇、暫存器層級效能調教仍需人類判斷；「避免 compound tool calls」這類行為約束屢次提醒仍會失效

## 不同視角 / 矛盾之處

- **成本 vs. 收益**：走完完整 SDD 流程需要時間；小修正、小 bug 不值得走流程，需要判斷粒度
- **文件負擔**：部分工具（如 SpecKit）產出文件量過大，反而降低執行意願；輕量工具（如 OpenSpec）更實際
- **與 vibe coding 的對比**：vibe coding 強調快速直覺式生成；SDD 強調可控、可追溯，兩者代表不同的 AI 協作哲學
- **工具 vs. 自建結構**：OpenSpec 提供現成工具；dotLLM 案例則是用 ROADMAP.md 自建結構，效果相當——核心是「結構本身」而非哪個工具

## 延伸問題

- SDD 的規格書（spec）與傳統軟體需求文件（PRD、User Story）的關係？
- SDD 能否應用到非軟體領域（如知識庫管理、內容創作工作流）？
- 在 AI 能力不斷提升的情況下，SDD 的必要性會增加還是降低？
- ROADMAP.md 驅動開發 vs. OpenSpec 工具驅動開發：前者更靈活，後者更標準化，如何選擇？
- 雙模型審查（Codex + Gemini）是否有成本效益的替代方案？
