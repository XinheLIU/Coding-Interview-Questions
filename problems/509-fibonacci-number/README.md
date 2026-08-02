---
id: 509
title: Fibonacci Number
slug: fibonacci-number
difficulty: Easy
topics: [dynamic-programming, recursion]
leetcode: https://leetcode.com/problems/fibonacci-number/
relations: [{"type": "specializes", "target": 70, "reason": "Climbing Stairs counts two-step paths — recurrence is identical, dp[n] = F(n+1)."}]
---

# 509. Fibonacci Number

Last updated: 2026-08-02

## Why this problem matters

The canonical example of overlapping subproblems. Naive recursion is `O(2^n)` because it recomputes the same state exponentially many times. Memoization or bottom-up DP makes it `O(n)` — you pay for each state exactly once.

## The extensibility

- **Space optimization**: The recurrence only looks back 2 states, so the full table collapses to two rolling variables (`O(1)` space).
- **Matrix exponentiation**: `O(log n)` time via `[[1,1],[1,0]]^n`.
- **Different step rules**: Tribonacci (`dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`), or generalized k-step variants.
- **Equivalent problems**: Climbing Stairs (#70), House Robber with no adjacency constraint, any "count paths in a linear state graph" problem.

## Variations to ask

1. What if you can take 1, 2, or 3 steps? (Tribonacci)
2. What if each step has a cost, and you want minimum cost to reach step n? (Min Cost Climbing Stairs #746)
3. What if the state is 2D instead of 1D? (Triangle #120, Unique Paths #62)

*Time* `O(n)`, *space* `O(1)` (space-optimized DP).

<<< @/problems/509-fibonacci-number/solution.py
