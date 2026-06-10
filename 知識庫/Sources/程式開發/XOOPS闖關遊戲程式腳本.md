---
type: source
original_path: 知識庫/ai工具/程式腳本.md
author: []
published: ""
tags:
  - 程式開發
  - XOOPS
  - 遊戲化教學
extracted_concepts:
  - "[[遊戲化教學]]"
  - "[[Google Apps Script]]"
extracted_entities:
  - "[[XOOPS]]"
  - "DiceBear"
---

## 摘要（3 句內）

設計一個以 XOOPS 3.0 為基礎、Pixel Art 風格的闖關答題遊戲模組需求文件。題目來源為 Google Sheets，透過 Google Apps Script 處理取題與計分邏輯。成績記錄包含闖關次數、最高分、首次通關分數等多維度數據。

## 關鍵要點

- 前端：XOOPS 3.0 + Pixel Art 風格，使用 DiceBear API 生成 100 張關主圖片
- 題目流程：Google Sheets → Google Apps Script → 隨機取 N 題顯示（不含答案）
- 計分：提交後由 Apps Script 計算，回寫 Google Sheets
- 環境變數：GOOGLE_APP_SCRIPT_URL、PASS_THRESHOLD、QUESTION_COUNT

## 此篇與知識庫哪些頁面有關

- [[XOOPS]]
- [[Google Apps Script]]
- [[遊戲化教學]]
