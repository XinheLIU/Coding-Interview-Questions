---
id: 77
title: Combinations
slug: combinations
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/combinations/
relations: []
---

# 77. Combinations

## Intuition

Combinations is the **textbook backtracking problem**: choose `k` elements from `1..n` where **order doesn't matter** and **no reuse**. The two constraints translate directly to code:

1. **Order doesn't matter** → use a `start` index to skip earlier choices (prevents `[1,2]` and `[2,1]` being counted twice)
2. **No reuse** → each recursive call passes `i+1` as the new `start`
3. **Fixed size** → base case triggers when `len(out) == k`

This is the **pure combination template** with no extra complications (no duplicates in input, no pruning needed beyond size check).

The tree for `n=4, k=2`:

```
              start=1
        /   |   |   \
       1    2   3   4
      /|\   |\   |
     2 3 4  3 4  4
    [1,2][1,3][1,4][2,3][2,4][3,4]
```

Each branch narrows the candidate pool by advancing `start`. The tree stops at depth `k`.

## Complexity

- **Time**: O(C(n,k) · k) — C(n,k) = n!/(k!(n-k)!) combinations, each taking O(k) to copy
- **Space**: O(k) recursion depth

## Code Notes

The commented versions show alternative parameter styles — closure (`self.res`), mutable append/pop — but the core algorithm is identical: `start` index + size-based termination. No sorting or deduplication needed because input is already `1..n` with no duplicates.

<<< @/problems/77-combinations/solution.py
