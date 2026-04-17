---
type: concept
aliases: [Markdown, md語法]
tags: [寫作工具, 技術文件, Obsidian]
related_concepts: []
related_entities: []
sources: ["[[Markdown語法指南]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

輕量級標記語言，用簡單符號實現文字排版，最終渲染為 HTML。廣泛用於技術文件、筆記軟體（如 Obsidian）、GitHub 等平台。

## 核心重點

| 語法 | 效果 |
|------|------|
| `# 標題` | H1～H6（# 數量對應層級） |
| `**文字**` | 粗體 |
| `*文字*` | 斜體 |
| `- 項目` | 無序列表 |
| `1. 項目` | 有序列表 |
| `[文字](URL)` | 超連結 |
| `![說明](網址)` | 圖片 |
| `> 文字` | 引用 |
| ` ```php ` | PHP 語法高亮程式碼區塊 |
| `\| 欄 \| 欄 \|` | 表格 |

## Obsidian 擴充語法

| 語法 | 效果 |
|------|------|
| `[[頁面名稱]]` | 雙向連結（WikiLink） |
| `> [!note] 標題` | Callout 區塊（info / warning / tip / danger 等類型） |
| `- [ ] 待辦` | 可互動的 Task List |
| YAML FrontMatter（`---` 包圍） | 結構化 metadata，支援 Dataview 查詢 |

詳細 Obsidian 語法使用規範，見 → [[Obsidian Skill]]

## 不同視角 / 矛盾之處

- 各平台對 Markdown 的支援略有差異（如 Obsidian 支援 `[[雙中括號連結]]`，但標準 Markdown 不支援）
- 同樣的 Markdown 檔案，在 Obsidian vs GitHub vs HackMD 渲染結果可能不同

## 延伸問題

- 如何讓 AI 自動使用 Obsidian 擴充語法？→ [[Obsidian Skill]]
