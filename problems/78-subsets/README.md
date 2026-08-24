---
id: 78
title: Subsets
slug: subsets
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/subsets/
relations: [{"type": "specializes", "target": 90, "reason": "Subsets II has duplicate elements — sort and skip the same element at the same DFS depth to de-dup."}]
---

# 78. Subsets

## Intuition

Subsets is the **simplest backtracking pattern**: enumerate all possible subsequences. Unlike combinations (which fix a target size `k`) or permutations (which exhaust all elements), subsets **record at every node** — an empty `out` is valid, `[1]` is valid, `[1,2]` is valid, all the way to the full array.

Key differences from other backtracking problems:
- **No base-case check** — `ret.append(out)` fires *before* recursion, not inside an `if`.
- **No pruning** — every branch is a valid subset; the only bound is `start` advancing to prevent `[1,2]` and `[2,1]` duplicates.
- **The `start` index** prevents revisiting earlier choices: each recursive call starts from `i+1`, ensuring subsets stay in input order and avoid duplicates like `[2,1]` vs `[1,2]`.

The tree looks like:

```
            []
       /    |    \
     [1]   [2]   [3]
    /  \    |
 [1,2][1,3][2,3]
   |
[1,2,3]
```

Every node in this tree is a valid subset — 8 subsets for 3 elements (2³).

## Complexity

- **Time**: O(2ⁿ · n) — 2ⁿ subsets, each taking O(n) to copy into `ret`
- **Space**: O(n) call stack depth (not counting output array)

## Code Notes

The solution uses the **immutable parameter style** (`out + [nums[i]]`), so no `undo` step needed. The commented alternative shows **mutable style** (`out.append` / `out.pop()`) with explicit `out[:]` copy — same algorithm, different bookkeeping.

<<< @/problems/78-subsets/solution.cpp
<<< @/problems/78-subsets/solution.py
