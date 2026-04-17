---
type: concept
aliases:
  - Skill
  - AI技能文件
  - skills.md
tags:
  - AI筆記
  - Obsidian
  - Antigravity
  - 工具設定
related_concepts:
  - '[[Markdown語法]]'
  - '[[提示詞工程]]'
related_entities:
  - '[[Paula 寶拉]]'
sources:
  - '[[Paula寶拉-Antigravity Skill設定]]'
created: '2026-04-17'
updated: '2026-04-17'
---

## 定義

Skill 是一份教學文件，用來告訴 AI 你所使用的工具有哪些特殊語法與功能。放在固定位置後，AI 在處理相關任務時會自動讀取，並按照文件內容輸出正確格式，而不只是輸出基本 Markdown。

## 核心重點

### Skill 檔案結構

```
---
name: Obsidian Markdown
description: 當使用者要求整理筆記、建立 Obsidian 頁面時使用
---

（語法規則與使用範例的 Markdown 正文）
```

### 存放路徑

```
.agent/
└── skills/
    └── obsidian-markdown/
        └── skill.md
```

### Obsidian Markdown Skill 教會 AI 使用的三個功能

| 功能 | 語法 | 效果 |
|------|------|------|
| Callout | `> [!warning] 標題` | 視覺獨立的警告區塊，快速瀏覽時立即抓眼 |
| Task List | `- [ ] 待辦事項` | 可互動的勾選清單，筆記本身即行動清單 |
| FrontMatter | `---` YAML 區塊 | 結構化 metadata，解鎖 Dataview 過濾與搜尋 |

### 取得方式

- **Skills Marketplace**（skillsmp.com）：28萬+ 開源 Skill，支援 AI 語意搜尋
- **自訂**：在 `.agent/skills/<資料夾名稱>/skill.md` 寫入自己的規則與範例

## 不同視角 / 矛盾之處

- Skill 只提供語法說明，AI 仍需理解情境才能在適當位置套用（e.g. 不會對所有內容都加 Callout）
- 效果依賴 AI 模型的理解能力，不同模型結果可能有差異

## 延伸問題

- 如何為自訂工具（如 Dataview、Canvas）撰寫自己的 Skill？
- Skill 與 Prompt 有何差異？何時用 Skill，何時用 Prompt？
