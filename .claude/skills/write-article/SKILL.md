---
name: write-article
description: Write or rewrite prose chapters (articles/blog posts) for this repo's VitePress book (book/*.md). Use when the user asks to write, rewrite, or translate a chapter, article, or blog post here — especially turning notes (often Chinese) into an English piece. Encodes the house style: concise, insight-first, written for experienced engineers/interviewers.
---

# Writing articles for this book

Prose chapters live in `book/*.md`. They explain the *why* — code itself is transcluded from `problems/`, never pasted. When writing or rewriting a chapter, follow the house style below.

## Audience & altitude

Write for **experienced engineers and interviewers**, not learners.

- **Skip the basics.** Assume the reader knows the Big-O table, what contiguous memory is, what a pointer is. Don't define terms; don't walk through mechanics they already own.
- **Lead with the insight, not the definition.** The first sentence of a section should say something worth knowing, not restate the topic.
- **Every line earns its place.** If a sentence only confirms what the reader already assumes, cut it.

## What to keep vs. cut

Keep the high-signal material:

- **Non-obvious moves** — the O(1) unordered-array insert, mark-and-sweep batch delete, why `prev` earns its keep. Tricks, not textbook facts.
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

- Embed solutions with `<<< @/problems/<id>-<slug>/solution.<ext>` — never paste code into the chapter. Use `#region` anchors for excerpts, never line numbers.
- Add/refresh a `Last updated: YYYY-MM-DD` line near the top (project rule).
- A new chapter must be registered by hand in `.vitepress/config.mts` (`nav`/`sidebar`); adding the file alone won't surface it.
- Verify with `npm run docs:build` — it fails on broken `@/` includes and dead links.
