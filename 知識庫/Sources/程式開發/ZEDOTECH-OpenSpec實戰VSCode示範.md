---
type: source
original_path: "Notes/Clippings/未來的程式開發？用 OpenSpec + AI，在 VS Code 幾乎不用寫程式.md"
author:
  - "[[ZEDOTECH]]"
published: 2026-03-10
tags:
  - openspec
  - spec-driven-development
  - ai-coding
  - claude-code
extracted_concepts:
  - "[[OpenSpec]]"
  - "[[規範驅動開發SDD]]"
  - "[[Claude-Skill]]"
extracted_entities:
  - "[[ZEDOTECH]]"
---

## 摘要（3 句內）

ZEDOTECH 頻道 Nicky 以實作方式示範在 VS Code 搭配 Claude Code 使用 OpenSpec 建立 C# 電商後台管理系統。完整走完兩輪 explore → ff → apply → verify → archive 開發循環，展示 Task 勾選機制、Verify 報告與 archive/sync 流程。是目前最完整的 OpenSpec 中文實作示範影片。

## 關鍵要點

- **SDD 四步核心**：explore（討論需求）→ ff（生成 Proposal/Design/Task 三文件）→ apply（依規格實作）→ archive（封存，同步主規格庫）
- **Verify 機制**：apply 完成後執行 `/opsx:verify`，AI 自動比對程式碼與規格，列出 critical / warning / suggestion；critical 必修，suggestion 可選
- **Task 勾選工作流**：AI 完成的自動打勾（`xxx`），需人工驗收的由開發者手動勾選
- **archive/sync 差異**：archive 是封存當次 change；sync 是將 delta spec 同步回外層主規格資料夾，保持主規格庫與實作一致
- **90% 不用手寫程式**：Nicky 自述過去一兩個月搭配 OpenSpec 開發，90% 情況下不再需要手寫任何一行程式
- **每輪開新對話**：做新功能時建議開新 Claude Code 對話視窗，避免上輪對話影響 AI 認知
- **實作細節**：watch run 會因上傳檔案觸發 hot reload 導致頁面遮罩，建議改用 `dotnet run`

## 此篇與知識庫哪些頁面有關

- [[OpenSpec]]：最完整中文操作示範，補充 Verify 報告、Task 勾選、archive/sync 實際行為
- [[規範驅動開發SDD]]：具體展示 SDD 四步流程圖，explore/ff/apply/archive 一一對應
- [[Claude-Skill]]：本影片使用 Claude Code 作為 AI 執行工具
- [[大雷-OpenSpec工具評測]]、[[twtrubiks-OpenSpec公車追蹤器心得]]、[[AI超元域-OpenSpec規範驅動開發]]、[[工程師下班有約-ClaudeCode實戰OpenSpec]]：同主題其他 OpenSpec 來源
