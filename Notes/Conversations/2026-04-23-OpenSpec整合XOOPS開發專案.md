---
title: "OpenSpec 如何整合到 XOOPS 開發專案"
date: 2026-04-23
tags:
  - openspec
  - xoops
  - spec-driven-development
  - ai-coding
related_concepts:
  - "[[OpenSpec]]"
  - "[[規範驅動開發SDD]]"
---

## 問題

> OpenSpec 如何能整合到我的 XOOPS 開發專案？如何寫規格書？

---

## 為什麼 XOOPS 適合 OpenSpec

XOOPS 老舊 PHP CMS 的典型痛點與 OpenSpec 解決的問題高度吻合：

- **模組架構複雜**：功能跨 `class/`、`admin/`、`templates/`、`language/` 多資料夾，AI 容易亂改
- **老舊慣例多**：`XoopsForm`、`XoopsObject`、`XoopsHandler` 有固定寫法，AI 不熟悉容易產出不符規範的代碼
- **需求持續追加**：客戶上線後不斷改，沒有文件就失控

---

## 操作流程

```
第一次使用（一次性）
│
├─ npx openspec init
│   └─ 生成 specs/ 目錄 + AI 工作指引
│
└─ 手動寫 specs/xoops-convention.md
    └─ 記錄 XOOPS 模組慣例、禁止事項

每次新功能
│
├─ /explore  → 讓 AI 問你清楚「這次要改什麼」
├─ /propose  → 產出 proposal.md + tasks.md
├─ /apply    → 按 task 逐一執行（每完成一個就 git commit）
└─ /archive  → 歸檔，更新主 specs
```

---

## 規格書結構

### `specs/xoops-convention.md`（主規格書，長期維護）

這是專案「憲法」，**一次寫好，每次 archive 後更新**：

```markdown
# specs/xoops-module-convention.md

## 模組目錄結構慣例
- xoops_version.php  → 模組宣告（必填欄位：name, version, dirname）
- class/             → XoopsObject + XoopsObjectHandler
- admin/             → 後台頁面（index.php 為入口）
- templates/         → Smarty .html 模板
- language/zht/      → 繁中語言包

## 資料庫操作規則
- 禁止直接 SQL，一律用 $xoopsDB->query()
- 表格名稱格式：{db_prefix}_modulename_tablename

## 表單慣例
- 前台用 XoopsForm 系列
- admin 用 xoops_cp_header() + xoops_cp_footer()
```

### `changes/` — 每次功能的 delta spec

```markdown
# changes/feature-member-approval/proposal.md

## 目標
會員申請後需要管理員審核，審核通過才能登入。

## 影響範圍（delta spec）
- ADD: class/memberHandler.php → 新增 approveMember() 方法
- MODIFY: admin/index.php → 新增審核列表頁籤
- MODIFY: templates/admin_index.html → 新增審核狀態欄位
- ADD: language/zht/admin.php → 審核相關文字

## 不影響範圍
- 前台顯示邏輯不動
- 資料庫結構不變（沿用 users 表的 level 欄位）
```

---

## `specs/xoops-convention.md` 必寫內容

| 類型 | 要寫的內容 |
|------|-----------|
| **禁止行為** | 禁直接 SQL、禁硬寫文字、禁跳過語言包 |
| **必填結構** | xoops_version.php 必填欄位 |
| **命名規則** | class 名稱、表格前綴、模板變量格式 |
| **測試方式** | 後台頁面路徑、測試帳號條件 |

---

## 完整 delta spec 範本（留言審核功能）

```markdown
# changes/feature-comment-moderation/spec.md

## 背景
客戶反映匿名留言有垃圾訊息問題，需要後台審核機制。

## 功能範圍
1. 留言預設狀態改為「待審核」(status=0)
2. 後台新增審核列表，可批次核准/刪除
3. 審核通過後前台才顯示

## XOOPS 實作約束（AI 必須遵守）
- Handler 繼承 XoopsObjectHandler，不可直接操作 $xoopsDB
- 後台頁面套用 xoops_cp_header() / xoops_cp_footer()
- 語言字串放 language/zht/main.php，key 格式：_MD_MODULENAME_KEYNAME
- 模板變量用 $xoopsTpl->assign()，禁止直接 echo

## 驗收條件
- [ ] 新留言不顯示於前台
- [ ] 管理員後台可看到待審核列表
- [ ] 核准後前台立即顯示
- [ ] 刪除後資料從資料庫移除
```

---

## 核心結論

OpenSpec 對 XOOPS 的最大價值：**把腦子裡知道但沒寫出來的 XOOPS 慣例，變成 AI 每次都會看的規範**。

最划算的第一步：安裝 OpenSpec 後，先寫 `specs/xoops-convention.md`。
