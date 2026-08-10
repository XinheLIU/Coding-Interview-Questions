---
id: 232
title: Implement Queue using Stacks
slug: implement-queue-using-stacks
difficulty: Easy
topics: [queue, stack]
leetcode: https://leetcode.com/problems/implement-queue-using-stacks/
relations: []
---

# 232. Implement Queue using Stacks

Last updated: 2026-08-10

## Why this problem matters

The standard interview vehicle for **amortized analysis**. Every individual `pop` looks like it might
cost `O(n)`, and a candidate who stops there gives the wrong complexity. The right answer requires
arguing about a *sequence* of operations rather than one — which is the actual skill being tested,
and the same argument that justifies dynamic array growth.

## The key insight

**Pouring one stack into another reverses it, and two reversals give back the original order.**
Push onto `in_stack`; when you need the front, pour everything into `out_stack` and the oldest
element is now on top.

The subtle part is *when* to pour. **Refill `out_stack` only when it is empty.** Pour early — while
`out_stack` still holds elements — and newer elements land on top of older ones, breaking FIFO.
That guard is also what makes the amortized bound work: each element is pushed and popped at most
once per stack, so `n` operations cost `O(n)` total no matter how they interleave.

Names say what each stack is *for*, not what order it was declared in: `in_stack`, `out_stack`.

## Python

### Two stacks with lazy transfer

*Time* — `push` and `empty` are `O(1)` worst case; `pop` and `peek` are amortized `O(1)`, worst case
`O(n)` on the one call that triggers a refill. *Space* `O(n)`.

<<< @/problems/232-implement-queue-using-stacks/solution.py

## The extensibility

- **The mirror problem** — [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
  is not symmetric. Queues can't be reversed by pouring, so you pay `O(n)` on every push (or every pop)
  with no amortization to hide behind. Worth doing both to see why the trick only works one way.
- **Two stacks make a deque?** Not quite, with this scheme: alternating front and back operations
  force a pour every time and the amortized argument collapses to `O(n)` per op.
- **The same amortization argument** covers dynamic array doubling, the mark-and-sweep batch delete,
  and monotonic-stack problems where each element is pushed and popped once.
- **A functional queue** uses exactly this two-list structure — it is how persistent queues get
  amortized `O(1)` in ML and Haskell.

## Variations to ask

1. What is the worst-case cost of a single `pop`, and the amortized cost? (*The whole point — expect `O(n)` and `O(1)`.*)
2. Prove the amortized bound. (*Wants "each element moves between stacks at most once".*)
3. Why not pour on every `push` instead? (*Still correct, but now `push` is `O(n)` with no amortization.*)
4. Now implement a stack using queues. (*#225 — and explain why it's worse.*)
5. What breaks if you refill `out_stack` while it still has elements? (*FIFO order — the guard is load-bearing.*)
