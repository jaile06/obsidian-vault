---
title: 知識庫操作紀錄
type: log
---

# 知識庫操作紀錄

---

## 2026-04-17 Ingest | Karpathy LLM Wiki 原文

**操作類型：** Ingest

**處理的原始檔案（1 篇）：**
- LLM Wiki — Andrej Karpathy（原始定義文件）

**新增 Sources 頁（1 頁）：**
- Karpathy-LLM Wiki原文

**新增 Concepts 頁（2 頁）：**
- Memex（Bush 1945 聯想路徑知識庫概念）
- qmd搜尋引擎（本地 Markdown 混合搜尋工具）

**更新現有頁面（3 頁）：**
- Karpathy筆記方法（新增 source 連結）
- Andrej Karpathy（補充三種操作、Memex 根源、補齊實踐者名單）

**更新：** index.md（新增 1 Source、2 Concepts）

---

## 2026-04-17 補建 | 缺口 Concepts（第二輪）

**操作類型：** 補建

**補建缺口 Concepts（8 頁，均有現有頁面引用但檔案不存在）：**
- 知識管理系統（由 第二大腦、RAG 等多頁引用）
- 自動入庫（由 我是戴倫、戴倫-自我進化AI知識庫 引用）
- 知識庫健康檢查（由 我是戴倫、戴倫-自我進化AI知識庫 引用）
- 常數函數（由 一次函數、國中數學 引用）
- Context Window（由 RAG、AI工具總覽 引用）
- 多模態（由 RAG、AI工具總覽 引用）
- Google Apps Script（由 XOOPS闖關遊戲程式腳本 引用）
- 遊戲化教學（由 XOOPS闖關遊戲程式腳本 引用）

**更新：** index.md（新增 8 Concepts、補上 2 個 Sources：范凱-五層架構、戴倫-自我進化AI知識庫）

---

## 2026-04-17 Ingest | Clippings 新文章（第二批）

**操作類型：** Ingest

**處理的原始檔案（2 篇）：**
- Karpathy 的 LLM Wiki 火了，我改造了一下，比原版好用十倍（范凱说AI）
- 用大神卡帕西的方法，我打造了一個會自我進化的AI知識庫（我是戴倫）

**新增 Sources 頁（2 頁）：**
- 范凱-五層架構改造Karpathy方法
- 戴倫-自我進化AI知識庫

**新增 Concepts 頁（2 頁）：**
- 五層知識庫架構
- AI確認機制

**新增 Entities 頁（2 頁）：**
- 范凱说AI
- 我是戴倫

**跨文章新連結：**
- 五層架構 ↔ Karpathy筆記方法（改造關係）
- AI確認機制 ↔ 提示詞工程（操作層連結）
- 范凱说AI / 我是戴倫 ↔ Andrej Karpathy（同為實踐者）

**更新：** index.md（新增知識管理分類兩個新 Concept、兩個新 Entity）

---

## 2026-04-17 Ingest | 補充 Clippings + 缺口 Concepts

**操作類型：** Ingest + 補建

**新增 Sources 頁（2 頁）：**
- EP08-Obsidian打造AI筆記流（Clippings）
- Karpathy筆記術-Claude Code建立知識庫（Clippings）

**補建使用者已建 Source 頁所缺的 Concepts（2 頁）：**
- 對比度測試（由 5色調色盤 + 網站配色流程 引用）
- 提示詞工程（由 AI思維重構 + AI工具總覽 引用）

**新增 Concepts 頁（2 頁）：**
- 第二大腦
- Karpathy筆記方法

**新增 Entities 頁（1 頁）：**
- Andrej Karpathy

**更新：** index.md（新增所有新頁面，補上 知識管理 主題分類）

---

## 2026-04-17 Ingest | OneDrive匯入 批次處理

**操作類型：** Ingest

**來源資料夾：** 知識庫/OneDrive匯入/

**處理的原始檔案（6 篇）：**
- 國中數學講義：線型函數與函數圖形.md
- ai工具/ai 工具介紹.md
- ai工具/程式腳本.md（XOOPS 闖關遊戲需求）
- 網站配色/配色流程.md
- 網站配色/免費背景圖網站.md + 依圖片抓取配色網站.md + 5色調色盤.md（合併）
- Markdown/Markdown語法.md + 如何插入PHP代碼.md（合併）

**略過：**
- ai 思維重構.md（僅含 YouTube 連結，無可提取內容）

**新增 Sources 頁（6 頁）：**
- 國中數學-線型函數與函數圖形
- AI工具總覽
- XOOPS闖關遊戲程式腳本
- 網站配色流程
- 免費設計資源彙整
- Markdown語法指南

**新增 Concepts 頁（6 頁）：**
- 線型函數、一次函數（數學）
- RAG（AI技術）
- 網站配色系統、色彩角色（網站設計）
- Markdown語法（技術工具）

**新增 Entities 頁（3 頁）：**
- ChatGPT、NotebookLM（AI工具）
- Adobe Color（設計工具）

**更新：** index.md（新增所有頁面條目）

---

## 2026-04-16 初始化 | 建立第二大腦

**操作類型：** 初始化

**建立的結構：**
- Clippings/（輸入）
- 知識庫/（消化）
- 創作庫/（輸出）
- 每日筆記/（時間管理）
- Templates/（模板）
- CLAUDE.md（工作規則）
