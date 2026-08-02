---
id: 152
title: Maximum Product Subarray
slug: maximum-product-subarray
difficulty: Medium
topics: [array, dynamic-programming]
leetcode: https://leetcode.com/problems/maximum-product-subarray/
relations: [{"type": "builds-on", "target": 53, "reason": "Same 'max ending at i' DP structure, but tracks both max and min because negatives flip signs."}]
---

# 152. Maximum Product Subarray

Last updated: 2026-08-02

## Why this problem matters

The first twist on Maximum Subarray (#53). It shows that when the operation isn't monotonic (negatives flip signs), you must track **both extremes** — today's minimum might become tomorrow's maximum when multiplied by another negative.

## The key insight

**Sign flips break the single-extremum assumption.** In Maximum Subarray, keeping the running max is enough because addition is monotonic. Multiplication isn't: `(-10) * (-5) = 50`. So you track both `dp_max[i]` and `dp_min[i]` at each position, and when you see a negative number, swap them conceptually — the transition already does this by taking `max(...)` over all three choices.

## The extensibility

- **Zero handling**: Zeros reset both max and min to zero — the `max(nums[i], ...)` choice handles this.
- **Subarray with constraints**: Maximum Product Subarray with at most K zeros, or exactly one negative allowed.
- **Divide instead of multiply**: Similar tracking, but division by zero or negatives would need explicit handling.
- **Other non-monotonic operations**: Any DP where the operation can flip the optimality (min ↔ max) needs dual tracking.

## Variations to ask

1. What if we can skip at most K elements in the subarray?
2. What if zeros are not allowed, or we must include exactly one zero?
3. What if we track the actual subarray boundaries, not just the product?
4. What if the array is circular (wraparound allowed)?

*Time* `O(n)`, *space* `O(1)` (rolling array).

<<< @/problems/152-maximum-product-subarray/solution.py
