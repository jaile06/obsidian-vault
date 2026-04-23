---
type: source
original_path: "Notes/Clippings/xoops_prompts_specialized.md"
author: []
published: ""
tags:
  - 程式開發
  - XOOPS
  - 提示詞工程
extracted_concepts:
  - "[[XOOPS開發規範]]"
  - "[[提示詞工程]]"
extracted_entities:
  - "[[XOOPS]]"
created: 2026-04-23
updated: 2026-04-23
---

## 摘要（3 句內）

三種針對 XOOPS 2.5 模組開發情境設計的專用 Prompt：新增功能、重構、修 Bug。每種 Prompt 內嵌完整的開發規範（Procedural PHP、Smarty、Bootstrap 5 等）與輸出格式要求。可直接複製貼上使用，搭配任務單範本填寫具體需求。

## 關鍵要點

- **三種情境：** 新增功能 / 重構現有程式 / 修 Bug
- **共同開發規範：**
  - 只用 Procedural PHP（禁 class-based）
  - DB 操作：`global $xoopsDB;` + `$xoopsDB->query()` + `$xoopsDB->prefix()`
  - 路徑：`XOOPS_ROOT_PATH` / `XOOPS_URL`
  - 畫面：Smarty `.tpl` + Bootstrap 5 + FontAwesome 6
  - 提示 / 確認：SweetAlert；表單驗證：FormValidator；上傳：TadUpFiles
  - PHP 只做邏輯 + `$xoopsTpl->assign()`，禁止直接輸出 HTML
- **共同安全規範：** 所有輸入需過濾、SQL 用 `$xoopsDB->escape()`、admin 必查 XOOPS_TOKEN 與管理員權限、SQL 執行後必檢查結果
- **固定輸出格式：** Schema Map → Logic Flow → PHP → TPL → JavaScript → Security Check

## 此篇與知識庫哪些頁面有關

- [[XOOPS開發規範]] — 提取自本篇規範條目
- [[提示詞工程]] — 本篇為領域專用 Prompt 模板的實例
- [[XOOPS]] — 目標平台
- [[XOOPS-任務單範本]] — 搭配使用的填寫範本
- [[XOOPS闖關遊戲程式腳本]] — 同為 XOOPS 主題來源
