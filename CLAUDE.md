# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Last updated: 2026-07-27

## What this repo is

Two layers over the same files:

1. **A problem-first LeetCode solution library** — one folder per problem at `problems/<id>-<slug>/` (bare, un-padded id), holding every language solution together (`solution.py`, `solution.cpp`, `solution.sql`) plus a `README.md` whose YAML frontmatter is the problem's metadata (`id`, `title`, `difficulty`, `topics`, `leetcode`, `relations`). A second approach in the same language is `solution.<variant>.<ext>` (e.g. `solution.v2.py`, `solution.dp.py`). Most solutions are authored via the LeetCode VS Code extension (they carry `@lc app=leetcode ...` / `@lc code=start|end` markers). Files with no derivable LeetCode id are parked in `problems/_unresolved/`.
2. **A VitePress "book"** (`book/*.md`) that reads those solution files as the single source of truth. There is no separate copy of the code — chapters transclude the real files.

The book is organised as **seven chapters in learning order**, not a flat topic list: Linear Structures → Trees & Heaps → Recursion & Divide and Conquer → Search & Sort → Dynamic Programming → Techniques, with SQL off to the side as a separate skill. Every problem lands in exactly one chapter, and problems carry typed relationships to each other. The homepage renders the chapter map; each chapter page renders its own prerequisite DAG and a full index.

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

## Chapters, topics, and relationships are all generated

Folders no longer encode topic — `topics` in each README's frontmatter does. `scripts/gen_index.py` reads all frontmatter and (re)writes `book/by-topic/<topic>.md`, `book/by-difficulty/<level>.md`, `.vitepress/sidebar-problems.json`, and `.vitepress/problem-graph.json`. **Never hand-edit those generated files** — re-run the script instead.

### `scripts/taxonomy.py` is the one place chapter membership is decided

Every topic tag is declared there exactly once, mapping to a chapter, a section within it, and a **priority**. A problem's chapter is decided by its highest-priority topic, so a problem tagged `[binary-tree, recursion]` lands in Trees (33) rather than Recursion (63) — priority encodes "which idea is this problem actually teaching".

Consequences worth knowing before you touch it:

- **An undeclared topic fails the build.** `gen_index.py` raises rather than silently creating an orphan topic page. Add the tag to `TOPICS` or fix the typo.
- **Changing a priority moves problems between chapters in bulk.** Re-run `gen_index.py` and check the printed per-chapter counts.
- **A single problem can be re-homed** with a `chapter:` line in its frontmatter, which overrides the computed chapter. Use it sparingly — if you need it more than a handful of times, the priorities are wrong.
- Tags describe *the technique the solution uses*, not the problem's surface. Binary search discards a half rather than combining sub-answers, so it is not `divide-and-conquer`; quickselect and merge sort are.

Problem-to-problem knowledge is stored as typed, directed `relations` in the source problem's frontmatter. Keep the value as valid inline JSON because the generator is stdlib-only:

```yaml
relations: [{"type": "builds-on", "target": 20, "reason": "Reuses stack-based parenthesis matching, then tracks substring boundaries."}]
```

- Supported types: `builds-on`, `generalizes`, `specializes`, `same-pattern`, `contrasts`.
- `target` is the stable bare problem id. The generator derives reverse relationships; do not duplicate them in the target README.
- `reason` is required and must name the shared invariant, transformation, or meaningful contrast. A shared topic alone is not evidence.
- When adding or resolving a problem, inspect its solution and existing problems for a defensible `builds-on` predecessor. If the relationship is unclear, ask the user; do not invent an edge.
- The custom VitePress theme reads the generated graph and shows the current problem's incoming and outgoing relationships after its solution content.

`python3 scripts/suggest_relations.py` reports where the graph is thin: title series missing an internal edge, per-chapter link coverage, and sections with zero relations. It is read-only and suggests *candidates* — you still have to read both solutions before writing an edge. `--chapter <id>` scopes it; `--isolated` lists the unconnected problems by name.

Only relations with **both endpoints in the same chapter** appear in that chapter's graph. Cross-chapter edges are real and show on both problem pages; the chapter page reports their count rather than pretending the chapter is self-contained.

## Commands

```bash
npm install            # first-time setup (Node already required)
npm run docs:dev       # local book at http://localhost:5173/Coding-Interview-Questions/
npm run docs:build     # production build to .vitepress/dist (fails on broken @/ includes AND dead links)
npm run docs:preview   # serve the built site
python3 scripts/gen_index.py         # regenerate chapter data, topic/difficulty indexes, sidebar, graph
python3 scripts/suggest_relations.py # read-only: report where the knowledge graph is still thin
python3 scripts/reorg.py             # one-time language-first → problem-first migration (dry-run; --apply)
```

Verifying a change end-to-end = run `docs:build` (catches broken includes and dead links) and/or grep `.vitepress/dist/**/*.html` for a source line to confirm it was transcluded.

## Config that will bite you

- `.vitepress/config.mts` hardcodes `base: '/Coding-Interview-Questions/'`. This must match the GitHub repo name or Pages links 404. Change it if the repo is renamed or a custom domain is used.
- `.github/workflows/deploy.yml` deploys on push to `master`. It requires a one-time repo setting: **Settings → Pages → Source → "GitHub Actions"**.
- The **prose** chapters and top-level nav in `config.mts` are hand-maintained (adding a `book/<name>.md` does not auto-register it). The **topic/difficulty** sidebar groups come from `sidebar-problems.json` and update only when you re-run `gen_index.py`.
- The `Chapters` sidebar list in `config.mts` duplicates the chapter *reading order* that `scripts/taxonomy.py` declares in `CHAPTERS`. Adding or reordering a chapter means editing both. The taxonomy decides which problems go where; `config.mts` decides what the sidebar shows.
- `<ChapterGraph>`, `<ChapterIndex>`, and `<CurriculumMap>` are registered globally in `.vitepress/theme/index.ts`, so chapter Markdown uses them without an import. Both chapter components take a `chapter="<id>"` prop that must match a `CHAPTERS` id — a typo renders an empty section rather than failing the build.
- `.vscode/settings.json` sets `leetcode.filePath` so the extension writes new solves straight to `problems/${id}-${kebab-case-name}/solution.${ext}`. `${id}` is not zero-padded — that is why problem folders use bare ids.

## Adding a problem

Solve it via the LeetCode extension (it lands in `problems/<id>-<slug>/solution.<ext>` automatically), or create that folder by hand. Then:

1. Add/point its `README.md` frontmatter (`id`, `title`, `difficulty`, `topics`, `leetcode`, `relations`). Every topic must already exist in `scripts/taxonomy.py`.
2. Read the solution and look for a defensible predecessor. `python3 scripts/suggest_relations.py --chapter <id>` shows what is nearby and unconnected.
3. Run `python3 scripts/gen_index.py` — it validates the topics, resolves the chapter, and regenerates the indexes, sidebar, and graph.

## Adding a prose chapter

Create `book/<name>.md` (prose = problem, intuition, complexity, the "why"), embed solutions with `<<< @/problems/<id>-<slug>/solution.<ext>` lines, then add it to the `sidebar`/`nav` in `.vitepress/config.mts`. Never duplicate code into the Markdown.

For a **curriculum chapter** rather than a template deep-dive, also: add the chapter to `CHAPTERS` in `scripts/taxonomy.py` (with its grid `col`/`row` for the homepage map) and point some topics at it, set `chapter: <id>` in the page's own frontmatter, and end the page with `<ChapterGraph chapter="<id>" />` and `<ChapterIndex chapter="<id>" />`.
