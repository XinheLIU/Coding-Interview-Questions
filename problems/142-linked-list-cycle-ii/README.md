---
id: 142
title: Linked List Cycle II
slug: linked-list-cycle-ii
difficulty: Medium
topics: [linked-list, two-pointers]
leetcode: https://leetcode.com/problems/linked-list-cycle-ii/
relations: [{"type": "builds-on", "target": 141, "reason": "Phase 1 is Floyd's detection unchanged; phase 2 adds a second walk from the head that meets at the cycle entry."}]
---

# 142. Linked List Cycle II

Last updated: 2026-08-10

## Why this problem matters

The payoff for actually proving [141](https://leetcode.com/problems/linked-list-cycle/) instead of
memorizing it. Phase 1 is unchanged; phase 2 is four lines that fall directly out of the algebra. If
you only remembered "fast and slow meet", there is nothing here to derive from.

## The key insight

**The meeting point is not arbitrary — it is exactly as far from the entry as the head is.**

Let `F` be the head-to-entry distance, `a` the entry-to-meeting distance, and `L` the cycle length.
When they meet, slow has walked `F + a` and fast has walked `2(F + a)`; their difference is a whole
number of laps, so `F + a ≡ 0 (mod L)`. That rearranges to `F ≡ L - a`: walking `F` steps from the
head and `L - a` steps forward from the meeting point land on the same node.

So phase 2 is just two pointers at *equal* speed — one from `head`, one from the meeting point —
and where they collide is the answer.

Names carry over from #141: `slow`, `fast`.

## Python

### Floyd's, two phases

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/142-linked-list-cycle-ii/solution.py

## The extensibility

- **Find the duplicate in an array** — [287](https://leetcode.com/problems/find-the-duplicate-number/)
  is this problem in disguise. Treat `i → nums[i]` as a linked list: values in `[1, n]` over `n + 1`
  slots force a cycle, and its entry is the duplicate. Same two phases, no extra space, input untouched.
- **Cycle length** — hold one pointer at the meeting point and walk the other around; that count is `L`.
- **Remove the cycle** — once you have the entry, walk to the node before it and null its `next`.
- **The general theorem** is about functional graphs, not lists: any function iterated from a start
  point traces a rho shape, and Floyd's finds its tail length and cycle length. That is the basis of
  Pollard's rho for integer factorization.

## Variations to ask

1. Prove that phase 2 works. (*The one question that separates derivation from memorization.*)
2. Find the duplicate number in an array of `n + 1` integers in `[1, n]`, without modifying it. (*#287 — same machinery, unrecognizable surface.*)
3. Return the cycle's length as well as its entry. (*One extra traversal.*)
4. Remove the cycle in place. (*Needs the node before the entry, not the entry itself.*)
