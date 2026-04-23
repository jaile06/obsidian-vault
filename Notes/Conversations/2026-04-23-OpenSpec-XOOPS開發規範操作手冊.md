---
title: "OpenSpec × XOOPS 開發規範操作手冊"
date: 2026-04-23
tags:
  - openspec
  - xoops
  - spec-driven-development
  - 操作手冊
related_concepts:
  - "[[OpenSpec]]"
  - "[[XOOPS開發規範]]"
  - "[[規範驅動開發SDD]]"
related_templates:
  - "[[OpenSpec-XOOPS-convention]]"
  - "[[OpenSpec-delta-spec-範本]]"
---

# OpenSpec × XOOPS 開發規範操作手冊

> **閱讀對象**：要用 AI 協作開發 XOOPS 2.5 模組的開發者
> **使用前提**：已有 openspace-sample 工作區（含 `.claude/skills/` 與 `openspec/` 目錄）

---

## 概念地圖

```
openspace-sample/                  ← Claude Code 工作區（已建好，不要重建）
├── .claude/skills/                ← /explore /propose /apply /archive 指令
└── openspec/
    ├── specs/
    │   └── convention.md          ← 「憲法」：AI 每次必讀的永久規範（你來填）
    ├── changes/
    │   ├── feature-審核機制/
    │   │   ├── spec.md            ← 這次要做什麼（你填）
    │   │   └── tasks.md           ← 拆解成哪些步驟（AI 產）
    │   └── fix-登入錯誤/
    │       └── spec.md
    └── config.yaml

www2/modules/your_module/          ← 你的 XOOPS 實際程式碼（另一個位置）
```

**工作節奏**：

```
第一次使用（一次性）          每次新功能
────────────────             ──────────────────────────────────
填 convention.md             /explore → /propose → /apply → /archive
（複製範本到 openspec/specs/）    ↑確認           ↑審閱spec
                                 你             你
```

---

## 第一章：初始設定（一次性）

> **前提**：openspace-sample 工作區已建好（含 `.claude/skills/` 與 `openspec/` 目錄）。
> 不需要執行 `npx openspec init`，結構已存在。

### 1-1 確認工作區結構

確認以下路徑存在：

```
openspace-sample/
├── .claude/skills/           ← 有 openspec-* 資料夾
└── openspec/
    ├── specs/                ← 空的，等你放 convention.md
    ├── changes/
    └── config.yaml
```

### 1-2 填寫主規格書

在 `openspace-sample/openspec/specs/` 新建 `convention.md`，從 Obsidian vault 複製 [[OpenSpec-XOOPS-convention]] 範本內容貼入。

**必須立刻填寫的欄位（其餘可之後補）：**

```markdown
## 1. 專案資訊
| 模組名稱 | your_module_name |   ← 填 dirname，例如：tadtools
| XOOPS 版本 | 2.5.x |
| PHP 版本 | 7.4 |          ← 依伺服器實際環境
```

**第 8 章「AI 禁止事項」最重要**，先確認這六條都在：

- [ ] 禁止直接 echo HTML
- [ ] 禁止用 class / namespace
- [ ] 禁止用 PDO / mysqli_ 直接操作資料庫
- [ ] 禁止用原生 `confirm()` / `alert()`（用 SweetAlert）
- [ ] 禁止省略 XOOPS_TOKEN 驗證（後台 POST）
- [ ] 禁止硬寫中文字串（放語言包）

### 1-3 提交初始規格書

```bash
git add openspec/specs/
git commit -m "chore: add OpenSpec convention spec"
```

---

## 第二章：開發新功能（每次流程）

### 完整流程圖

```
你想做一個新功能
        │
        ▼
   [Step 1] /explore
        │  AI 問你：目標是什麼？影響哪些檔案？
        │  你回答，直到 AI 說「我理解了」
        ▼
   [Step 2] /propose
        │  AI 產出 changes/feature-xxx/spec.md
        │          ├─ 目標
        │          ├─ 影響檔案清單（ADD/MODIFY/DELETE）
        │          └─ 不影響範圍
        │
        ▼ ← 你讀 spec.md，確認範圍正確
        │
   [Step 3] /apply
        │  AI 依 spec.md 逐步執行
        │  每完成一個 task → git commit
        ▼
   [Step 4] /archive
           AI 將 changes/feature-xxx/ 歸檔
           你更新 specs/convention.md（若有新發現的慣例）
```

### Step 1 詳解：/explore

**目的**：讓 AI 問清楚，避免範圍模糊導致亂改。

範例對話：

```
你：/explore 我要新增留言審核功能

AI：我有幾個問題：
    1. 審核是管理員逐筆核准，還是可以批次？
    2. 留言現在存在哪個資料表？有 status 欄位嗎？
    3. 核准後前台是立即顯示，還是需要重新整理？

你：批次核准。資料表是 xoops_mymod_comments，有 status 欄位（0=待審 1=通過）。
    核准後立即顯示。

AI：我理解了，可以進行 /propose。
```

**什麼時候繼續**：AI 說「我理解了」或你覺得沒有模糊點時。

### Step 2 詳解：/propose

**目的**：產出可審閱的 spec，讓你確認 AI 理解正確再動程式碼。

產出的 `changes/feature-comment-moderation/spec.md` 範例：

```markdown
## 目標
管理員可在後台批次核准或刪除待審核留言，核准後前台立即顯示。

## 影響範圍
- MODIFY: admin/main.php → 新增審核列表頁籤與批次操作
- MODIFY: templates/mymod_admin_main.html → 新增審核 UI
- MODIFY: language/zht/admin.php → 新增審核相關語言常數

## 不影響範圍
- 前台留言表單 UI 不變
- 資料庫結構不變（沿用 status 欄位）
- Email 通知功能不在本次範圍
```

**審閱重點**：

| 看什麼 | 為什麼重要 |
|--------|-----------|
| 不影響範圍 | 確認 AI 不會動到你不想改的地方 |
| 影響檔案清單 | 確認沒有遺漏，也沒有多餘 |
| 目標描述 | 確認 AI 理解的需求和你的一致 |

**有問題時**：直接跟 AI 說「這裡不對，應該是...」，重新 `/propose`，不要直接 `/apply`。

### Step 3 詳解：/apply

**目的**：逐步執行 spec.md 中的每個 task。

**操作原則**：

```bash
# AI 每完成一個 task，你就：
git add -p                    # 確認變更內容
git commit -m "feat: [描述]"  # 提交

# 好處：出問題可以精確 git revert 到任何一步
```

**遇到 AI 出現錯誤（違反規範）時**：

```
你：等等，這裡直接 echo HTML 了，違反 convention.md 第 3.4 條

AI：抱歉，我修正成 $xoopsTpl->assign() 方式...
```

不要讓 AI 繼續，先修正這個 task 再繼續下一個。

### Step 4 詳解：/archive

**目的**：整理本次開發的成果，更新長期規範。

執行後：
- `changes/feature-xxx/` 被標記為 `done`
- 詢問你是否有新慣例要加進 `specs/convention.md`

**什麼值得加進 convention.md**：

| 值得加 | 不用加 |
|--------|--------|
| AI 犯過的錯（違反規範） | 這次功能的業務邏輯 |
| 你發現的新 XOOPS 慣例 | 暫時性的決定 |
| 本次確立的命名規則 | 可從程式碼看出的東西 |

---

## 第三章：修 Bug 流程（快速通道）

修 bug 不需要 `/propose`，流程縮短為：

```
/explore  →  你說明 bug 現象與錯誤訊息  →  /apply
```

### 建立 Bug Spec

複製 [[OpenSpec-delta-spec-範本]] 並填寫：

```markdown
# changes/fix-[bug簡述]/spec.md

## 問題描述
[錯誤訊息或現象]

## 重現步驟
1. ...
2. ...

## 預期行為
[應該要發生什麼]

## 影響範圍
- MODIFY: [檔案] → [修改說明]

## 不影響範圍
- [確認其他功能不受影響]
```

### 提供給 AI 的關鍵資訊

```
1. 錯誤訊息（完整，包含行號）
2. 發生頁面的 URL
3. 觸發操作（點了什麼、送出了什麼）
4. 最近有沒有修改過相關程式碼
```

---

## 第四章：重構流程

重構最需要「不影響範圍」寫清楚，避免 AI 改壞現有功能。

```markdown
# changes/refactor-[描述]/spec.md

## 目標
[為什麼要重構，例：某函式超過 300 行，拆分提高可讀性]

## 影響範圍
- MODIFY: [檔案] → [重構說明]

## 不影響範圍（重構的黃金規則）
- 所有對外行為不變（輸入/輸出相同）
- 資料庫操作邏輯不變
- 前台顯示效果不變

## 驗收條件
- [ ] 所有原有測試通過
- [ ] 後台功能正常
- [ ] 前台顯示正常
```

---

## 第五章：維護 convention.md

### 何時更新

| 時機 | 更新內容 |
|------|---------|
| AI 違反規範被糾正後 | 把這條加進「禁止事項」 |
| 每次 `/archive` 後 | 本次發現的新慣例 |
| 新增第三方套件後 | 更新前端規範章節 |
| 升版 XOOPS / PHP 後 | 更新版本資訊與相容性注意事項 |

### convention.md 健康度自我檢查

```
□ 禁止事項有 AI 犯過的錯嗎？（沒有 = 規範太籠統）
□ 範例程式碼是真實可用的嗎？（不是 = 更新）
□ 路徑與模組名稱填對了嗎？（還有佔位符 = 還沒完成）
□ 上次更新日期是什麼時候？（超過 1 個月 = 考慮審閱）
```

---

## 快速參考卡

### 指令對照

| 我想做的事 | 執行指令 |
|-----------|---------|
| 開始新功能 | `/explore` |
| 確認 AI 理解範圍 | `/propose` → 審閱 spec |
| 執行程式碼修改 | `/apply` |
| 完成後整理歸檔 | `/archive` |
| 只是修 bug | `/explore` → `/apply`（跳過 propose）|

### 出問題時的 checklist

```
□ AI 產出的程式碼有沒有直接 echo HTML？
□ 有沒有用 class / namespace？
□ 資料庫操作有沒有用 $xoopsDB->query()？
□ 後台 POST 有沒有驗證 XOOPS_TOKEN？
□ 有沒有硬寫中文字串（應放語言包）？
□ 刪除操作有沒有 SweetAlert 確認？
```

### 常用 git 操作配合 /apply

```bash
# 每個 task 完成後
git add modules/your_module/admin/main.php
git add modules/your_module/templates/
git commit -m "feat(審核): 新增後台審核列表頁籤"

# 發現某個 task 改壞了
git log --oneline    # 找到問題 commit 的 hash
git revert abc1234   # 只還原那一個 task

# 查看目前所有變更
git diff HEAD
```

---

## 相關資源

| 資源 | 說明 |
|------|------|
| [[OpenSpec-XOOPS-convention]] | 主規格書範本（複製到專案用） |
| [[OpenSpec-delta-spec-範本]] | 每次功能的 spec 填寫範本 |
| [[OpenSpec 如何整合到 XOOPS 開發專案]] | 整合分析與背景 |
| [[OpenSpec安裝初始化]] | 安裝步驟詳解 |
| [[XOOPS開發規範]] | XOOPS 2.5 技術規範知識庫頁 |
| [[XOOPS-PromptKit-三種開發Prompt]] | 不用 OpenSpec 時的 Prompt 工具集 |
