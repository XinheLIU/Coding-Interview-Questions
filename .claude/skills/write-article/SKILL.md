---
name: write-article
description: Write or rewrite prose chapters (articles/blog posts) for this repo's VitePress book (book/*.md). Use when the user asks to write, rewrite, or translate a chapter, article, or blog post here — especially turning notes (often Chinese) into an English piece. Encodes the house style: concise, insight-first, written for experienced engineers/interviewers.
---

# Writing articles for this book

Last updated: 2026-08-10

Prose chapters live in `book/*.md`. They explain the *why* — code itself is transcluded from `problems/`, never pasted. When writing or rewriting a chapter, follow the house style below.

**Code presentation — naming, comments, complexity, and the heading layout for transcluded code — is in `.claude/skills/shared/code-presentation.md`.** It is shared with `resolve-problems` so chapters and problem READMEs show code the same way. Read it before you embed anything.

## Audience & altitude

Write for **experienced engineers and interviewers**, not learners.

- **Skip the basics.** Assume the reader knows the Big-O table, what contiguous memory is, what a pointer is. Don't define terms; don't walk through mechanics they already own.
- **Lead with the insight, not the definition.** The first sentence of a section should say something worth knowing, not restate the topic.
- **Every line earns its place.** If a sentence only confirms what the reader already assumes, cut it.

## Show the optimization journey, not just the final answer

When documenting a solution, **reveal the thought progression from straightforward to optimized**:

- **Start with the direct approach** — the table/array DP that works but isn't optimal. State what it does and why it's correct, not why it's slow (they can see that).
- **Name the optimization technique** — rolling array/variables, space collapse, in-place modification, bottom-up reversal. Use the standard term the reader will recognize.
- **Show what changed** — "The recurrence only looks back 2 states, so collapse to two variables" beats "we can optimize space." The constraint that permits the optimization is the insight.

Example progression:
1. Fibonacci — full `O(n)` table → two rolling variables `O(1)`, because the transition depth is 2
2. Triangle — `O(n²)` 2D table → `O(n)` 1D array reusing the last row, because each row depends only on the row below
3. Maximum Subarray — `O(n)` explicit DP array → in-place reuse of the input array `O(1)`

**Recognize space optimizations worth calling out:**
- **Rolling array/variables** — when the recurrence looks back k steps, you need only k slots
- **Dimension collapse** — 2D grid → 1D array when each row/column depends only on the previous
- **In-place DP** — reusing the input array when mutation is allowed
- **Reverse iteration** — bottom-up or right-to-left to avoid clobbering dependencies

Don't present these as tricks to memorize. Frame each as "the structure of the recurrence permits this" — the optimization follows from understanding the dependencies.

## What to keep vs. cut

Keep the high-signal material:

- **Non-obvious moves** — the O(1) unordered-array insert, mark-and-sweep batch delete, why `prev` earns its keep. Tricks, not textbook facts.
- **The progression from basic to optimized** — "here's the direct solution; here's what the dependencies actually are; here's the collapse that structure permits."
- **Applications, named concretely** — "LRU = doubly linked list + hash map, and here's why neither alone works," not "linked lists are used in many places."
- **Points to notice / gotchas** — pointer ordering, sentinel nodes, boundary cases that separate strong candidates.
- **The sharpened trade-off** — one crisp framing beats a comparison table.

Cut: introductions to fundamentals, restated Big-O walkthroughs, filler transitions, hedging, and anything a comparison table already implies.

## Rewrite, don't translate

When the source is notes (often Chinese), **rewrite** — restructure into a coherent argument, don't render line-by-line. Merge repeated points into one pass. Turn walls of bullets into a lead + tight sections.

## Form

- **Code over prose.** A 3–5 line example with a one-line "why" beats a paragraph. Show the failure mode (e.g. the pointer swap that drops the tail), not just the correct line.
- **Scannable headers.** Short, declarative section titles the reader can skim.
- **Tables sparingly** — only when the contrast is genuinely 2-dimensional, and only for readers who'd benefit. For an expert audience, a sentence usually wins.
- **Be concise by default.** Aim short; expand only where the insight demands it. If a draft feels long, it is — cut 40% and see what breaks.

## Repo mechanics

- Embed solutions with `<<< @/problems/<id>-<slug>/solution.<ext>` — never paste code into the chapter.
- **Every transcluded block carries a complexity line** directly above it: `*Time* \`O(n)\`, *space* \`O(1)\``. A chapter that shows code without its price is missing the point of the comparison.
- **When a chapter shows the same algorithm in more than one language, use the same `## <Language>` → `### <Approach>` shape the READMEs use** (see the shared contract). State the shared invariant once above the language sections rather than re-explaining it per language.
- **Identifiers in inline chapter snippets must match the solution file they illustrate.** A chapter that writes `prev` while the transcluded file says `pre` costs the reader a translation step. If they disagree, fix the solution file — it is the source of truth.
- To spotlight part of a long file, add `#region name` / `#endregion` anchors **to the source file first**, then reference `@/path#name`. Never line numbers. Note: no solution file in this repo carries anchors yet, so the first use means editing the source.
- Add/refresh a `Last updated: YYYY-MM-DD` line near the top (project rule).
- A new chapter must be registered by hand in `.vitepress/config.mts` (`nav`/`sidebar`); adding the file alone won't surface it. A curriculum chapter also needs its entry in `CHAPTERS` in `scripts/taxonomy.py` and the `<ChapterGraph>` / `<ChapterIndex>` components at the end.
- Verify with `npm run docs:build` — it fails on broken `@/` includes and dead links.
