"""從 PDF 某一頁裁下原文的圖，存成 PNG。裁的是原圖，不重畫。

在筆記庫根目錄執行：
    python _tools/crop_figure.py <citekey> <PDF頁序> <圖號> <x0> <y0> <x1> <y1>
例如裁 Davis1989 第 5 頁的 Figure 1，範圍是頁面上半部：
    python _tools/crop_figure.py Davis1989 5 1 0.08 0.12 0.92 0.55

座標是頁面寬、高的比例（0 到 1），左上角是 0 0、右下角是 1 1。
先用 0 0 1 1 裁整頁，打開 PNG 看圖在哪裡，再縮小範圍；最後確認圖完整、沒切到圖說或正文。
PDF 從 Zotero 找（要開著），跟 extract_text.py 一樣；也可以加 --pdf 直接指定。
解析度預設 200 dpi，要更清楚加 --dpi 300。同一個圖號再裁一次會蓋掉舊的 PNG。
輸出到 03_文獻筆記/附件_模型圖/{citekey}_Fig{圖號}.png，
筆記裡用 ![[附件_模型圖/{citekey}_Fig{圖號}.png]] 嵌入。
需要 PyMuPDF：python -m pip install pymupdf
"""
import argparse
import sys

sys.dont_write_bytecode = True  # 不在 _tools/ 留 __pycache__
from extract_text import ROOT, find_pdf, load_fitz  # noqa: E402

FIG_DIR = ROOT / "03_文獻筆記" / "附件_模型圖"


def ratio(value):
    v = float(value)
    if not 0 <= v <= 1:
        raise argparse.ArgumentTypeError(f"{value} 不在 0 到 1 之間")
    return v


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="從 PDF 某頁裁下原文的圖，存成 PNG。")
    ap.add_argument("citekey")
    ap.add_argument("page", type=int, help="PDF 頁序，從 1 起算，跟 _text/ 的分頁標記相同")
    ap.add_argument("fig", help="圖號，用在檔名，例如 1 或 2a")
    ap.add_argument("box", nargs=4, type=ratio, metavar=("x0", "y0", "x1", "y1"))
    ap.add_argument("--pdf", help="直接指定 PDF 路徑，不經過 Zotero")
    ap.add_argument("--dpi", type=int, default=200)
    args = ap.parse_args(argv)
    x0, y0, x1, y1 = args.box
    if x0 >= x1 or y0 >= y1:
        ap.error("範圍要左上比右下小：x0 < x1、y0 < y1")

    pdf_path, err = find_pdf(args.citekey, args.pdf)
    if err:
        print(f"{args.citekey}：{err}")
        return 1

    fitz = load_fitz()
    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:  # PDF 壞掉、不是 PDF
        print(f"{args.citekey}：打不開 PDF（{exc}）")
        return 1

    with doc:
        if not 1 <= args.page <= doc.page_count:
            print(f"{args.citekey}：這個 PDF 只有 {doc.page_count} 頁")
            return 1
        page = doc[args.page - 1]
        r = page.rect
        clip = fitz.Rect(r.width * x0, r.height * y0, r.width * x1, r.height * y1)
        FIG_DIR.mkdir(parents=True, exist_ok=True)
        out = FIG_DIR / f"{args.citekey}_Fig{args.fig}.png"
        page.get_pixmap(dpi=args.dpi, clip=clip).save(out)
    print(f"{args.citekey}：第 {args.page} 頁 → {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
