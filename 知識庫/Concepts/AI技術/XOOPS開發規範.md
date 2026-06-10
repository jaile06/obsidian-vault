---
type: concept
aliases:
  - XOOPS 2.5 開發規範
tags:
  - 程式開發
  - XOOPS
  - 規範
related_concepts:
  - "[[提示詞工程]]"
  - "[[規範驅動開發SDD]]"
related_entities:
  - "[[XOOPS]]"
sources:
  - "[[XOOPS-PromptKit-三種開發Prompt]]"
  - "[[XOOPS-任務單範本]]"
  - "[[XOOPS闖關遊戲程式腳本]]"
  - "[[2026-04-23-OpenSpec整合XOOPS開發專案]]"
  - "[[2026-04-23-OpenSpec-XOOPS開發規範操作手冊]]"
created: 2026-04-23
updated: 2026-05-06
---

## 定義

一套針對 XOOPS 2.5 模組開發制定的技術規範，規定語言、資料庫操作、路徑、前端框架、UI 元件、安全防護等標準，確保模組相容性與可維護性。

## 核心重點

### 後端規範
- **語言：** 只用 Procedural PHP（禁用 class-based 架構）
- **資料庫：** `global $xoopsDB;` → `$xoopsDB->query($sql)` → `$xoopsDB->prefix('table_name')`
- **路徑：** `XOOPS_ROOT_PATH`（檔案系統）、`XOOPS_URL`（網址）
- **畫面輸出：** PHP 只做邏輯 + `$xoopsTpl->assign()`，**禁止在 PHP 直接輸出 HTML**
- **模板：** Smarty `.tpl` 檔

### 前端規範
- **樣式框架：** Bootstrap 5
- **圖示庫：** FontAwesome 6
- **提示 / 確認視窗：** SweetAlert（刪除、上傳、權限變更等操作必用）
- **表單驗證：** FormValidator
- **檔案上傳：** TadUpFiles

### 安全規範
- 所有輸入必須過濾
- SQL 字串必須使用 `$xoopsDB->escape()`
- `admin/main.php` 必須驗證 **XOOPS_TOKEN** 與管理員權限
- 每個 SQL 執行後必須檢查結果
- 刪除、上傳、權限變更等危險操作需額外安全確認

### UI 無障礙規範
- 字體 `1.1rem` 以上
- 高對比度色彩搭配
- 較大的點擊目標

## OpenSpec 整合操作流程

每次新功能開發標準流程（搭配 OpenSpec）：

```
一次性初始化
  npx openspec init → 生成 specs/ + AI 工作指引
  手動建 specs/xoops-convention.md（記錄模組慣例、禁止事項）

每次功能迭代
  /explore → AI 主動追問需求
  /propose → 產出 proposal.md + tasks.md
  /apply   → 逐 task 執行，完成一個 git commit 一次
  /archive → 歸檔，更新主 specs
```

主規格書 `specs/xoops-module-convention.md` 關鍵內容：
- 模組目錄結構慣例（xoops_version.php、class/、admin/、templates/、language/zht/）
- 資料庫操作規則（禁止直接 SQL，一律用 `$xoopsDB->query()`）
- 表格命名格式：`{db_prefix}_modulename_tablename`

## 不同視角 / 矛盾之處

- 規範針對 XOOPS 2.5；XOOPS 3.x 部分語法可能不同（如 [[XOOPS闖關遊戲程式腳本]] 基於 3.0）
- Procedural PHP 與現代 PHP 開發慣例（OOP）相悖，但為 XOOPS 2.5 相容性必要條件

## 延伸問題

- 如何將此規範轉為 AGENTS.md / CLAUDE.md 讓 AI 在 XOOPS 開發中自動遵守？
- 規範在 XOOPS 2.5 與 3.x 間有哪些差異需要維護？
