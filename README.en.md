[繁體中文](README.md) | English

# thesis-notes-template

An Obsidian vault template for master's students taking thesis notes: templates for five kinds of notes, rules for filling in literature notes, a literature matrix, and five prompts you can paste straight into an AI tool. Download, unzip, and open the folder in Obsidian.

**All notes, templates, and prompts are in Traditional Chinese.** This page is the only English part.

The prompts are plain text and don't depend on any AI tool, and the repo contains no AI tool configuration files. Some sections have been tested with Claude Code and Codex; the web apps, Mac, and installing from scratch haven't been tested yet. Which sections were tested and how is in section 7 of the [template guide page](https://wayhong0928.github.io/mis-thesis-guide/pages/thesis-notes-template.html) on mis-thesis-guide (Chinese).

Intro page (Chinese): <https://wayhong0928.github.io/thesis-notes-template/>

## Download and open

**Install with AI**: if you have Claude Code or Codex, paste section 0 of [`00_總覽/prompt.md`](00_總覽/prompt.md) into it. It installs Zotero, Obsidian, Python, and PyMuPDF, downloads this template, and walks you through the Better BibTeX and Obsidian settings step by step.

**By hand**:

1. Click the green **Code** button at the top of this page, then **Download ZIP**, and unzip it wherever you like (for example `Documents/Thesis/02_notes`).
2. Open Obsidian, choose "Open folder as vault", and pick the unzipped folder.
3. Read `00_總覽/開始使用.md` (Getting started) first.

## What's inside

```
00_總覽/                 Overview
├── 開始使用.md          Getting started: the short version
├── 研究設計速查.md      Research design sheet: research questions, hypothesis table, which constructs each hypothesis uses
├── 術語表.md            Glossary: standard Chinese translation, English name, scale source, and aliases in the literature for each construct
├── 文獻筆記填寫規則.md  Literature note rules: page numbers, figures, TBD, construct translations, evidence-strength wording, self-check list
├── prompt.md            Install prompt plus five working prompts (web app and CLI versions)
└── 文獻矩陣.base        Literature matrix: all literature notes in one table
01_理論/ (theories)  02_變數/ (variables)  03_文獻筆記/ (literature notes)
04_論文草稿/ (thesis drafts)  05_假設推演/ (hypothesis derivations)  06_方法/ (methods)
07_模板/                 Templates: theory, variable, three types of literature note, hypothesis derivation, method (7 in total)
```

Folders `01` to `06` each have a `說明.md` (readme) with its file naming rules and usage. `Davis1989`, `PU_知覺有用性` (perceived usefulness), and `知覺有用性→使用意圖` (perceived usefulness → intention to use) are filled-in examples; delete them once you've got the idea.

## Design decisions

- **Literature notes don't carry your own hypothesis numbers.** A paper note links only to construct notes. Hypothesis numbers appear only in `研究設計速查.md` and in the `hypothesis` field of derivation notes, so when you revise or renumber hypotheses, no literature note has to change.
- **Derivation notes are named after the relationship** (`知覺有用性→使用意圖`), with no H number in the file name.
- **Constructs from the original paper are translated as the paper names them**, not renamed to match your study. The mapping lives only in the variable table.
- **Write TBD rather than something wrong.** Chapter 2 draws directly on these notes.
- **Check AI-written notes in a new conversation.** The conversation that wrote a note can't see its own mistakes.

## First-week checklist

- [ ] Install Better BibTeX in Zotero and set the citekey formula (see the next section)
- [ ] Use one date format in Zotero (for example always `YYYY-MM-DD`, or only `YYYY`); with mixed formats, the citekey may fail to pick up the year
- [ ] Decide whether Chinese author names go in one field or two, and set the language field to `zh-TW` (see the link at the end of the next section)
- [ ] Fill in `術語表.md` and `研究設計速查.md` (prompt 1 can ask an AI to draft them from your proposal)
- [ ] Read `文獻筆記填寫規則.md` and write your first literature note
- [ ] Put the whole folder in a cloud drive with version history, and back it up by hand once a month

## Connecting Zotero

The vault and Zotero are matched by **citekey**: a literature note's file name is its citekey, for example `Davis1989.md`.

- **Citekey formula**: Better BibTeX's default formula is `auth.lower + shorttitle(3,3) + year` (author surname, first three words of the title, year). The template's examples use the shorter `auth.capitalize + year` (which gives `Davis1989`); Better BibTeX adds a, b suffixes when the same author has two papers in one year. Either works, but pick one and keep it. Changing the formula doesn't update existing keys; you have to select the items and Refresh them by hand ([Better BibTeX documentation](https://retorque.re/zotero-better-bibtex/citing/)).
- **Don't change a citekey once it's set**: renaming a note breaks its links.
- **Leave PDFs in Zotero**: the CLI prompts use Better BibTeX to look up a PDF's location in Zotero storage by citekey and read it there, so you don't need to copy or rename files. Zotero has to be running.

Whether Chinese author names go in one field or two, and how to fill in the language field, is covered in ["Chinese sources: author names and the language field"](https://wayhong0928.github.io/mis-thesis-guide/pages/tools-knowledge.html) (2.3.8) on the mis-thesis-guide reference management page (Chinese), along with off-campus access, Better BibTeX installation, and citing in Word. The template needs no Obsidian plugins. If you want a Zotero-related plugin, section 2 of the [template guide page](https://wayhong0928.github.io/mis-thesis-guide/pages/thesis-notes-template.html) covers how well each one is maintained.

## Writing workflow

1. **Find papers**: check which hypotheses in `研究設計速查.md` have thin evidence and search with that gap in mind.
2. **Read and take notes**: highlight the PDF in Zotero and write the paper note following the rules.
3. **Derive hypotheses**: write the derivation note first to see which papers each arrow needs; if evidence is missing, go back to step 1.
4. **Gather into construct notes**: open a construct note, use its backlinks to see which paper notes supply material, and organize it into definitions, agreements, and disputes.
5. **Write the thesis**: write `04_論文草稿` from construct, derivation, and method notes, not from paper notes directly.
6. **Wrap up**: generate the reference list from Zotero; go through the hypothesis table and confirm each hypothesis has literature in chapter 2 and a derivation in chapter 3.

## Reporting problems

If a template or prompt is wrong, or the steps don't work, report it in [Issues](https://github.com/wayhong0928/thesis-notes-template/issues).

## Same series

| Resource | For |
|---|---|
| [mis-thesis-guide](https://wayhong0928.github.io/mis-thesis-guide/) | A knowledge base on research methods and thesis writing, for looking up concepts and criteria |
| [One-hour quickstart](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart.html) | Students who only use the ChatGPT, Claude, or Gemini web apps and want a thesis assistant set up in an hour (there's also a [Claude Code and Codex version](https://wayhong0928.github.io/mis-thesis-guide/pages/ai-quickstart-agent.html)) |
| [thesis-notes-template](https://github.com/wayhong0928/thesis-notes-template) | Students who want to take literature notes in Obsidian with ready-made templates and filling rules |
| [mis-thesis-skills](https://github.com/wayhong0928/mis-thesis-skills) | Students using Claude Code or Codex who want AI to check topics and writing against fixed criteria |
| [claude-workflow-template](https://github.com/wayhong0928/claude-workflow-template) | Students using Claude Code on a thesis or research project who want a ready-made workflow setup: session handoff, dispatch templates, independent verification |

## License

MIT. Davis (1989), quoted in the example note, is copyrighted by its original publisher; the note excerpts only definitions and figures, with page numbers.
