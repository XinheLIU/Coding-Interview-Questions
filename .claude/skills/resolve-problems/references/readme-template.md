# Problem README template

Last updated: 2026-08-10

Copy this shape. Code presentation rules — naming, comments, complexity, heading layout —
live in `.claude/skills/shared/code-presentation.md`.

## Body order

```
frontmatter          id, title, slug, difficulty, topics, leetcode, relations
# <id>. <Title>
Last updated: YYYY-MM-DD

## Why this problem matters      what it teaches — one paragraph
## The key insight               the invariant every implementation below shares
## <Language>                    one H2 per language present on disk
   ### <Approach>                one H3 per 写法, each with complexity + transclusion
## The extensibility             axes of variation
## Variations to ask             numbered interview follow-ups
```

Prose first, code in the middle, prose last. The last section must be prose: the theme
injects its own `<h2>Knowledge graph` after the whole body, and it reads badly directly
under a code block.

Skip a section when you have nothing real to say in it. An empty "The extensibility" is
worse than no heading — but "Why this problem matters" and "The key insight" are never
skippable, they are the reason the page exists.

## Section guidance

**Why this problem matters** — what the problem *teaches*, not what it asks. "The first
subarray DP problem. It teaches you that `dp[i]` can mean best-ending-at-i rather than
best-up-to-i." Position it in the progression where you can: "the first 2D recurrence",
"the constrained version of #70".

**The key insight** — one bolded thesis sentence, then the mechanism. This is the 找共同点
step: state the invariant that every language and approach below shares, once, so the code
sections don't each re-explain it.

**Language / approach sections** — see the shared contract. Language H2 even when there is
only one language; approach H3 names the idea; complexity line under each H3 before the code.

**The extensibility** — the axes along which the problem generalizes: what constraint you
could add, what dimension you could raise, which problem family it opens onto. Link related
LeetCode problems inline here.

**Variations to ask** — numbered follow-ups an interviewer would use, each with a short
parenthetical on what it tests.

## Filled example

````markdown
---
id: 24
title: Swap Nodes In Pairs
slug: swap-nodes-in-pairs
difficulty: Medium
topics: [linked-list]
leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/
relations: [{"type": "builds-on", "target": 206, "reason": "Reuses the three-pointer relink of in-place reversal, but bounded to a window of two nodes."}]
---

# 24. Swap Nodes In Pairs

Last updated: 2026-08-10

## Why this problem matters

The smallest problem where a dummy head genuinely pays for itself. Swapping the first
pair changes the head, so without a sentinel you write one branch for the head and
another for the interior. With one, every pair is the interior case.

## The key insight

**Hold the node *before* the pair, and the swap is three assignments in a fixed order.**
With `prev → first → second`, you relink to `prev → second → first` — but only if you
save `second` before overwriting `first.next`, or you lose the rest of the list.

Both implementations below use the same names: `dummy`, `prev`, `first`, `second`.

## Python

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.py

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per pair

<<< @/problems/24-swap-nodes-in-pairs/solution.v2.py

## C++

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.cpp

## The extensibility

- **Swap in groups of k** — [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
  generalizes the window from 2 to k, and now you must check that k nodes remain before committing.
- **Swap values instead of nodes** — trivial here, but the interviewer is testing whether you
  noticed the problem says nodes. It matters when the node carries more than a value.
- **Odd tail handling** is the boundary that separates levels: the loop guard `prev.next and prev.next.next`
  leaves a lone final node untouched, which is the required behaviour.

## Variations to ask

1. Reverse in groups of k instead of pairs. (*Tests whether the window generalizes.*)
2. What changes if the list is doubly linked? (*Four pointers to fix, not two.*)
3. Do it without a dummy node. (*Watch them handle the head case separately.*)
4. Swap only pairs whose sum is even, leaving others in place. (*Conditional relink, same skeleton.*)
````
