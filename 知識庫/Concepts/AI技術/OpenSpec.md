---
type: concept
aliases:
  - OpenSpec
tags:
  - openspec
  - ai-coding
  - spec-driven-development
related_concepts:
  - "[[規範驅動開發SDD]]"
  - "[[Claude-Skill]]"
  - "[[提示詞工程]]"
  - "[[AI確認機制]]"
related_entities:
  - "[[大雷早上好]]"
  - "[[沈弘哲twtrubiks]]"
  - "[[AI超元域]]"
  - "[[为什么叫QQ]]"
  - "[[工程師下班有約]]"
  - "[[ZEDOTECH]]"
sources:
  - "[[大雷-OpenSpec工具評測]]"
  - "[[twtrubiks-OpenSpec公車追蹤器心得]]"
  - "[[AI超元域-OpenSpec規範驅動開發]]"
  - "[[QQ-限制AI自由度AI編程]]"
  - "[[工程師下班有約-ClaudeCode實戰OpenSpec]]"
  - "[[ZEDOTECH-OpenSpec實戰VSCode示範]]"
  - "[[2026-04-23-OpenSpec整合XOOPS開發專案]]"
  - "[[2026-04-23-OpenSpec安裝初始化]]"
created: 2026-04-22
updated: 2026-05-06
---

## 定義

OpenSpec 是一個輕量、開源的規範驅動 AI 編程工作流工具（GitHub: Fission-AI/OpenSpec）。它在你和 AI 動手寫代碼前，先讓雙方對「要做什麼」達成共識，透過結構化的提案與任務追蹤，讓 AI 按規範執行而非自由猜測。

## 核心重點

- **四步核心流程**：`explore`（探索討論）→ `propose`（生成提案文件）→ `apply`（按任務執行）→ `archive`（歸檔，更新主規格書）
- **雙資料夾結構**：`changes/`（進行中的變更）vs. `specs/`（已完成的主規格書）；用 git 類比：changes = feature branch，specs = main branch
- **delta spec**：OpenSpec 獨有設計，用自然語言記錄 add/modify/remove/rename 的變更，類似 git diff
- **archive 機制**：完成後將 changes 搬入 archive，只保留最新主 specs 供 AI 讀取，節省 context window
- **輕量無需 API key**：只需 Node.js 20.19.0+，npm 全局安裝
- **工具無關**：支援 Claude Code、Cursor、Codex、Windsurf、GitHub Copilot 等主流工具
- **適合場景**：現有專案迭代（「從 1 到 N」），比 SpecKit 更適合老專案改造
- **AI 主動提問**：在 explore 階段可讓 AI 主動追問釐清需求，不再由使用者單方面說不清楚；特別適合 PM / 業務等非技術角色
- **知識斷層防護**：每次變更都有文件紀錄，即使關鍵人員離職也不怕系統知識斷層
- **Verify 機制**：apply 完成後執行 `/opsx:verify`，AI 自動比對程式碼與規格，列出 critical / warning / suggestion 三級問題；critical 必修，suggestion 可選（來源：[[ZEDOTECH-OpenSpec實戰VSCode示範]]）
- **每輪開新對話**：做新功能時建議開新 AI 對話視窗，避免上輪對話殘留影響 AI 判斷

## XOOPS 專案整合要點

XOOPS 老舊 PHP CMS 的痛點與 OpenSpec 高度吻合：
- **跨資料夾架構**（class/、admin/、templates/、language/）→ AI 容易亂改，specs 可明確限定範圍
- **老舊慣例多**（XoopsForm、XoopsObject、XoopsHandler）→ 寫入 specs/xoops-convention.md 讓 AI 遵守
- **需求持續追加**（客戶上線後不斷改）→ delta spec 確保每次變更都有文件

安裝方式：`npm install -g openspec`（需 Node.js 18+），初始化：`npx openspec init`

## 不同視角 / 矛盾之處

- **vs. SpecKit**：SpecKit 適合從零開始；OpenSpec 適合既有專案。SpecKit 文件輸出量大，容易讓人放棄；OpenSpec 更輕量，完整走完流程的成功率較高
- **不是每個改動都要走流程**：小 bug 修正只需 git commit 記錄即可，避免過度儀式化
- **兩種使用策略**：①完整走四步；②只用 propose 產出文件，自行用 AI 執行（不依賴 OpenSpec 後續指令）

## 延伸問題

- OpenSpec 與 AGENTS.md / CLAUDE.md 的關係？（OpenSpec init 會生成 AI 工作指南，與 AGENTS.md 概念重疊）
- delta spec 的自然語言版本控制是否可取代部分 git commit message 的功能？
- 在知識庫工作流（非軟體開發）中，SDD 概念是否適用？
