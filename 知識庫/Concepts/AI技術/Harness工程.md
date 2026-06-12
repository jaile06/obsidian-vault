---
type: concept
aliases: [Harness Engineering, Agent Harness, 代理工作框架]
tags: [AI技術, Agent, 自動化, 工作流]
related_concepts: ["[[Claude-Skill]]", "[[Evals]]", "[[AI確認機制]]", "[[任務拆解]]", "[[規範驅動開發SDD]]"]
related_entities: ["[[Nick Nisi]]"]
sources: ["[[AIEngineer-NickNisi-刪除95%AgentSkills]]"]
created: 2026-06-12
updated: 2026-06-12
---

## 定義

Harness 工程是把 AI agent 包進一層程式化外框（狀態機、關卡、驗證器），用**程式碼強制**流程推進，而非靠 prompt 拜託模型遵守。核心信條：agent 犯錯不是去修它產出的 code，而是修 harness，讓同樣的錯誤在系統層面不可能再發生。

## 核心重點

- **Enforce, don't instruct**：prompt 指示可以被模型遺忘或「決定不做」；狀態機關卡在模型決策之外，verifier 沒通過就是進不了下一階段
- **證據取代信任**：每個階段必須交出不可造假的證據——測試輸出做 SHA-256 雜湊驗證、UI 修復附 Playwright 前後錄影；設計原則是「讓真的做事比說謊更容易」
- **Case 實例**：Nick Nisi 的 harness 含 5 個 agent（implementer / verifier / reviewer / closer / retro），以 TypeScript 狀態機串接；最重要的不是 agent 而是 agent 之間的 gates
- **失敗即 harness 的 bug**：每次失敗都成為下一輪的資料；retro agent 分析 transcript（是否 doom loop、重複呼叫同一工具），寫入分框架的 memory 檔（通用 / Next.js / TanStack Start…）
- **起點是 Claude skill 的極限**：Case 原本是一個 skill，複雜化後出現 context drop（忘記步驟、跳過任務），才改建為外部狀態機——skill 適合輕量流程，重流程需要 harness

## 不同視角 / 矛盾之處

- 與 [[AI確認機制]] 同樣不信任 AI 全自動，但手段相反：范凱靠**人工**看一眼確認，harness 工程靠**程式碼**自動驗證——前者保留人類判斷，後者追求無人值守的規模化
- 建 harness 本身是不小的工程投資，單人輕量工作流未必划算

## 延伸問題

- 本庫的 ingest 流程（提案→確認→執行）能否部分 harness 化，例如自動驗證 index 計數與 Archive 完成？
- 狀態機關卡與 [[Claude-Skill]] 的觸發機制如何混搭？
- retro agent 的自動記憶更新與 Claude 的 memory 機制有何異同？
