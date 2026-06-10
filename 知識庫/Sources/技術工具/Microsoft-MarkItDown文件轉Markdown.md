---
type: source
original_path: "Clippings/microsoftmarkitdown Python tool for converting files and office documents to Markdown.md"
author:
  - "Microsoft"
published: 2026-05-05
source: "https://github.com/microsoft/markitdown"
tags:
  - 工具
  - Python
  - Markdown
  - LLM工具鏈
extracted_concepts: []
extracted_entities:
  - "[[MarkItDown]]"
created: 2026-05-05
updated: 2026-05-05
---

## 摘要

Microsoft 開源 Python 工具，將各類型檔案（PDF、Word、PPT、Excel、圖片、音訊、HTML 等）轉換為 Markdown，專為 LLM 與文字分析 pipeline 設計，重點保留文件結構（標題、清單、表格、連結）。

## 關鍵要點

### 支援格式

PDF、PowerPoint、Word、Excel、圖片（EXIF + OCR）、音訊（EXIF + 語音轉錄）、HTML、CSV/JSON/XML、ZIP、YouTube URL、EPub 等。

### 為何選 Markdown

- LLM 原生「說」Markdown，理解度高、token 效率佳
- 接近純文字，最小標記量，保留結構

### 安裝與使用

```bash
pip install 'markitdown[all]'
markitdown path-to-file.pdf > output.md
```

### 安全注意事項

- 以當前程序權限執行 I/O，不可信任環境需做輸入驗證
- 優先呼叫最窄 API：`convert_local()` > `convert_stream()` > `convert()`

### 插件生態

- 支援第三方插件（`#markitdown-plugin`）
- `markitdown-ocr`：以 LLM Vision 提取嵌入圖片文字

## 此篇與知識庫哪些頁面有關

- [[MarkItDown]] — 工具本體
- [[Obsidian PDF擷取]] — 同屬「文件 → 知識庫」輸入通道
- [[RAG]] — LLM 文件處理 pipeline 的前置步驟
