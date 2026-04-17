---
type: source
original_path: Notes/Clippings/Antigravity 實戰：無痛設定 Skills ，直出結構化筆記.md
author:
  - '[[Paula 寶拉]]'
published: '2026-03-01'
tags:
  - Obsidian
  - AI筆記
  - Skill
  - Antigravity
  - Claude
extracted_concepts:
  - '[[Obsidian Skill]]'
  - '[[Markdown語法]]'
extracted_entities:
  - '[[Paula 寶拉]]'
---

## 摘要（3 句內）

AI 預設只會輸出基本 Markdown，因為它不知道你在用哪種工具。Skill 是一份放在固定位置的教學文件，讓 AI 在處理任務前先讀取，進而主動使用 Obsidian 的 Callout、Task List、FrontMatter 等功能。從 Skills Marketplace 找到現成 Skill、複製到 `.agent/skills/` 資料夾，不需安裝任何套件即可生效。

## 關鍵要點

- **Skill 本質**：YAML FrontMatter（name + description）+ Markdown 正文（語法規則與範例）
- **存放位置**：`.agent/skills/<skill-name>/skill.md`
- **自動偵測**：AI 處理相關任務時自動讀取，無需手動指定
- **差異一 Callout**：重要提醒從條列項目改為視覺獨立的 `> [!warning]` 區塊
- **差異二 Task List**：代辦事項從靜態表格改為可勾選的 `- [ ]` 清單，開完會直接運作
- **差異三 FrontMatter**：自動補上日期、tag、status，解鎖 Dataview 過濾與搜尋
- **來源**：Skills Marketplace（skillsmp.com），28萬+ 開源 Skill
- **限制**：Skill 僅說明語法規則，AI 仍需理解情境才能正確套用

## 此篇與知識庫哪些頁面有關

- [[Obsidian Skill]]
- [[Markdown語法]]
- [[Paula 寶拉]]
