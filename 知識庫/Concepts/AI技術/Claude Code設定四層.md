---
type: concept
aliases: ["Claude四層設定", "CLAUDE.md Rules Memory Hooks", "Claude Code 環境設定"]
tags: [AI技術, ClaudeCode, 工具設定, Context-Window]
related_concepts: ["[[Claude-Skill]]", "[[Context Window]]", "[[提示詞工程]]"]
related_entities: ["[[AgentCrew Academy]]"]
sources: ["[[AgentCrewAcademy-Claude四大設定]]"]
created: 2026-04-23
updated: 2026-04-23
---

## 定義

Claude Code 提供四個層次的環境設定，讓規則從「自然語言建議」升級到「程式層強制執行」，解決 Claude 選擇性忘記規則的問題。

## 四層架構

### 1. CLAUDE.md（默契檔）
- 每次 Claude 啟動時自動注入上下文
- 分兩個層級：**user level**（全域，跨所有專案）、**project level**（專案特有）
- 官方建議 < 400 行，實務建議維持 **200 行以下**，避免模型注意力稀釋
- 適合放：身份、語氣偏好、跨專案通用規則、資安底線

### 2. Rules（條件路徑載入）
- 存在 `rules/` 資料夾，每個檔案管一個主題
- 關鍵特性：可設定**只有在特定路徑/檔案類型才載入**，節省 context window
- 適合放：只在某類檔案才需要的規則（如「只有跑 Python 腳本時才套用」）
- CLAUDE.md 超過 200 行時，可請 Claude 自動判斷哪些規則可移至 Rules

### 3. Memory（Claude 自寫的動態狀態）
- Claude 在工作中判斷「值得記住」的事，自動寫入 memory 目錄
- 結構：`memory.md`（主索引）→ 各子檔（按需載入）
- 記錄內容：使用者糾正的行為、臨時狀態（旅行計畫、進行中的案子）、動態偏好
- 與 CLAUDE.md 的差異：CLAUDE.md 是你設定的持久規定；Memory 是 Claude 記錄的動態知識

### 4. Hooks（程式層強制執行）
- 以**程式碼**而非自然語言定義，事件觸發、100% 不被繞過
- 類型：工具使用前攔截、工具使用後檢查、對話開場注入
- 適合場景：寄信/傳訊前強制確認、刪除危險檔案前攔截、API key 防外洩
- 自然語言規則「建議性遵守」；Hooks 是「強制硬擋」

## 進化路徑（實務建議）

```
初期   → /init 生成基礎 CLAUDE.md，邊用邊補規則
中期   → CLAUDE.md 超過 200 行 → 部分規則移至 Rules（條件載入）
進階   → 規則寫了但 Claude 還是忘 → 升級成 Hooks（強制執行）
動態狀態 → 臨時資訊放 Memory，不污染規則層
```

## 不同視角 / 矛盾之處

- Hooks 雖強制，但需要寫程式碼，維護成本高於自然語言規則
- Memory 是自動管理，但 Claude 也提供手動 `/memory` 指令查閱與編輯
- 規則分散在四層後，整體設定的可讀性與維護性需要定期審視

## 延伸問題

- [[Claude-Skill]] 與 Hooks 如何協作？（Skill 觸發 vs Hook 攔截）
- Rules 的條件路徑設定是否與 [[MCP]] 工具觸發整合？
- 何時應該用 Rules 而非 [[Claude-Skill]]？
