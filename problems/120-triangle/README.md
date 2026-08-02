---
id: 120
title: Triangle
slug: triangle
difficulty: Medium
topics: [array, dynamic-programming]
leetcode: https://leetcode.com/problems/triangle/
relations: [{"type": "builds-on", "target": 509, "reason": "Extends the 1D recurrence to 2D — dp[i][j] depends on two neighbors below instead of one behind."}, {"type": "builds-on", "target": 64, "reason": "Same minimum-path-sum DP structure, but the grid is a triangle and you work bottom-up instead of top-down."}]
---

# 120. Triangle

Last updated: 2026-08-02

## Why this problem matters

The first **2D recurrence** in the DP progression. Fibonacci and Climbing Stairs are 1D (`dp[i]` depends only on `dp[i-1]` and `dp[i-2]`). Triangle is 2D (`dp[i][j]` depends on `dp[i+1][j]` and `dp[i+1][j+1]`), but the transition is still local — each cell picks the minimum of two neighbors. This is the bridge between linear DP and grid DP (Unique Paths, Minimum Path Sum).

## The key insight

**Bottom-up beats top-down here.** Starting from the bottom row, each cell has exactly 2 reachable neighbors below it. Top-down would mean multiple paths converging at each cell, requiring tracking of all incoming paths. Bottom-up makes the transition trivial: `dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]`.

## The extensibility

- **Space optimization**: Each row depends only on the row below, so you can collapse the 2D table to a 1D array of length `n` — the solution reuses the last row.
- **In-place modification**: If mutating the input is allowed, modify `triangle[i][j]` directly instead of using a separate DP array (`O(1)` extra space).
- **Different constraints**: What if you can skip at most K rows? What if each cell has a different set of reachable neighbors?
- **Other grid shapes**: Rectangular grid (Minimum Path Sum #64), restricted directions (Unique Paths #62), obstacles (Unique Paths II #63).

## Variations to ask

1. What if the triangle is upside-down (top-down instead of bottom-up)?
2. What if you must collect the actual path, not just the minimum sum?
3. What if each cell has 3 or 4 reachable neighbors instead of 2?
4. What if the triangle has negative values and you want the **maximum** sum instead?

## Solution variants

This problem has two implementations with different space trade-offs:
- `solution.py` (below) — Bottom-up DP with space optimization (reuse last row)
- `solution.v2.py` — In-place DP modifying the input triangle

*Time* `O(n²)` where n is the number of rows, *space* `O(n)` → `O(1)` if in-place.

<<< @/problems/120-triangle/solution.py
