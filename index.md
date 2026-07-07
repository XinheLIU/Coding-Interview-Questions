---
layout: home

hero:
  name: "Coding Interview Notes"
  text: "A book + synced code"
  tagline: Prose chapters whose code blocks stay in sync with the actual solution files.
  actions:
    - theme: brand
      text: Dynamic Programming
      link: /book/dynamic-programming
    - theme: alt
      text: SQL
      link: /book/sql

features:
  - title: One source of truth
    details: Every code block is pulled straight from a solution file. Edit the file, the book updates — no copy-paste drift.
  - title: Practice by topic
    details: Chapters group problems by pattern so you build knowledge structures instead of memorizing one-offs.
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

> How this book stays in sync: code blocks use VitePress file includes
> (`<<< @/Python/79.word-search.py`). The `.py` / `.cpp` / `.sql` files under this
> repo are the single source of truth — the book renders their current contents.
