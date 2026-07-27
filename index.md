---
layout: home

hero:
  name: "Coding Interview Notes"
  text: "A knowledge graph of solved problems"
  tagline: Seven chapters in learning order, every problem linked to what it builds on — with code pulled straight from the solution files.
  actions:
    - theme: brand
      text: Start with Linear Structures
      link: /book/linear-structures
    - theme: alt
      text: Browse by topic
      link: /book/by-topic/array

features:
  - title: One source of truth
    details: Every code block is pulled straight from a solution file. Edit the file, the book updates — no copy-paste drift.
  - title: A graph, not a list
    details: Problems carry typed relationships — builds-on, specializes, contrasts — each with a stated reason. Series like Climbing Stairs → House Robber are explicit edges, not something you have to notice.
  - title: The "why", not just the "what"
    details: Prose focuses on intuition, invariants, and complexity; the code carries the details.
---

## Principles

* Build knowledge structures
* Deliberate practice — 5 to 7 passes per question, then expand
* Constant feedback
* Study by topic and review

## 7 Steps for a Coding Interview

1. **Listen & clarify**
2. **Example** — big, non-special cases
3. **Brute force** first
4. **Optimize** — improve step by step; enumerate all possible solutions
5. **Walk through** — explain clearly; state time & space complexity
6. **Code** — clean indentation, precise naming, modularization
7. **Test** — small/fast cases, then edge cases, then large cases

## How this book is wired

**Code never gets pasted.** Chapters embed the real solution files with VitePress
file includes (`<<< @/problems/70-climbing-stairs/solution.py`). The `.py` / `.cpp`
/ `.sql` files are the single source of truth — edit one and the page follows.

**Structure is generated, not maintained.** Each problem's `README.md` frontmatter
carries its `topics` and its `relations`; `scripts/gen_index.py` rolls those up into
the chapter map above, the topic and difficulty indexes, and the sidebar.
`scripts/taxonomy.py` is the one place that decides which topics belong to which
chapter.

**The graph grows deliberately.** A relationship needs a stated reason naming the
shared invariant — a shared topic tag is not evidence.
`python3 scripts/suggest_relations.py` reports where the graph is still thin, which
is where the next edge should go.
