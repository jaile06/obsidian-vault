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
related_entities: []
sources:
  - "[[twtrubiks-OpenSpec公車追蹤器心得]]"
  - "[[QQ-限制AI自由度AI編程]]"
  - "[[大雷-OpenSpec工具評測]]"
created: 2026-04-22
updated: 2026-04-22
---

## 定義

規範驅動開發（Spec-Driven Development, SDD）是一種 AI 輔助開發哲學：**先有規格，才有代碼**。核心主張是透過「限制 AI 的自由度」——流程化、規範化、可驗證化——換取輸出的可控性與可稽核性。

## 核心重點

- **反直覺洞見**：最聰明的 AI 編程方式不是給 AI 最大自由度，而是透過結構化約束讓 AI 更可靠
- **三化原則**：流程化（固定執行步驟）、規範化（書面共識文件）、可驗證化（任務清單可逐項確認）
- **與 AI 確認機制的共同精神**：先提案再執行，人類在代碼動手前審查計畫，保留決策控制權
- **典型工具**：[[OpenSpec]]（輕量、適合現有專案）、SpecKit（適合新專案）、gstack、Superpowers
- **適用場景**：中大型功能迭代、跨越多個 session 的長期開發、需要審計軌跡的團隊協作

## 不同視角 / 矛盾之處

- **成本 vs. 收益**：走完完整 SDD 流程需要時間；小修正、小 bug 不值得走流程，需要判斷粒度
- **文件負擔**：部分工具（如 SpecKit）產出文件量過大，反而降低執行意願；輕量工具（如 OpenSpec）更實際
- **與 vibe coding 的對比**：vibe coding 強調快速直覺式生成；SDD 強調可控、可追溯，兩者代表不同的 AI 協作哲學

## 延伸問題

- SDD 的規格書（spec）與傳統軟體需求文件（PRD、User Story）的關係？
- SDD 能否應用到非軟體領域（如知識庫管理、內容創作工作流）？
- 在 AI 能力不斷提升的情況下，SDD 的必要性會增加還是降低？
