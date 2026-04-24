# Skills 詳細流程

> 此檔案不自動注入。AI 在觸發對應 Skill 時才讀取。
> 頁面格式詳見 `Templates/concept.md`、`entity.md`、`source.md`。

---

## Skill 1: Ingest & Organize

**階段一：提案（不動檔案）**
1. 先詢問：「這份 md 是否從 `D:\note` 自行匯入的檔案？」
   - **是** →
     - 將 `.md` 與 `.docx` 移至 `Notes/Clippings/`
     - 若 `D:\note\media\` 有對應圖片：
       - 依 md 檔名產生簡短英文子目錄名（如 `modern-state-challenge`）
       - 圖片重新命名為 `{短英文名}_01.png`、`_02.png`…
       - 移至 vault 的 `media/{短英文名}/`
   - **否** → 直接讀取 `Notes/Clippings/` 或 `Notes/Conversations/` 新文件
2. 列出：新建 / 更新哪些 Source・Concept・Entity、建議標籤、交叉引用
3. 不確定的標注 ⚠️ → **等確認**

**階段二：執行**
4. 建 Source → 提取 Concept → 提取 Entity（已存在則合併，不重建）
5. 加雙向連結 `[[]]` → 更新 `index.md` → 寫 `log/YYYY-MM.md`
6. 完成後原檔移至 `Notes/Clippings/Archive/`
7. 同步：`git add . && git commit -m "sync: YYYY-MM-DD ingest" && git push`

**合併規則：** 先讀 index.md；同義詞用 `aliases` 合併；絕不建重複頁。

---

## Conversation 入庫

值得存的：跨主題分析、決策紀錄、新洞見、架構討論。
檔名：`YYYY-MM-DD_主題關鍵字.md` → `Notes/Conversations/`

---

## Skill 2: Query & Synthesize

1. 讀 `index.md` → 找相關 Concept / Entity / Source / LifeOS / Writing
2. 綜合回答；發現缺連結主動提議補
3. 有保存價值（新綜合、跨頁整合）→ 提議存檔（先提案）
4. 純事實查詢不存

---

## Skill 3: Content Output

1. 從沉澱層提取素材 → 產出初稿 → 確認後存 `Writing/`
2. **回流檢查：** 新概念 → Concepts、新來源 → Sources、新人物 → Entities
3. 遵守先提案再執行

---

## Skill 4: Lint & Maintenance

掃描全庫，找出：
- 孤立頁面（無引用）
- 重複概念（未合併）
- 矛盾資訊
- 知識缺口（延伸問題無對應頁）
- 過薄頁面（核心重點 < 3）
- 斷裂連結（`[[]]` 指向不存在的檔案）

產出 `知識庫/WeeklyReport_YYYY-MM-DD.md`，更新 `index.md` + `log.md`。
