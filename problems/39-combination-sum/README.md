---
id: 39
title: Combination Sum
slug: combination-sum
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/combination-sum/
relations: [{"type": "specializes", "target": 40, "reason": "Adds the no-reuse constraint: sort + skip duplicates in the DFS to avoid revisiting the same candidate."}, {"type": "builds-on", "target": 377, "reason": "Combination Sum IV counts ordered sequences — the counting version is a 1D knapsack DP rather than backtracking."}]
---

# 39. Combination Sum

The first backtracking problem where a partial answer can be **wrong**, so pruning and the `start` index become essential. Candidates may be reused, so each digit (candidate) is an unbounded supply.

**Intuition two-liner.** Walk a tree where each level picks the next candidate to add to `out`; `start` pins which candidates we are *still allowed* to try so order doesn't matter, and `sum(out) > target` is the prune that stops dead branches.

**The `start` index is the whole trick.** Without it, `[2,3]` and `[3,2]` would both be emitted because "add 3 then add 2" and "add 2 then add 3" are two different leaves. `start` enforces that candidates are only ever added in non-decreasing index order, so each *multiset* has exactly one tree path. This is the same mechanism that 40 uses, minus the "skip duplicates" line.

**Reuse means passing `i`, not `i+1`.** `for i in range(start, …): dfs(i, …)` permits choosing the *same* candidate again. Compare with 40, which passes `i+1` to forbid reuse — the single-character difference between the two problems.

**Pruning.** `sum(out) > target` → return (dead); `== target` → record a copy. Note the two solutions choose different stop conditions: `solution.py` compares `sum(out)` to `target`, while the commented block in `solution.v2.py` subtracts and tests `target == 0` / `target < 0`. Both are correct; the subtraction version is faster (O(1) per step vs. O(len) recomputing the sum).

**Complexity.** Worst case: `target / min(candidates)` choices deep with `n` branches each → time loosely **O(n^(T/m))**, space O(T/m) recursion depth (plus output). T = target, m = smallest candidate.

<<< @/problems/39-combination-sum/solution.py

## Variants

`solution.v2.py` — the **append/undo** form: `out.append(candidate)` … `dfs` … `out.pop()` mutates a single shared list instead of allocating `out + [candidate]` at every node. The commented block inside shows the subtract-style termination (`target - candidate`, recurse until `0`/`<0`), the more efficient idiom.

<<< @/problems/39-combination-sum/solution.v2.py
