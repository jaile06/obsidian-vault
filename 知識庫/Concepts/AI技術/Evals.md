---
type: concept
aliases: [Eval, AI評測, 評估驅動]
tags: [AI技術, 測試, Agent, 量測]
related_concepts: ["[[Claude-Skill]]", "[[Harness工程]]", "[[Context Window]]", "[[提示詞工程]]"]
related_entities: ["[[Nick Nisi]]"]
sources: ["[[AIEngineer-NickNisi-刪除95%AgentSkills]]"]
created: 2026-06-12
updated: 2026-06-12
---

## 定義

Evals（評測）是對 LLM / agent 任務反覆執行同一組情境並量測正確率的測試方法。因為 AI 是非確定性程式，「看起來有效」不可信，唯有量測才能知道一個 prompt、skill 或 context 的改動讓表現變好還是變差。

## 核心重點

- **反直覺發現**：Nick Nisi 用 eval 量測發現，載入 docs 生成的 skill 後任務正確率 77%，不載入反而 97%——更多 context 主動讓模型變笨（wild goose chase）
- **量測前不可知**：這種退化沒有任何錯誤訊息，不跑 eval 完全看不見；「我以為加了一堆東西更好」是常見錯覺
- **eval 也量成本**：刪掉 95% skills 後，單輪 eval 時間從 68 分鐘降到 6 分鐘，token 消耗大幅下降
- **工具支援**：Claude 已有現成的 eval skill，可自動建立評測、產出 HTML 並排報告（載入 skill vs 不載入的對照）
- **應用準則**：對 agent-facing 產品，用 eval 找出模型「穩定犯錯」的點，只針對那些點寫 gotchas

## 不同視角 / 矛盾之處

- 「加更多說明會更好」的直覺 vs 量測結果「精簡 gotchas 勝過全量文件」——兩者僅能靠 eval 裁決
- eval 本身有建置成本，小型個人工作流是否值得建完整 eval，仍是取捨

## 延伸問題

- 個人知識庫的 Skill（如本庫 Skill 1–4）能否設計輕量 eval 驗證流程品質？
- eval 情境要多少組才有統計意義？
- [[Harness工程]] 的 retro agent 自動分析 transcript，能否取代部分人工 eval？
