---
type: source
original_path: "Notes/Clippings/xoops_task_template.md"
author: []
published: ""
tags:
  - 程式開發
  - XOOPS
  - 提示詞工程
extracted_concepts:
  - "[[XOOPS開發規範]]"
  - "[[提示詞工程]]"
extracted_entities:
  - "[[XOOPS]]"
created: 2026-04-23
updated: 2026-04-23
---

## 摘要（3 句內）

配合三種 XOOPS 2.5 專用 Prompt 使用的任務單範本集，共五種格式（通用完整版、簡短版、新增功能版、重構版、修 Bug 版）。使用方式：先貼對應 Prompt，再貼任務單並填入模組名稱、檔案路徑、問題描述與需求。範本結構化欄位涵蓋資料表異動、UI 需求、已知錯誤訊息等，引導完整描述任務。

## 關鍵要點

- **五種任務單格式：** 通用完整 / 簡短 / 新增功能專用 / 重構專用 / 修 Bug 專用
- **必填核心欄位：** 任務類型、模組名稱、處理檔案、現況描述、需求說明
- **選填欄位：** 資料表資訊、權限與流程要求、UI 需求、已知錯誤訊息、其他限制
- **使用方式：** Prompt → 任務單（依情境選版本）→ AI 依固定格式輸出
- **固定輸出格式：** Schema Map / Logic Flow / PHP / TPL / JavaScript / Security Check

## 此篇與知識庫哪些頁面有關

- [[XOOPS-PromptKit-三種開發Prompt]] — 搭配使用的 Prompt 本體
- [[XOOPS開發規範]] — 任務單隱含的開發規範前提
- [[提示詞工程]] — 任務單為結構化 Prompt 的輸入設計
- [[XOOPS]] — 目標平台
