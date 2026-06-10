---
type: source
original_path: "Notes/Clippings/AI 時代非技術人最該學的設計能力：把 Human SOP 變成 Agentic Workflow.md"
author: ["[[Gary Chen]]"]
published: "2026-05-31"
tags: [clippings, AI技術, Agent]
extracted_concepts: ["[[任務拆解]]"]
extracted_entities: ["[[Gary Chen]]"]
created: 2026-06-10
updated: 2026-06-10
---

## 摘要（3 句內）

說明為何把任務整包丟給「mega agent」註定不穩定，並提出將 Human SOP 轉成 Agentic Workflow 的四步方法論：格式標準化、任務拆解與連結、雙向開發、整合與執行環境。最後以「公司內部請求分類系統」為例，示範如何把分類、回覆草稿拆成兩個用 JSON artifact 串接的 skill。

## 關鍵要點

- Human SOP / Skill / Agentic Workflow 三層定義：給人看的流程文件 → 打包給 agent 的執行單位 → 多 skill 串成的生產線
- mega agent 失敗原因：任務太大太模糊，出錯無法定位、無法 review，不具 production 所需的穩定性與可修復性
- 四步法：①格式標準化（參數化 + RFC2119 的 MUST/SHOULD/MAY + 結構化 Markdown）②任務拆解與連結（pipeline step + artifact 串接）③雙向開發（默會知識 Tacit Knowledge 透過迭代補齊）④整合與執行環境（接 [[MCP]] 工具 + human-in-the-loop checkpoint）
- 真實案例：公司內部請求分類系統拆成 internal-request-triage（分類/priority/assignee）與 internal-request-reply-drafting（產生回覆草稿）兩個 skill，用 JSON 串接

## 此篇與知識庫哪些頁面有關

- [[任務拆解]]（新建 Concept，本篇核心方法論）
- [[Claude-Skill]]（skill 的資料夾結構：SKILL.md + references + scripts，與本篇定義一致）
- [[MCP]]（本篇提及作為 agent 統一調用外部工具的協定，並說明 Anthropic 已捐給 Linux Foundation 的 Agentic AI Foundation）
