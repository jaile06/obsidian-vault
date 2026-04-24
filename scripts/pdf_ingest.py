"""
pdf_ingest.py — Clippings 兩階段自動入庫，符合五層架構 vault 規則

【兩階段工作流】

Stage 1（產生草稿）：
    把 PDF 丟進 Notes/Clippings/
    python scripts/pdf_ingest.py
    → Notes/Clippings/your-file.md（草稿，可在 Obsidian 確認）

Stage 2（正式入庫）：
    確認草稿後執行：
    python scripts/pdf_ingest.py --ingest
    → 建立 知識庫/Sources/<topic>/<slug>.md
    → 更新 知識庫/index.md
    → 寫 知識庫/log/YYYY-MM.md
    → 草稿移至 Notes/Clippings/Archive/
    → PDF 移至 Notes/pdf/

單檔模式：
    python scripts/pdf_ingest.py --pdf <路徑> [--title "標題"]   # Stage 1
    python scripts/pdf_ingest.py --md  <路徑> [--title "標題"]   # Stage 2

依賴：
    pip install marker-pdf
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path



# ── Vault 路徑常數
VAULT             = Path(__file__).parent.parent
CLIPPINGS         = VAULT / "Notes" / "Clippings"
CLIPPINGS_ARCHIVE = CLIPPINGS / "Archive"
PDF_ARCHIVE       = VAULT / "Notes" / "pdf"
SOURCES           = VAULT / "知識庫" / "Sources"
LOG_DIR           = VAULT / "知識庫" / "log"
INDEX_MD          = VAULT / "知識庫" / "index.md"

VALID_TOPICS = ["AI技術", "技術工具", "數學", "知識管理", "程式開發", "網站設計"]

# ── Stage 2 本地分類：keyword matching，不呼叫 API
TOPIC_KEYWORDS = {
    "AI技術": ["ai", "llm", "gpt", "transformer", "模型", "人工智慧", "機器學習",
              "深度學習", "神經網路", "nlp", "自然語言", "prompt", "embedding",
              "rag", "agent", "machine learning", "neural", "fine-tun"],
    "技術工具": ["docker", "git", "linux", "devops", "ci/cd", "vscode",
               "obsidian", "terminal", "shell", "cli", "api", "工具"],
    "數學": ["數學", "統計", "機率", "線性代數", "微積分", "math", "algebra",
            "calculus", "probability", "theorem", "proof", "矩陣"],
    "知識管理": ["知識管理", "筆記", "zettelkasten", "pkm", "second brain",
               "知識庫", "knowledge", "學習"],
    "程式開發": ["python", "javascript", "typescript", "rust", "程式", "coding",
               "algorithm", "演算法", "資料結構", "design pattern", "軟體", "架構"],
    "網站設計": ["html", "css", "react", "vue", "next.js", "web", "前端",
               "後端", "ui", "ux", "網站", "網頁", "frontend", "backend"],
}


# ════════════════════════════════════════
# 工具函式
# ════════════════════════════════════════

def pdf_to_raw_markdown(pdf_path: Path) -> str:
    marker_bin = shutil.which("marker_single") or (Path(sys.executable).parent / "marker_single")
    marker_bin = Path(marker_bin)
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        cmd = [
            str(marker_bin),
            str(pdf_path),
            "--output_dir", str(tmp_path),
            "--output_format", "markdown",
            "--disable_multiprocessing",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print("  [marker stderr]", result.stderr[-600:])
            raise RuntimeError("marker 轉換失敗，請確認已安裝 marker-pdf 且 PDF 可讀取。")
        md_files = list(tmp_path.rglob("*.md"))
        if not md_files:
            raise RuntimeError("marker 未產生 Markdown 檔案。")
        return md_files[0].read_text(encoding="utf-8")


def make_slug(name: str) -> str:
    slug = re.sub(r"[^\w一-鿿\-]", "-", name)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug[:80]


def update_index(page_name: str) -> None:
    text = INDEX_MD.read_text(encoding="utf-8")

    def bump(m: re.Match) -> str:
        return f"## 3. Sources（{int(m.group(1)) + 1}）"
    text = re.sub(r"## 3\. Sources（(\d+)）", bump, text)
    text = text.replace(
        "**完整清單:**\n- [[index-sources]]",
        f"- [[{page_name}]]\n**完整清單:**\n- [[index-sources]]",
        1,
    )
    INDEX_MD.write_text(text, encoding="utf-8")


def append_log(entry: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m')}.md"
    if not log_file.exists():
        log_file.write_text(
            f"# 操作記錄 {datetime.now().strftime('%Y-%m')}\n\n",
            encoding="utf-8",
        )
    with log_file.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")


def preclean_raw_text(text: str) -> str:
    """在送 Claude 前先本地去噪，省 input token"""
    # 移除獨立頁碼行（如 "1", "Page 2", "- 3 -"）
    text = re.sub(r"^\s*[-—]?\s*\d{1,4}\s*[-—]?\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*Page\s+\d+\s*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    # 壓縮連續空行為最多 2 行
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # 移除行尾多餘空白
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    return text.strip()


def classify_topic(text: str) -> str:
    """本地 keyword matching 分類，取代 Claude API 呼叫"""
    text_lower = text.lower()
    scores = {}
    for topic, keywords in TOPIC_KEYWORDS.items():
        scores[topic] = sum(text_lower.count(kw.lower()) for kw in keywords)
    best = max(scores, key=scores.get)
    # 沒有任何 keyword 命中時，預設歸類為知識管理
    return best if scores[best] > 0 else "知識管理"


# ════════════════════════════════════════
# Stage 1：PDF → 草稿 .md 到 Clippings（純本地，不呼叫 API）
# ════════════════════════════════════════

def build_draft_md(cleaned_text: str, slug: str, today: str) -> str:
    """用清理後的文字組裝草稿 Markdown：frontmatter + 空白摘要模板 + 正文"""
    # 自動分類，決定 tags 初始值
    topic = classify_topic(cleaned_text)
    frontmatter = (
        f"---\n"
        f"type: source\n"
        f"original_path: \"Notes/Clippings/{slug}.md\"\n"
        f"author: [\"\"]\n"
        f"published: \"\"\n"
        f"tags: [{topic}]\n"
        f"extracted_concepts: []\n"
        f"extracted_entities: []\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        f"---\n"
    )
    # 摘要與要點區塊留空，讓使用者在 Obsidian 手動補填
    template = (
        "\n## 摘要（3 句內）\n\n"
        "（待填寫）\n\n"
        "## 關鍵要點\n\n"
        "- （待填寫）\n\n"
        "## 此篇與知識庫哪些頁面有關\n\n"
        "- （待填寫）\n\n"
        "---\n\n"
    )
    return frontmatter + template + cleaned_text


def stage1_pdf(pdf_path: Path, title: str | None = None) -> bool:
    today = datetime.now().strftime("%Y-%m-%d")
    slug  = make_slug(title or pdf_path.stem)
    draft = CLIPPINGS / f"{slug}.md"

    if draft.exists():
        print(f"  [略過] 草稿已存在：{draft.name}")
        return False

    print(f"\n── [Stage 1] {pdf_path.name}")
    print("  [1/3] marker：PDF → 原始 Markdown…")
    raw_text = pdf_to_raw_markdown(pdf_path)

    # 本地去噪：移除頁碼、壓縮空行
    print("  [2/3] 本地去噪…")
    raw_text = preclean_raw_text(raw_text)

    # 組裝草稿（純本地，不呼叫任何 API）
    print(f"  [3/3] 組裝草稿（{len(raw_text):,} 字元）…")
    draft_content = build_draft_md(raw_text, slug, today)
    draft.write_text(draft_content, encoding="utf-8")

    print(f"  ✓ 草稿已寫入：Notes/Clippings/{draft.name}")
    print(f"  → 請在 Obsidian 補填摘要 / 要點後，執行 --ingest 正式入庫")
    return True


# ════════════════════════════════════════
# Stage 2：草稿 .md → 知識庫 Sources
# ════════════════════════════════════════

def stage2_md(md_path: Path, title: str | None = None) -> bool:
    slug     = make_slug(title or md_path.stem)
    raw_text = md_path.read_text(encoding="utf-8")

    print(f"\n── [Stage 2] {md_path.name}")
    # 本地 keyword 分類，不呼叫 API
    print(f"  [1/4] 本地分類：決定入庫位置…")
    topic     = classify_topic(raw_text)
    page_name = title or md_path.stem

    source_dir  = SOURCES / topic
    source_dir.mkdir(parents=True, exist_ok=True)
    source_path = source_dir / f"{slug}.md"

    if source_path.exists():
        print(f"  [略過] Source 已存在：知識庫/Sources/{topic}/{slug}.md")
        return False

    print(f"  [2/4] 寫入：知識庫/Sources/{topic}/{slug}.md")
    source_path.write_text(raw_text, encoding="utf-8")

    print(f"  [3/4] 更新 index.md → [[{page_name}]]")
    update_index(page_name)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    append_log(
        f"- {now} `pdf_ingest --ingest` [[{page_name}]] → "
        f"`知識庫/Sources/{topic}/{slug}.md`  來源：`{md_path.name}`"
    )

    print("  [4/4] 歸檔…")
    CLIPPINGS_ARCHIVE.mkdir(parents=True, exist_ok=True)
    shutil.move(str(md_path), str(CLIPPINGS_ARCHIVE / md_path.name))

    # 若 Clippings 內有同名 PDF，一併移至 Notes/pdf/
    pdf_path = CLIPPINGS / f"{md_path.stem}.pdf"
    if pdf_path.exists():
        PDF_ARCHIVE.mkdir(parents=True, exist_ok=True)
        shutil.move(str(pdf_path), str(PDF_ARCHIVE / pdf_path.name))
        print(f"    PDF 歸檔：Notes/pdf/{pdf_path.name}")

    print(f"  ✓ [[{page_name}]] → 知識庫/Sources/{topic}/")
    return True


# ════════════════════════════════════════
# main
# ════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(description="Clippings 兩階段自動入庫")
    parser.add_argument("--ingest", action="store_true",
                        help="Stage 2：將 Clippings 中的 .md 草稿正式入庫")
    parser.add_argument("--pdf",    help="單檔模式 Stage 1：指定 PDF 路徑")
    parser.add_argument("--md",     help="單檔模式 Stage 2：指定 .md 路徑")
    parser.add_argument("--title",  help="自訂頁面標題（單檔模式有效）")
    args = parser.parse_args()

    CLIPPINGS.mkdir(parents=True, exist_ok=True)

    # ── 單檔模式
    if args.pdf:
        p = Path(args.pdf).resolve()
        if not p.exists():
            sys.exit(f"[錯誤] 找不到：{p}")
        stage1_pdf(p, args.title)
        return

    if args.md:
        p = Path(args.md).resolve()
        if not p.exists():
            sys.exit(f"[錯誤] 找不到：{p}")
        stage2_md(p, args.title)
        return

    # ── 批次模式
    if args.ingest:
        # Stage 2：處理 Clippings 中所有 .md
        mds = sorted(
            f for f in CLIPPINGS.glob("*.md")
            if f.is_file()
        )
        if not mds:
            print("Notes/Clippings/ 中沒有 .md 草稿可入庫。")
            return
        print(f"找到 {len(mds)} 個草稿，開始入庫…")
        done, skipped = 0, 0
        for md_path in mds:
            try:
                if stage2_md(md_path):
                    done += 1
                else:
                    skipped += 1
            except Exception as e:
                print(f"  [錯誤] {md_path.name}：{e}")
        print(f"\n入庫完成：成功 {done} 個，略過 {skipped} 個。")
        print("建議接著執行 sync-vault 同步到 GitHub。")

    else:
        # Stage 1：處理 Clippings 中所有 .pdf
        pdfs = sorted(CLIPPINGS.glob("*.pdf"))
        if not pdfs:
            print("Notes/Clippings/ 中沒有 .pdf 檔案。")
            print(f"請將 PDF 放入：{CLIPPINGS}")
            return
        print(f"找到 {len(pdfs)} 個 PDF，產生草稿…")
        done, skipped = 0, 0
        for pdf_path in pdfs:
            try:
                if stage1_pdf(pdf_path):
                    done += 1
                else:
                    skipped += 1
            except Exception as e:
                print(f"  [錯誤] {pdf_path.name}：{e}")
        print(f"\nStage 1 完成：產生 {done} 個草稿，略過 {skipped} 個。")
        print("請在 Obsidian 確認草稿後，執行：python scripts/pdf_ingest.py --ingest")


if __name__ == "__main__":
    main()
