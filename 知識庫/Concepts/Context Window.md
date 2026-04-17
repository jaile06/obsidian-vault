---
type: concept
aliases: [上下文視窗, 脈絡視窗, 輸入長度限制]
tags: [AI技術, LLM, 基礎概念]
related_concepts: ["[[RAG]]", "[[多模態]]", "[[提示詞工程]]"]
sources: ["[[AI工具總覽]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

LLM 在單次對話中能「看到」的最大 token 數量。超出視窗的內容模型無法直接存取。

## 核心重點

- **單位**：Token（約 0.75 個英文單字，中文每字約 1–2 token）
- **限制來源**：Transformer 架構的注意力機制計算成本
- **影響**：長文件、多輪對話、大型程式碼庫超出限制時需截斷

## 各模型規模（參考）

| 模型 | Context Window |
|------|----------------|
| GPT-4o | 128K tokens |
| Claude Sonnet 4.6 | 200K tokens |
| Gemini 1.5 Pro | 1M tokens |

## 與 RAG 的關係

[[RAG]] 正是為了突破 Context Window 限制而生：將大型知識庫存在外部，每次只檢索相關片段放入視窗，而非把全部內容塞入。

## 延伸問題

- Context Window 越大越好嗎？（成本、注意力稀釋問題）
- Karpathy 方法用 Index.md 替代 RAG，適合中小型知識庫（< 200 頁）
