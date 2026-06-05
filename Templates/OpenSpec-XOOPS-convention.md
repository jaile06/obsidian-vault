---
title: OpenSpec XOOPS 主規格書範本
description: 複製到 XOOPS 專案的 specs/convention.md 使用，這是 AI 每次開發都會讀的「規則」
tags:
  - template
  - openspec
  - xoops
related_concepts:
  - "[[XOOPS開發規範]]"
  - "[[OpenSpec]]"
---

> **使用方式**：將以下內容（從分隔線以下）複製到你的 XOOPS 模組專案 `specs/convention.md`，依實際情況調整 `[你的模組名稱]` 等佔位符。

---

# specs/convention.md — XOOPS 2.5 模組開發規範

> 本文件是 AI 開發協作的強制規範。每次執行任何程式碼修改前，AI 必須先讀本文件。

## 1. 專案資訊

| 欄位 | 值 |
|------|----|
| 模組名稱 | `[your_module_name]`（小寫，對應 dirname） |
| XOOPS 版本 | 2.5.x |
| PHP 版本 | 5.6 / 7.x（依伺服器環境填寫） |
| 模組根目錄 | `XOOPS_ROOT_PATH/modules/[your_module_name]/` |

---

## 2. 目錄結構慣例

```
modules/[your_module_name]/
├── xoops_version.php     ← 模組宣告（必填欄位見下方）
├── index.php             ← 前台入口
├── admin/
│   └── main.php          ← 後台入口（必須驗證 TOKEN 與權限）
├── class/
│   └── [object].php      ← 資料物件定義（使用 XoopsObject/XoopsObjectHandler）
├── templates/
│   └── [module]_[page].html  ← Smarty 模板（.html 副檔名）
├── language/
│   └── zht/
│       ├── main.php      ← 前台語言字串
│       └── admin.php     ← 後台語言字串
└── sql/
    └── mysql.sql         ← 安裝時建立的資料表
```

### `xoops_version.php` 必填欄位

```php
$modversion['name']        = '模組顯示名稱';
$modversion['version']     = 1.0;
$modversion['dirname']     = '[your_module_name]';
$modversion['description'] = '模組說明';
$modversion['author']      = '作者';
```

---

## 3. 後端規範（強制）

### 3.1 PHP 寫法

- **只用 Procedural PHP**，禁用 class-based 架構（XOOPS 2.5 不支援 namespace）
- 每個 PHP 檔案開頭必須有安全檢查：
  ```php
  defined('XOOPS_ROOT_PATH') || die('Restricted access');
  ```

### 3.2 資料庫操作

```php
// 正確寫法
global $xoopsDB;
$table = $xoopsDB->prefix('modulename_tablename');
$sql   = "SELECT * FROM $table WHERE id = " . (int)$id;
$result = $xoopsDB->query($sql);

// 字串欄位必須 escape
$name = $xoopsDB->escape($_POST['name']);

// 每次 query 後必須檢查結果
if (!$result) {
    // 處理錯誤
}
```

**禁止行為：**
- 禁止直接使用 `mysqli_*` 或 PDO
- 禁止字串拼接未 escape 的輸入（SQL Injection 風險）
- 禁止省略 `$xoopsDB->query()` 的結果檢查

### 3.3 路徑規則

| 情境 | 使用常數 |
|------|---------|
| 引入本機檔案 | `XOOPS_ROOT_PATH` |
| 產生前台連結 | `XOOPS_URL` |
| 模組根目錄   | `XOOPS_ROOT_PATH . '/modules/[your_module_name]/'` |

### 3.4 畫面輸出規則

- PHP 只做邏輯運算與資料處理
- **禁止在 PHP 直接 echo HTML**
- 所有顯示資料透過 `$xoopsTpl->assign('key', $value)` 傳給 Smarty
- 模板檔案：`templates/[module]_[page].html`

---

## 4. 前端規範（強制）

| 用途 | 套件 | 備註 |
|------|------|------|
| CSS 框架 | Bootstrap 5 | 已內建於佈景主題 |
| 圖示 | FontAwesome 6 | `<i class="fa fa-xxx">` |
| 提示 / 確認視窗 | SweetAlert | 刪除、危險操作必用，禁用原生 `confirm()` |
| 表單驗證 | FormValidator | 前台表單必用 |
| 檔案上傳 | TadUpFiles | 所有檔案上傳一律使用，禁止自行實作上傳邏輯 |

### 危險操作強制規則

以下操作**必須**使用 SweetAlert 二次確認：
- 刪除任何資料
- 批次操作
- 不可逆的狀態變更
- 檔案上傳（TadUpFiles 整合）
- 權限變更

---

## 5. 安全規範（強制）

### 5.1 後台頁面

`admin/main.php` 必須包含：

```php
// 驗證管理員身份
if (!isset($xoopsUser) || !$xoopsUser->isAdmin()) {
    redirect_header(XOOPS_URL, 3, '無權限存取');
    exit();
}

// 驗證 XOOPS TOKEN（POST 操作）
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!$GLOBALS['xoopsSecurity']->check()) {
        redirect_header(XOOPS_URL . '/modules/[your_module_name]/admin/main.php', 3, '安全驗證失敗');
        exit();
    }
}
```

### 5.2 輸入過濾規則

| 資料類型 | 處理方式 |
|---------|---------|
| 整數 ID | `(int)$_GET['id']` |
| 字串（SQL） | `$xoopsDB->escape($_POST['field'])` |
| HTML 輸出 | `htmlspecialchars($value, ENT_QUOTES)` |
| 檔案上傳 | 一律透過 TadUpFiles，不直接處理 `$_FILES` |

---

## 6. 語言包規範

- **禁止在 PHP 或 TPL 寫死中文字串**
- 語言常數命名格式：`_MD_[MODULENAME]_[KEYNAME]`（全大寫）
- 範例：
  ```php
  // language/zht/main.php
  define('_MD_MYMODULE_SUBMIT', '送出');
  define('_MD_MYMODULE_DELETE_CONFIRM', '確認刪除此筆資料？');
  ```
- 模板中使用：`{_MD_MYMODULE_SUBMIT}`

---

## 7. UI 無障礙規範

- 字體大小：`1.1rem` 以上
- 色彩對比度：符合 WCAG AA（前景/背景對比 ≥ 4.5:1）
- 可點擊目標：最小 44×44px

---

## 8. AI 開發禁止事項（摘要）

> 這裡列出過去 AI 曾犯過的錯，優先級最高。

- 禁止直接 echo HTML（用 Smarty assign）
- 禁止用 class / namespace / PSR 命名風格
- 禁止用 PDO / mysqli_ 直接操作資料庫
- 禁止用原生 `confirm()` / `alert()`（用 SweetAlert）
- 禁止省略 XOOPS_TOKEN 驗證（後台 POST）
- 禁止硬寫中文字串（放語言包）
- 禁止自行實作檔案上傳（用 TadUpFiles）

---

*最後更新：`[填寫日期]`*
*更新時機：每次 /archive 後，將本次發現的新慣例加入。*
