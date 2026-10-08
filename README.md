# thesis-notes-template

給碩士生用的 Obsidian 論文筆記庫範本：五種筆記的模板、文獻筆記的填寫規則、一張文獻矩陣表，和五段可以直接貼給 AI 的 prompt。下載解壓縮，用 Obsidian 打開就能用。

Prompt 只是文字，不綁特定 AI 工具，repo 裡也沒有任何 AI 工具的設定檔。目前用 Claude Code 和 Codex 測過部分段落，網頁版、Mac 和從零安裝還沒測；哪幾段測過、怎麼測的，見 mis-thesis-guide [範本說明頁](https://wayhong0928.github.io/mis-thesis-guide/pages/thesis-notes-template.html)第七節。

介紹頁：<https://wayhong0928.github.io/thesis-notes-template/>

## 下載與開啟

**用 AI 安裝**：有 Claude Code 或 Codex 的話，把 [`00_總覽/prompt.md`](00_總覽/prompt.md) 第 0 段貼給它。它會裝好 Zotero、Obsidian、Python 和 PyMuPDF，下載這個範本，再一步一步帶你點完 Better BibTeX 和 Obsidian 的設定。

**自己來**：

1. 按這頁上方的綠色 **Code** → **Download ZIP**，解壓縮到你想放的地方（例：`文件/碩士論文/02_筆記`）。
2. 打開 Obsidian，選「開啟資料夾作為儲存庫」（Open folder as vault），選剛解壓縮的資料夾。
3. 先讀 `00_總覽/開始使用.md`。

## 裡面有什麼

```
00_總覽/
├── 開始使用.md          第一眼看的短版說明
├── 研究設計速查.md      研究問題、假說表、構念對假說
├── 術語表.md            構念的標準中譯、英文原名、量表來源、文獻中的別名
├── 文獻筆記填寫規則.md  頁碼、數字、TBD、構念譯名、證據強度用詞、自我核對清單
├── prompt.md            安裝 prompt＋五段工作 prompt（網頁版＋CLI 版）
└── 文獻矩陣.base        所有文獻筆記排成一張表
01_理論/  02_變數/  03_文獻筆記/  04_論文草稿/  05_假設推演/  06_方法/
07_模板/                 理論、變數、文獻筆記三型、假設推演、方法，共 7 份
```

每個資料夾裡的 `說明.md` 寫了檔名規則和用法。`Davis1989`、`PU_知覺有用性`、`知覺有用性→使用意圖` 三份是填好的示範，看懂後可以刪。

## 幾個設計上的決定

- **文獻筆記不寫你自己的假說編號。** 論文卡只連到構念卡；假說編號只出現在 `研究設計速查.md` 和推演卡的 `hypothesis` 欄。假說改版、重新編號時，文獻筆記一份都不用動。
- **推演卡用關係命名**（`知覺有用性→使用意圖`），不把 H 編號放進檔名。
- **原論文的構念照原文翻**，不改成你研究的構念名稱，對應關係只寫在變項表。
- **寧可寫 TBD，也不能寫錯。** 第二章會直接從筆記取材。
- **AI 寫的筆記要開新對話核對**，寫的那個對話看不出自己的錯。

## 第一週清單

- [ ] Zotero 裝好 Better BibTeX，設好 citekey 公式（見下一節）
- [ ] Zotero 的日期欄位統一格式（例如一律填 `YYYY-MM-DD` 或只填 `YYYY`）；格式不一致時，citekey 可能解析不出年份
- [ ] 決定中文作者姓名用單欄還是兩欄，語言欄填 `zh-TW`（見下一節最後的連結）
- [ ] 填 `術語表.md` 和 `研究設計速查.md`（可以用 prompt 第 1 段請 AI 從計畫書填初稿）
- [ ] 讀 `文獻筆記填寫規則.md`，寫第一份文獻筆記
- [ ] 把整個資料夾放進有版本紀錄的雲端硬碟，另外每月手動備份一次

## Zotero 怎麼接

筆記庫和 Zotero 靠 **citekey** 對上：文獻筆記的檔名就是 citekey，例如 `Davis1989.md`。

- **citekey 公式**：Better BibTeX 的預設公式是 `auth.lower + shorttitle(3,3) + year`（作者姓氏＋標題前三個字＋年份）。範本的示範用的是較短的 `auth.capitalize + year`（產生 `Davis1989`），同作者同年份時 Better BibTeX 會自動加 a、b 字尾。兩種都可以，選定後就不要再換。改公式不會自動改掉既有的 key，要選取項目後手動 Refresh（[Better BibTeX 官方說明](https://retorque.re/zotero-better-bibtex/citing/)）。
- **citekey 定了就不改**：筆記改名會讓連結斷掉。
- **PDF 留在 Zotero 就好**：CLI 版的 prompt 會透過 Better BibTeX，用 citekey 查出 PDF 在 Zotero 存放區的位置直接讀，不用另外複製或改檔名。跑的時候 Zotero 要開著。

中文作者姓名用單欄還是兩欄、語言欄怎麼填，見 mis-thesis-guide 文獻管理頁的[〈中文文獻：作者姓名與語言欄〉](https://wayhong0928.github.io/mis-thesis-guide/pages/tools-knowledge.html)（2.3.8）；校外連線、Better BibTeX 安裝、Word 引用也在同一頁。範本不需要任何 Obsidian 外掛，想用 Zotero 相關外掛的話，各外掛的維護狀況見[範本說明頁](https://wayhong0928.github.io/mis-thesis-guide/pages/thesis-notes-template.html)第二節。

## 寫作流程

1. **找論文**：看 `研究設計速查.md` 哪條假說證據薄，帶著缺口去找。
2. **讀＋做筆記**：在 Zotero 的 PDF 上劃線，照填寫規則寫論文卡。
3. **推導假說**：先寫推演卡，看清每條箭頭需要哪幾篇證據撐；缺證據就回第 1 步。
4. **收料進構念卡**：打開構念卡，從反向連結看有哪些論文卡提供了材料，整理成定義、共識、爭議。
5. **寫進正文**：面對構念卡、推演卡、方法卡寫 `04_論文草稿`，不直接面對論文卡。
6. **收尾**：Zotero 產生參考文獻；對照假說表，確認每條假說在第二章有文獻、在第三章有推導。

## 回報問題

模板或 prompt 有錯、照步驟做不出來，請到 [Issues](https://github.com/wayhong0928/thesis-notes-template/issues) 回報。

## 同系列

| 資源 | 適合誰 |
|---|---|
| [mis-thesis-guide](https://wayhong0928.github.io/mis-thesis-guide/) | 研究方法與論文寫作的知識庫，查觀念、查判準 |
| [一小時上手](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart.html) | 只用 ChatGPT、Claude、Gemini 網頁版，想在一小時內建好論文助手（另有 [Claude Code、Codex 版](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart-agent.html)） |
| [thesis-notes-template](https://github.com/wayhong0928/thesis-notes-template) | 想用 Obsidian 做文獻筆記，要現成的模板和填寫規則 |
| [mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills) | 用 Claude Code 或 Codex，想讓 AI 照固定判準檢查題目與寫作 |

## 授權

MIT。示範筆記引用的 Davis（1989）原文版權屬原出版者，筆記只摘錄定義與數字並附頁碼。
