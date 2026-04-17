---
type: concept
aliases: [檢索增強生成, Retrieval-Augmented Generation]
tags: [AI技術, LLM, 知識庫]
related_concepts: ["[[Context Window]]", "[[多模態]]"]
related_entities: ["[[NotebookLM]]"]
sources: ["[[AI工具總覽]]"]
created: 2026-04-17
updated: 2026-04-17
---

## 定義

讓 AI 在回答問題前，先從外部知識庫檢索相關資料，再結合這些資料生成回應的技術架構。解決 LLM 訓練資料截止日期與特定領域知識不足的問題。

## 核心重點

- **Retrieval（檢索）**：依使用者問題，從外部資料庫找出相關文件片段
- **Augmented（增強）**：把檢索結果連同問題一起送給 LLM
- **Generation（生成）**：LLM 依據檢索內容產生更精準的回應
- 需要向量資料庫（Vector DB）與 Embedding 技術支援
- [[NotebookLM]] 是 RAG 的實際應用案例

## 不同視角 / 矛盾之處

- Karpathy 的 Index-based Wiki 方法不使用 RAG，而是靠 AI 讀目錄索引找資料；對小規模個人知識庫（~100篇）可行，避免向量資料庫的建置成本

## 延伸問題

- RAG 與 Fine-tuning 的差異與適用場景？
- 向量資料庫的 Embedding 是如何運作的？
