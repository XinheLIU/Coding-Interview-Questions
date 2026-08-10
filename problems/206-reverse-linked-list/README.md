---
id: 206
title: Reverse Linked List
slug: reverse-linked-list
difficulty: Easy
topics: [linked-list]
leetcode: https://leetcode.com/problems/reverse-linked-list/
relations: [{"type": "specializes", "target": 92, "reason": "Reverse sublist [m,n] by inserting each node after the anchor rather than reversing the whole list."}]
---

# 206. Reverse Linked List

Last updated: 2026-08-10

## Why this problem matters

The primitive the rest of the linked-list chapter is built from. Swap in pairs, reverse in k-groups,
palindrome check, reorder list — all of them reverse a segment somewhere. Owning the three-pointer
dance here means those problems reduce to "where do I stop".

## The key insight

**Reversal is one saved pointer away from being trivial.** Flipping `cur.next` destroys the only
route to the rest of the list, so the forward link must be read *before* it is overwritten. That
single constraint is the whole problem — every approach below is a different way of respecting it.

Three distinct techniques appear across the two languages:

- **Pointer flip** — walk forward, reverse one link per step; `prev` accumulates the reversed prefix.
- **Recursive** — recurse to the tail, flip links on the way back up. The original tail is returned
  unchanged through every frame.
- **Head insertion** — pin `cur` to the original head and repeatedly splice the *following* node to
  the front. Nothing is flipped; the order emerges by construction.

Shared names throughout: `head`, `prev`, `cur`, `next_node`, `new_head`, `dummy`.

## Python

### Iterative pointer flip

*Time* `O(n)`, *space* `O(1)`

Python's tuple assignment evaluates the entire right side before binding anything — which is exactly
the read-before-overwrite rule this problem demands, so the usual temporary disappears.

<<< @/problems/206-reverse-linked-list/solution.py

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per node, and a long list will exhaust Python's stack

<<< @/problems/206-reverse-linked-list/solution.v2.py

## C++

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per node

<<< @/problems/206-reverse-linked-list/solution.cpp

### Iterative head insertion

*Time* `O(n)`, *space* `O(1)`

A genuinely different idea from the pointer flip, and the one that generalizes: because it splices
after a fixed anchor, it is the technique
[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) needs in order to
reverse only a sublist.

<<< @/problems/206-reverse-linked-list/solution.v2.cpp

## The extensibility

- **Reverse a sublist `[m, n]`** — [92](https://leetcode.com/problems/reverse-linked-list-ii/).
  Head insertion wins: anchor before position `m`, splice `n - m` nodes, done. Adapting the pointer
  flip instead means stitching three segments back together.
- **Reverse in k-sized groups** — [25](https://leetcode.com/problems/reverse-nodes-in-k-group/) applies
  this in a loop, plus a length check before committing to each group.
- **Palindrome linked list** — [234](https://leetcode.com/problems/palindrome-linked-list/) reverses the
  second half in place after finding the midpoint with fast/slow pointers, giving `O(1)` space.
- **The recursion is the instructive failure mode.** It is the prettier code and the wrong answer in
  production: `O(n)` stack on unbounded input. Keeping both variants is what makes that visible.

## Variations to ask

1. Do it recursively, then tell me why you wouldn't ship it. (*Wants the stack depth named out loud.*)
2. Reverse only the nodes between positions m and n. (*Head insertion falls out; pointer flip struggles.*)
3. Reverse every k nodes, leaving a short final group as-is. (*Composition plus a length pre-check.*)
4. Check whether the list is a palindrome in `O(1)` space. (*Reversal as a subroutine, not the answer.*)
