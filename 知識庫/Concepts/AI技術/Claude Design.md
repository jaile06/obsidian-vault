---
type: concept
aliases: ["Claude Design 功能"]
tags: [AI技術, 設計工具, Claude]
related_concepts: ["[[Claude Code設定四層]]", "[[規範驅動開發SDD]]", "[[多模態]]"]
related_entities: ["[[李哈利Harry]]"]
sources: ["[[李哈利Harry-ClaudeDesign設計師危機]]"]
created: 2026-04-24
updated: 2026-04-24
---

## 定義

Anthropic 推出的 AI 視覺設計工具，底層由 Opus 4.7 驅動，使用者用自然語言描述需求，可一站式生成品牌設計系統、PPT（Slide Deck）、網頁原型（Prototype）、Landing Page 和 App 介面。

## 核心重點

- **Design System 優先**：先建立品牌色票、字體、風格基礎，後續所有生成作品自動保持一致性
- **多元輸入**：支援截圖、Figma 檔、HTML Extractor 抓取代碼、直接輸入網址
- **Tweaks 即時調整**：生成後可在界面用自然語言微調局部元素（顏色、字體、文案、排版）
- **與 Claude Code 整合**：設計完成後可將 HTML/CSS 代碼直接交接給 Claude Code 在本地執行
- **Draw 功能**：可在畫面上圈選區域並給指令，精準調整特定元素
- **限制**：若目標網站有 Cloudflare 保護，HTML 自動抓取可能失敗，需手動貼代碼或改用 URL 輸入

## 不同視角 / 矛盾之處

- **設計師觀點**：one-shot 完成度已相當高，但細節仍需人工調整；工具降低設計門檻同時也對基礎設計工作造成威脅
- **取代爭議**：影片作者認為 AI 不取代設計師職業，但會取代不會用 AI 的設計師
- **vs 其他工具**：與 Lovable、Figma AI 相比，Claude Design 強調品牌系統的一致性管理

## 延伸問題

- Claude Design 與 Figma 的整合深度如何？是否支援雙向同步？
- Opus 4.7 視覺能力與 GPT-4o 或 Gemini Ultra 相比，具體差距在哪？
- 品牌設計系統（Design System）能否匯出為 Figma token 或 CSS 變數？
