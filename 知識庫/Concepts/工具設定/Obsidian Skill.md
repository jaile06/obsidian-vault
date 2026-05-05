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
  - '[[Nico投资有道]]'
  - '[[Martina在进化]]'
sources:
  - '[[Paula寶拉-Antigravity Skill設定]]'
  - '[[Nico投资有道-ObsidianClaudian知識庫入門]]'
  - '[[Martina在进化-AI第二大腦告別靈感焦慮]]'
created: '2026-04-17'
updated: '2026-05-05'
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

### Claudian 插件指令系統（Nico 投资有道 / Martina）

另一種 Skill 實作形態：透過 Obsidian 社群插件 Claudian，在知識庫內直接使用斜線指令操控 AI。

| 指令 | 功能 |
|------|------|
| `/ask` | 搜尋知識庫筆記 |
| `/report` | 自動生成週報 |
| `/review` | 定期回顧摘要 |
| `/daily` | 生成每日任務（含昨日未完成事項） |
| `/capture` | 快速捕獲網頁或文字 → 結構化筆記 |

- Claudian 插件尚未上架社群市場，需手動安裝（main.js + manifest.json + styles.css）
- 大陸環境需額外設定代理環境變數（Clash 預設端口 7890）
- 可自訂新 Skill：在對話框描述需求，Claudian 自動產生 skill 配置文件

## 延伸問題

- 如何為自訂工具（如 Dataview、Canvas）撰寫自己的 Skill？
- Skill 與 Prompt 有何差異？何時用 Skill，何時用 Prompt？
- Claudian 的 12 個斜線指令如何對應到五層架構的操作流程？
