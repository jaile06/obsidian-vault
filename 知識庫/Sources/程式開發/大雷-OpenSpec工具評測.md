---
type: source
original_path: "Notes/Clippings/OpenSpec：让AI按规范写代码的革命工具 OpenSpec The Revolutionary Tool That Makes AI Write Spec-Driven Code.md"
author:
  - "[[大雷早上好]]"
published: "2025-10-12"
tags:
  - openspec
  - spec-driven-development
  - ai-coding
extracted_concepts:
  - "[[OpenSpec]]"
  - "[[規範驅動開發SDD]]"
extracted_entities:
  - "[[大雷早上好]]"
---

## 摘要（3 句內）

OpenSpec 是針對「現有專案迭代」痛點設計的規範驅動開發工具，比 SpecKit 更適合已有代碼的專案改造。它採用雙資料夾結構（changes / specs）分離「當前狀態」與「變更計畫」，確保每次迭代清晰可追溯。實測以 AI 內容偵測工具為案例，從零到完整產品僅花費幾十美分。

## 關鍵要點

- **與 SpecKit 的核心差異**：SpecKit 只適合從零開始的新專案；OpenSpec 專治老專案改造，雙資料夾結構擴展性更強
- **安裝門檻低**：需 Node.js 20.19.0+，`npm` 全局安裝，無需 API key
- **初始化向導**：支援 GitHub Copilot、Cursor、Claude Code、Kilo code 等主流工具選擇
- **工作流程**：填充專案上下文 → 建立變更提案 → AI 產出詳細計畫書 → 逐項執行任務
- **`openspec view` 指令**：終端機實時顯示任務進度條
- **成本優勢**：同等開發量比傳統方式節省 10x 以上（幾十美分 vs. 幾美元）
- **定位**：「給 AI 開發團隊配備的項目經理」

## 此篇與知識庫哪些頁面有關

- [[OpenSpec]] — 本篇核心工具
- [[規範驅動開發SDD]] — 方法論背景
- [[Claude-Skill]] — OpenSpec init 會將 skill 注入 AI 編碼工具設定資料夾
