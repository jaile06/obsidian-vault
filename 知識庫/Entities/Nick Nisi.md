---
type: entity
role: "WorkOS DX 工程師 / AI Engineer 講者"
tags: [人物, AI技術, Agent]
related_concepts: ["[[Harness工程]]", "[[Evals]]", "[[Claude-Skill]]"]
sources: ["[[AIEngineer-NickNisi-刪除95%AgentSkills]]"]
created: 2026-06-12
updated: 2026-06-12
---

## 簡介

WorkOS（身分驗證 / AuthKit 服務商）的 Developer Experience 工程師，維護 20+ repo、橫跨 8 種語言的 SDK。自稱 8 個月沒有親手寫過一行程式碼，全部透過 agent 完成再人工 review。X/GitHub：@nicknisi。

## 主要觀點與貢獻

- 建立個人 harness「Case」：TypeScript 狀態機串接 5 個 agent，每階段須交出證據（SHA-256 驗證測試輸出、Playwright 錄影）才能推進
- 「刪掉 95% skills 反而變強」實驗：1 萬行 docs 生成 skills 使正確率 97%→77%，改為 553 行手寫 gotchas 後回升，eval 時間 68→6 分鐘
- 三原則：Enforce, don't instruct / Guide, don't prescribe / Measure, don't assume
- 「模型已經會寫程式，只需要知道地雷在哪」——對 agent-facing 產品只寫穩定犯錯點的 gotchas

## 與其他人物的關聯

- [[Jim AI Notebook]] 製作了此演講的中文導讀
- 引用 Ryan Lepollo 的 harness engineering 思想（只修 harness、不修 code）
