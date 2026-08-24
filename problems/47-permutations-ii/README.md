---
id: 47
title: Permutations II
slug: permutations-ii
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/permutations-ii/
relations: []
---

# 47. Permutations II

## Intuition

Permutations II = Permutations + **input has duplicates** + **output must be unique**. The fix is the same as Combination Sum II: **sort first, then skip duplicate siblings at the same recursion depth**.

The key line:
```python
if i and nums[i] == nums[i-1]: continue
```

Why `i` (not `i > 0`)? Because this solution uses **slice-based candidate shrinking** (`nums[:i] + nums[i+1:]`) — each recursive call receives a *new* array, so the first element is always index 0. Checking `i > 0` would allow the first duplicate; checking `i` (nonzero) skips it.

Example: `[1,1,2]` sorted produces:
```
Level 0:  [1, 1, 2]  → pick first 1, skip second 1 (duplicate sibling), pick 2
Level 1:  [1, 2] or [1, 2] or [1, 1]  → each sees a fresh sliced array
```

The commented alternative uses a **visited array** with `nums[i] == nums[i-1] and not visited[i-1]` — same logic, different bookkeeping. The condition means: "if the previous identical element was not used in this branch, skip the current one" (ensures duplicates are used left-to-right).

## Complexity

- **Time**: O(n! · n) worst-case (all unique), but pruning reduces it significantly when many duplicates exist
- **Space**: O(n) recursion depth

## Code Notes

The slice-based dedup (`if i and nums[i] == nums[i-1]`) is simpler than the visited-based variant but relies on the candidate pool being sliced each call. If switching to a visited array (for memory efficiency), the condition changes to `if nums[i] == nums[i-1] and not visited[i-1]`.

<<< @/problems/47-permutations-ii/solution.py
