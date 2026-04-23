---
title: "OpenSpec Delta Spec 範本（XOOPS 新功能）"
description: "每次開發新功能前，複製此範本到 changes/feature-[名稱]/spec.md，填入具體需求"
tags:
  - template
  - openspec
  - xoops
  - spec-driven-development
related_concepts:
  - "[[OpenSpec]]"
  - "[[XOOPS開發規範]]"
---

> **使用方式**：
> 1. 在 XOOPS 模組專案建立 `changes/feature-[功能名稱]/` 目錄
> 2. 將以下內容複製為 `spec.md`，填寫所有 `[...]` 欄位
> 3. 給 AI 看此 spec 後執行 `/apply`

---

# Feature Spec：`[功能名稱]`

> **建立日期**：`[YYYY-MM-DD]`
> **狀態**：`draft` / `approved` / `done`

---

## 背景與目標

> 說明**為什麼**需要這個功能、**客戶或使用者的痛點**是什麼。

`[例：客戶反映匿名留言有垃圾訊息，需要後台審核機制才能控制內容品質]`

---

## 功能範圍（這次要做的事）

> 條列**使用者看得到的功能變化**，不要寫技術細節。

1. `[例：留言預設狀態改為「待審核」，前台不顯示]`
2. `[例：後台新增審核列表，顯示待審核留言]`
3. `[例：管理員可批次核准或刪除]`
4. `[例：核准後前台立即顯示]`

---

## 不包含在此次範圍（明確排除）

> 這個區塊非常重要。明確告訴 AI「不要動」的部分。

- `[例：前台留言表單 UI 不變]`
- `[例：Email 通知功能留到下次]`
- `[例：資料庫結構不變，沿用現有 status 欄位]`

---

## 影響範圍（檔案層級的 delta）

> 列出每個會被新增或修改的檔案，標明動作類型。

| 動作 | 檔案路徑 | 變更說明 |
|------|---------|---------|
| `ADD` | `class/[Object]Handler.php` | `[例：新增 approve() / reject() 方法]` |
| `MODIFY` | `admin/main.php` | `[例：新增審核列表頁籤與批次操作]` |
| `MODIFY` | `templates/[module]_admin_main.html` | `[例：新增審核狀態欄位與操作按鈕]` |
| `MODIFY` | `language/zht/admin.php` | `[例：新增審核相關語言常數]` |
| `ADD` | `sql/update_v[X.X].sql` | `[例：若需要資料庫異動，說明欄位變更]` |

---

## XOOPS 實作約束（AI 必須遵守）

> 從 `specs/convention.md` 提取本次最相關的規範，方便 AI 快速確認。

- Handler 繼承 `XoopsObjectHandler`，資料庫操作用 `$xoopsDB->query()`
- 後台頁面套用 `xoops_cp_header()` / `xoops_cp_footer()`
- 後台 POST 操作必須驗證 `XOOPS_TOKEN`
- 語言字串放 `language/zht/admin.php`，key 格式：`_MD_[MODULENAME]_[KEYNAME]`
- 模板變量用 `$xoopsTpl->assign()`，禁止直接 echo
- 刪除、批次操作必須用 SweetAlert 確認視窗
- `[補充本次特有的約束]`

---

## 資料庫資訊（如有異動）

```sql
-- 現有相關資料表
-- [例：{prefix}_mymodule_comments (id, content, status, created)]

-- 本次異動（如有）
-- [例：ALTER TABLE {prefix}_mymodule_comments ADD COLUMN reviewed_by INT DEFAULT 0;]
```

若無資料庫異動，填寫：**本次不修改資料庫結構**。

---

## 驗收條件

> 可以直接複製貼上給測試人員確認的 checklist。

- [ ] `[例：新增留言後，前台不顯示該留言]`
- [ ] `[例：管理員後台可看到「待審核」列表，數量正確]`
- [ ] `[例：點擊核准後，前台立即顯示該留言]`
- [ ] `[例：點擊刪除時，出現 SweetAlert 確認視窗]`
- [ ] `[例：刪除後資料從資料庫移除，列表更新]`
- [ ] `[例：批次核准 / 批次刪除功能正常]`
- [ ] `[例：頁面文字全部使用語言包，無硬寫中文]`

---

## 測試環境資訊

| 欄位 | 值 |
|------|----|
| 後台路徑 | `[例：http://localhost/xoops/modules/mymodule/admin/main.php]` |
| 測試管理員帳號 | `[admin / 密碼]` |
| 測試資料 | `[例：資料庫已有 5 筆 status=0 的待審核留言]` |

---

*此 spec 執行完成後，執行 `/archive` 歸檔，並將新發現的慣例更新至 `specs/convention.md`。*
