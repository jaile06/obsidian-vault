# XOOPS 2.5 任務單範本

這份文件可搭配以下 Prompt 使用：

- 新功能版 Prompt
- 重構版 Prompt
- 修 Bug 版 Prompt

建議做法：

1. 先貼對應的 Prompt
2. 再貼這份任務單內容
3. 補上實際模組名稱、檔案、需求與現況

---

## 一、通用完整版任務單範本

```text
【任務類型】
（請選一項）
- 建立新功能
- 重構現有程式
- 修正 Bug
- UI / UX 調整
- 權限與安全性補強
- 資料表調整

【模組名稱】
（請填寫）
例如：news、course、contact、download、form

【處理檔案】
（請填寫）
例如：
- admin/main.php
- index.php
- list.php
- edit.php
- templates/module_list.tpl

【目前現況】
（請描述目前的程式狀況或貼上舊程式碼）
例如：
- 目前 PHP 直接輸出 HTML
- 列表頁仍是舊版 table 排版
- 刪除功能使用原生 confirm
- SQL 沒有做 escape
- 表單沒有驗證
- 上傳功能未使用 TadUpFiles

【需求說明】
（請條列這次要完成的內容）
1.
2.
3.
4.

【資料表資訊】
（若涉及資料表異動，請填寫；若沒有可寫「無」）
例如：
- 資料表：xxx_records
- 新增欄位：sort、enable
- 修改欄位：title 長度改為 255
- 建立索引：cate_id
- 是否需保留舊資料：是 / 否

【權限與流程要求】
（若有請填寫）
例如：
- 僅管理員可新增／刪除
- 前台會員只能查看不可編輯
- 刪除前必須 SweetAlert 二次確認
- 表單送出前必須做 FormValidator 驗證

【UI 要求】
（若有請填寫）
例如：
- 改成 Bootstrap 5 card 版型
- 按鈕加入 FontAwesome 6 圖示
- 字體放大，適合視力較弱者
- 手機版可正常操作
- 表單欄位間距加大

【已知問題或錯誤訊息】
（修 Bug 時建議填）
例如：
- Undefined index: title
- Call to undefined function
- SQL syntax error
- 上傳圖片後無法顯示
- 刪除後資料仍存在

【其他限制】
（若有請填寫）
例如：
- 必須相容 XOOPS 2.5
- 不可改動既有主鍵
- 必須保留原本函式名稱
- 不可改為 class-based 架構
- 必須沿用目前資料表

【輸出要求】
請依序提供：
1. Schema Map
2. Logic Flow
3. PHP Code
4. TPL Code
5. JavaScript Code
6. Security Check
```

---

## 二、簡短版任務單範本

```text
【任務類型】
重構 / 新增功能 / 修 Bug / UI 調整

【模組名稱】
（填寫）

【檔案】
（填寫）

【目前問題】
（填寫）

【需求】
1.
2.
3.

【是否涉及資料表】
是 / 否
若是，請補充欄位異動：

【輸出格式】
請依序提供：
1. Schema Map
2. Logic Flow
3. PHP Code
4. TPL Code
5. JavaScript Code
6. Security Check
```

---

## 三、新功能專用任務單範本

```text
【任務類型】
建立新功能

【模組名稱】
（填寫）

【功能名稱】
（填寫）
例如：附件上傳、列表篩選、前台投稿、後台審核

【功能目標】
（請描述這個功能要解決什麼問題）

【處理檔案】
（填寫）

【資料表需求】
1. 是否需新增資料表：是 / 否
2. 是否需新增欄位：是 / 否
3. 欄位需求：
4. 是否需保留舊資料相容：是 / 否

【功能流程】
例如：
1. 使用者進入頁面
2. 填寫表單
3. 驗證資料
4. 寫入資料庫
5. 顯示成功訊息

【UI 要求】
（填寫）

【權限要求】
（填寫）

【其他限制】
（填寫）

【輸出要求】
請依序提供：
1. Schema Map
2. Logic Flow
3. PHP Code
4. TPL Code
5. JavaScript Code
6. Security Check
```

---

## 四、重構專用任務單範本

```text
【任務類型】
重構現有程式

【模組名稱】
（填寫）

【處理檔案】
（填寫）

【舊程式現況】
（請描述目前程式問題）
例如：
- PHP 與 HTML 混寫
- 非 Bootstrap 5 介面
- 缺少中文註解
- 刪除仍用原生 confirm
- SQL 與流程過於混亂

【重構目標】
1.
2.
3.

【必須保留的舊邏輯】
（請填寫）
例如：
- 原本查詢條件不可改
- 原本分頁邏輯必須保留
- 原本欄位命名不可改動

【可優化項目】
（請填寫）
例如：
- 畫面改為 Bootstrap 5
- 拆出 Smarty tpl
- 改善按鈕與操作流程
- 補上安全檢查

【是否涉及資料表異動】
是 / 否
若是，請補充：

【輸出要求】
請依序提供：
1. Schema Map（若無異動請註明）
2. Logic Flow
3. PHP Code
4. TPL Code
5. JavaScript Code
6. Security Check
```

---

## 五、修 Bug 專用任務單範本

```text
【任務類型】
修正 Bug

【模組名稱】
（填寫）

【處理檔案】
（填寫）

【錯誤現象】
（請清楚描述）
例如：
- 新增資料後頁面空白
- 編輯後資料沒有更新
- 圖片上傳成功但前台不顯示
- 刪除按鈕點了沒反應

【錯誤訊息】
（若有請貼上）
例如：
- Undefined variable
- SQL syntax error
- Call to undefined function
- Warning / Notice 內容

【重現步驟】
1.
2.
3.

【預期結果】
（原本應該發生什麼）

【目前實際結果】
（實際發生了什麼）

【是否涉及資料表】
是 / 否
若是，請補充表結構或 SQL

【其他限制】
例如：
- 只能最小幅度修正
- 不可影響既有前台功能
- 必須保留舊版資料相容

【輸出要求】
請依序提供：
1. Bug Analysis
2. Schema Map（若無異動請註明）
3. Logic Flow
4. PHP Code
5. TPL Code
6. JavaScript Code
7. Security Check
```

---

## 六、實際填寫範例

```text
【任務類型】
重構現有程式

【模組名稱】
news

【處理檔案】
admin/main.php
templates/news_list.tpl

【舊程式現況】
1. PHP 直接輸出 HTML
2. 列表頁不是 Bootstrap 5
3. 刪除仍用原生 confirm
4. SQL 沒有 escape

【重構目標】
1. 改成 PHP assign + Smarty tpl
2. 列表頁改為 Bootstrap 5 card 版型
3. 刪除改用 SweetAlert
4. 補上安全檢查與中文註解

【必須保留的舊邏輯】
1. 原本查詢排序方式不可改
2. 原本刪除流程必須保留
3. 原本資料表不可異動

【是否涉及資料表異動】
否

【輸出要求】
請依序提供：
1. Schema Map
2. Logic Flow
3. PHP Code
4. TPL Code
5. JavaScript Code
6. Security Check
```
