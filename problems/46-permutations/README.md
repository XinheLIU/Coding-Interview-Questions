---
id: 46
title: Permutations
slug: permutations
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/permutations/
relations: [{"type": "specializes", "target": 47, "reason": "Permutations II has duplicates — sort and skip same-value elements at the same recursion level."}]
---

# 46. Permutations

## Intuition

Permutations is the **order-matters, exhaust-all-elements** backtracking pattern. Unlike combinations (which use a `start` index to skip earlier choices), permutations **revisit every position** but exclude already-chosen elements.

Key differences from combinations/subsets:
- **No `start` index** — each level loops through *all* remaining candidates, not just those after some cutoff
- **Shrinking candidate pool** — pass `nums[:i] + nums[i+1:]` to exclude the chosen element from child calls
- **Base case: empty pool** — when `nums` is exhausted, `out` contains a full permutation

The tree for `[1,2,3]`:

```
              [1,2,3]
        /       |       \
       1        2        3
      / \      / \      / \
     2   3    1   3    1   2
     |   |    |   |    |   |
     3   2    3   1    2   1
   [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
```

Each level has one fewer choice than the parent. Total permutations: n!.

## Complexity

- **Time**: O(n! · n) — n! permutations, each taking O(n) to slice and copy
- **Space**: O(n) recursion depth (not counting output or sliced arrays)

## Code Notes

This solution uses **slice-based exclusion** (`nums[:i] + nums[i+1:]`) to maintain the candidate pool — clean but allocates O(n) per recursive call. An alternative is a **visited array** (see problem 47's commented code), which is O(1) per recursion but adds mutable state. For small n (typical in interviews), the slice style is clearer.

<<< @/problems/46-permutations/solution.py
