# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Last updated: 2026-07-07

## What this repo is

Two layers over the same files:

1. **A problem-first LeetCode solution library** — one folder per problem at `problems/<id>-<slug>/` (bare, un-padded id), holding every language solution together (`solution.py`, `solution.cpp`, `solution.sql`) plus a `README.md` whose YAML frontmatter is the problem's metadata (`id`, `title`, `difficulty`, `topics`, `leetcode`). A second approach in the same language is `solution.<variant>.<ext>` (e.g. `solution.v2.py`, `solution.dp.py`). Most solutions are authored via the LeetCode VS Code extension (they carry `@lc app=leetcode ...` / `@lc code=start|end` markers). Files with no derivable LeetCode id are parked in `problems/_unresolved/`.
2. **A VitePress "book"** (`book/*.md`) that reads those solution files as the single source of truth. There is no separate copy of the code — chapters transclude the real files.

## The one architectural idea that matters: code transclusion

The book never pastes code. Each chapter embeds a solution file with VitePress's file-include syntax:

```
<<< @/problems/1143-longest-common-subsequence/solution.py
```

- `srcDir` is the repo root, so the `@` alias resolves to the repo root. Any chapter, anywhere, references any solution with a stable `@/`-rooted path.
- Sync is **one-way**: solution file → book. Edit the `.py`, save → dev server hot-reloads the rendered block; push → Pages rebuilds. Editing the rendered block does nothing to the file.
- Only `.md` files become pages. The `.py/.cpp/.sql` files are never rendered as standalone pages — they exist only to be included.
- **Consequence:** the include path is keyed by the immutable problem id, so it almost never changes. Editing a solution or re-tagging its topics needs no Markdown edit; only physically moving a problem folder does.

Each `problems/<id>-<slug>/README.md` is itself a page (a VitePress `rewrites` rule serves it as the folder index, so `/problems/<id>-<slug>/` resolves while GitHub still renders the README in folder view).

To spotlight part of a long file instead of the whole thing, add `#region name` / `#endregion` comment anchors in the source and reference `@/path#name` — never line numbers (they break on edits).

## Topic/difficulty browsing is generated, not filed

Folders no longer encode topic — `topics` in each README's frontmatter does. `scripts/gen_index.py` reads all frontmatter and (re)writes `book/by-topic/<topic>.md`, `book/by-difficulty/<level>.md`, and `.vitepress/sidebar-problems.json` (imported by `config.mts`). **Never hand-edit those generated pages** — re-run the script instead.

## Commands

```bash
npm install            # first-time setup (Node already required)
npm run docs:dev       # local book at http://localhost:5173/Coding-Interview-Questions/
npm run docs:build     # production build to .vitepress/dist (fails on broken @/ includes AND dead links)
npm run docs:preview   # serve the built site
python3 scripts/gen_index.py   # regenerate topic/difficulty indexes + sidebar from frontmatter
python3 scripts/reorg.py       # one-time language-first → problem-first migration (dry-run; --apply to execute)
```

Verifying a change end-to-end = run `docs:build` (catches broken includes and dead links) and/or grep `.vitepress/dist/**/*.html` for a source line to confirm it was transcluded.

## Config that will bite you

- `.vitepress/config.mts` hardcodes `base: '/Coding-Interview-Questions/'`. This must match the GitHub repo name or Pages links 404. Change it if the repo is renamed or a custom domain is used.
- `.github/workflows/deploy.yml` deploys on push to `master`. It requires a one-time repo setting: **Settings → Pages → Source → "GitHub Actions"**.
- The **prose** chapters and top-level nav in `config.mts` are hand-maintained (adding a `book/<name>.md` does not auto-register it). The **topic/difficulty** sidebar groups come from `sidebar-problems.json` and update only when you re-run `gen_index.py`.
- `.vscode/settings.json` sets `leetcode.filePath` so the extension writes new solves straight to `problems/${id}-${kebab-case-name}/solution.${ext}`. `${id}` is not zero-padded — that is why problem folders use bare ids.

## Adding a problem

Solve it via the LeetCode extension (it lands in `problems/<id>-<slug>/solution.<ext>` automatically), or create that folder by hand. Add/point its `README.md` with frontmatter (`id`, `title`, `difficulty`, `topics`, `leetcode`), then run `python3 scripts/gen_index.py` so it appears in the topic/difficulty indexes.

## Adding a prose chapter

Create `book/<name>.md` (prose = problem, intuition, complexity, the "why"), embed solutions with `<<< @/problems/<id>-<slug>/solution.<ext>` lines, then add it to the `sidebar`/`nav` in `.vitepress/config.mts`. Never duplicate code into the Markdown.
