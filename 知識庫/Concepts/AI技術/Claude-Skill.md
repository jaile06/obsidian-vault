---
type: concept
aliases: ["Claude Skill", "技能封裝", "Skill"]
tags: [AI技術, Claude-Code, 自動化, 工作流]
related_concepts: ["[[MCP]]", "[[提示詞工程]]", "[[AI確認機制]]", "[[任務拆解]]"]
related_entities: ["[[Paula 寶拉]]", "[[三師爸Sense Bar]]"]
sources: ["[[Paula寶拉-Antigravity Skill設定]]", "[[Claude基本功EP04-NotebookLM五大進階應用]]", "[[GaryChen-HumanSOP轉AgenticWorkflow四步法]]", "[[阿西出海-8個必裝AISkill分類]]"]
created: 2026-04-17
updated: 2026-06-10
---

## 定義

Claude Skill 是將一段經過驗證的多步驟工作流，打包成可被一句話觸發的可重用技能。存成檔案後，只需提及觸發詞，Claude 就會自動執行所有預設步驟。

## 核心重點

- **兩種類型**：
  - **檔案型 Skill**（File-based）：存在本地 skill 資料夾，只能在 Claude Code 中使用，無法在 Claude.ai 網頁版觸發
  - **對話型 Skill**（Conversation-based）：在對話中定義，對話結束即消失
- **建立流程**：先手動完整跑一遍流程 → 確認無誤 → 請 Claude 將流程打包成 Skill 檔案
- **全域 vs 專案**：存在全域 skill 資料夾的 Skill，在任何專案都可觸發；存在專案資料夾的只在該專案有效
- **應用場景**：備課自動化、定期報告生成、筆記入庫流程等重複性多步驟任務

## 不同視角 / 矛盾之處

- Skill 的強大在於「做過一次就不用重做」，但維護成本存在：工具更新或流程變更時需重新驗證
- 過度依賴 Skill 可能讓使用者忘記流程細節，難以處理例外狀況

## 延伸問題

- Skill 與 [[MCP]] 如何協作（Skill 呼叫 MCP 工具）？
- 如何設計 Skill 的觸發詞讓它夠明確但不過於嚴苛？
- [[AI確認機制]] 是否應該內建在 Skill 流程中？
- [[任務拆解]] 中提到 skill 的「防守範圍」要拆多大才合適，如何具體判斷？
