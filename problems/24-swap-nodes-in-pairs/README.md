---
id: 24
title: Swap Nodes In Pairs
slug: swap-nodes-in-pairs
difficulty: Medium
topics: [linked-list]
leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/
relations: [{"type": "builds-on", "target": 206, "reason": "Reuses the save-next-then-relink discipline of in-place reversal, bounded to a window of two nodes."}]
---

# 24. Swap Nodes In Pairs

Last updated: 2026-08-10

## Why this problem matters

The smallest problem where a dummy head genuinely pays for itself. Swapping the first pair
changes the head of the list, so without a sentinel you write one branch for the head and
another for every interior pair. With one, there is only the interior case.

## The key insight

**Hold the node *before* the pair, and the swap is three assignments in a fixed order.**
Given `prev → first → second`, you want `prev → second → first`. Write `first.next = second.next`
first: the moment `second.next` points back at `first`, the original successor is unreachable and
the rest of the list is gone.

The loop guard `prev.next and prev.next.next` is what leaves a lone final node untouched — the
required behaviour for odd-length lists, and the boundary this problem is really testing.

All four implementations below use the same names: `dummy`, `prev`, `first`, `second`.

## Python

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.py

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per pair

The recursion never needs `prev`: the caller is holding it. Each frame swaps its own two nodes
and trusts the recursive call to hand back an already-swapped remainder.

<<< @/problems/24-swap-nodes-in-pairs/solution.v2.py

## C++

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.cpp

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per pair

<<< @/problems/24-swap-nodes-in-pairs/solution.v2.cpp

## The extensibility

- **Swap in groups of k** — [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
  widens the window from 2 to k. The new difficulty is that you must confirm k nodes remain
  *before* committing to the relink, which the `k = 2` guard hides.
- **Swap values instead of nodes** would be a two-line problem. The interviewer is checking that
  you noticed the problem says nodes — it matters as soon as a node carries more than a value, or
  external references point at it.
- **Doubly linked** turns three assignments into six, and the `prev` you track manually becomes a field.
- **Conditional swaps** ("swap only pairs summing to an even number") keep this skeleton exactly
  and add a predicate before the relink.

## Variations to ask

1. Reverse in groups of k instead of pairs. (*Tests whether the window generalizes.*)
2. Solve it without a dummy node. (*Watch them handle the head as a separate branch — and count the bugs.*)
3. What does your solution do with an odd number of nodes? (*The guard is the answer; many candidates never state it.*)
4. Recursive or iterative — which would you ship, and why? (*Wants the `O(n)` stack named out loud.*)
