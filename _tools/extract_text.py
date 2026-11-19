"""把 Zotero 裡的論文 PDF 轉成每頁標好頁碼的純文字，存到 _text/{citekey}.txt。

在筆記庫根目錄執行，Zotero 要開著：
    python _tools/extract_text.py Davis1989 Venkatesh2003
不經過 Zotero、直接指定 PDF（一次只能一篇）：
    python _tools/extract_text.py Davis1989 --pdf "<PDF 路徑>"

已經有文字檔的會跳過，加 --force 重新產生。
每頁開頭有一行「===== PDF p. N =====」，N 是 PDF 檔的第幾頁（從 1 起算），不是期刊印的頁碼。
需要 Zotero 裝好 Better BibTeX（用 --pdf 時不用），以及 PyMuPDF：python -m pip install pymupdf
"""
import argparse
import json
import sys
import urllib.request
from pathlib import Path

RPC_URL = "http://127.0.0.1:23119/better-bibtex/json-rpc"
ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = ROOT / "_text"


def zotero_pdfs(citekey):
    """回傳 (PDF 路徑清單, 錯誤訊息)。連不上 Zotero 直接結束程式。"""
    body = json.dumps({"jsonrpc": "2.0", "method": "item.attachments", "params": [citekey]}).encode()
    req = urllib.request.Request(RPC_URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            reply = json.load(resp)
    except (OSError, ValueError) as exc:
        sys.exit(f"連不上 Zotero 的 Better BibTeX（{exc}）。請確認 Zotero 開著，而且裝了 Better BibTeX。")
    if "error" in reply:
        return [], reply["error"].get("message", str(reply["error"]))
    paths = [a.get("path", "") for a in reply.get("result") or []]
    return [p for p in paths if p.lower().endswith(".pdf")], None


def find_pdf(citekey, pdf=None):
    """找出 citekey 對應的 PDF。找不到或有好幾個時回傳 (None, 說明)。"""
    if pdf:
        path = Path(pdf)
        return (path, None) if path.is_file() else (None, f"找不到檔案 {pdf}")
    pdfs, err = zotero_pdfs(citekey)
    if err:
        return None, f"Zotero 回報：{err}（citekey 拼錯，或這篇還沒進 Zotero）"
    if not pdfs:
        return None, "Zotero 裡這篇沒有附 PDF"
    if len(pdfs) > 1:
        listing = "\n".join(f"    {p}" for p in pdfs)
        return None, f"Zotero 裡有 {len(pdfs)} 個 PDF，不知道用哪個，請用 --pdf 指定：\n{listing}"
    return Path(pdfs[0]), None


def load_fitz():
    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("還沒裝 PyMuPDF，請先跑：python -m pip install pymupdf")
    return fitz


def extract(citekey, pdf_path):
    fitz = load_fitz()

    with fitz.open(pdf_path) as doc:
        parts = [f"# {citekey}\n# 共 {doc.page_count} 頁（頁碼是 PDF 檔的頁序）\n"]
        for i, page in enumerate(doc, 1):
            parts.append(f"\n===== PDF p. {i} =====\n{page.get_text('text')}")
        pages = doc.page_count
    TEXT_DIR.mkdir(exist_ok=True)
    (TEXT_DIR / f"{citekey}.txt").write_text("".join(parts), encoding="utf-8")
    return pages


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="把 PDF 轉成帶頁碼標記的純文字，存到 _text/。")
    ap.add_argument("citekeys", nargs="+", help="一個或多個 citekey")
    ap.add_argument("--pdf", help="直接指定 PDF 路徑，不經過 Zotero（只能配一個 citekey）")
    ap.add_argument("--force", action="store_true", help="文字檔已存在也重新產生")
    args = ap.parse_args(argv)
    if args.pdf and len(args.citekeys) > 1:
        ap.error("--pdf 一次只能配一個 citekey")

    failed = 0
    for key in args.citekeys:
        out = TEXT_DIR / f"{key}.txt"
        if out.exists() and not args.force:
            print(f"{key}：_text/{key}.txt 已存在，跳過（要重做加 --force）")
            continue
        pdf_path, err = find_pdf(key, args.pdf)
        if err:
            print(f"{key}：{err}")
            failed += 1
            continue
        try:
            pages = extract(key, pdf_path)
        except Exception as exc:  # PDF 壞掉、加密等
            print(f"{key}：轉檔失敗（{exc}）")
            failed += 1
            continue
        print(f"{key}：{pages} 頁 → _text/{key}.txt")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
