---
type: source
original_path: "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill"
author: []
published: ""
tags: [網站設計, AI技術, UI設計, 配色, Claude-Skill]
extracted_concepts: ["[[AI設計系統生成]]", "[[網站配色系統]]"]
extracted_entities: ["[[UI-UX-Pro-Max]]"]
created: 2026-06-11
updated: 2026-06-11
---

## 摘要（3 句內）

UI UX Pro Max 是一個 AI 設計系統生成 skill 套件（MIT License），以 CSV 資料庫＋Python 搜尋引擎驅動，依產業類別秒速生成完整設計系統。核心資料：161 個產業推理規則、161 組產業對應色板、67 種 UI 樣式、57 組 Google Fonts 字體配對、99 條 UX 指南（含反模式）。採三層推理流程：多域並行搜尋 → 推理引擎（產業規則＋BM25 排序＋反模式過濾）→ 輸出驗證（交付前檢查清單）。

## 關鍵要點

- **資料驅動而非自由發揮**：色板、字體、樣式全部來自結構化 CSV 資料庫，依產業類別（SaaS、金融、醫療、電商、教育…）檢索
- **三層推理流程**：①多域搜尋（產品類型/樣式/色板/模式/字體 5 維並行）②推理引擎（產業規則、BM25、反模式過濾）③輸出驗證（易用性、響應式、焦點狀態檢查清單）
- **產業 × 情感配色**：案例 "Serenity Spa" — 柔和粉(#E8B4B8)＋鼠尾草綠(#A8D5BA)＋金(#D4AF37)，字體 Cormorant Garamond＋Montserrat，反模式為霓虹色與刺眼動畫
- **反模式是一等公民**：每個產業規則同時定義「該做」與「不該做」
- **架構**：`data/`（CSV）＋ `scripts/search.py`（生成引擎）＋ `templates/`（平台範本），支援 15 個技術棧
- 使用：`uipro init --ai claude` 安裝後自然語言觸發，或 CLI 直接呼叫 search.py

## 此篇與知識庫哪些頁面有關

- [[AI設計系統生成]]（新建 Concept，本篇為資料驅動派代表）
- [[UI-UX-Pro-Max]]（工具 Entity）
- [[網站配色系統]]（產業導向色板補充既有五色角色方法）
- [[Claude-Skill]]（第三方 skill 生態的實例：SKILL.md＋data＋scripts 結構）
- [[任務拆解]]（三層推理流程同樣是 pipeline＋artifact 思維）
