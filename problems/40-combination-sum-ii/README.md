---
id: 40
title: Combination Sum Ii
slug: combination-sum-ii
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/combination-sum-ii/
relations: [{"type": "specializes", "target": 216, "reason": "Restricts candidates to 1-9 with a fixed count, changing only the range passed to DFS."}]
---

# 40. Combination Sum Ii

39 + **no reuse** + **duplicate candidates**. That second addition is the interesting one: `candidates` may contain the same number twice, yet the answer may not contain the same *combination* twice. Two distinct definitions of "duplicate" that every interviewer checks you can tell apart.

**Two changes from 39, and exactly one point of care.**

1. **No reuse** → pass `i+1` so a candidate is consumed at most once.
2. **Duplicate values** → sort, then skip `candidates[i]` when `i > start and candidates[i] == candidates[i-1]`.

**Why sort + skip, and why `i > start` not `i > 0`.** Sorting clusters equal values together. At a given tree level, once you've *started* a branch with the first `1`, the second `1` at the same level would only regenerate the same combinations, so we skip it. The guard is `i > start` because that skips the *sibling* duplicate at the current level while still allowing the `[1,1,…]` case — where the second `1` is chosen one level *deeper* (there `start` has advanced past the first `1`, so it is not skipped). `i > 0` would wrongly forbid any two equal values ever sharing a combination, killing `[1,1,6]`.

**Contrast with 39** (also see its README): 39 passes `i` (reuse) and needs no dedup because each value appears once; 40 passes `i+1` (no reuse) and needs the sort+skip because values can repeat.

**Pruning** is the same as 39: `target < 0` → return, `== 0` → record. `solution.py` subtracts (`target - candidates[i]`), the O(1) idiom.

**Complexity.** Worst-case O(2^n) leaves (each candidate in or out), each path O(n) to copy → **time O(n·2^n)**, **space O(n)** depth + output.

<<< @/problems/40-combination-sum-ii/solution.py

## Variants

`solution.v2.py` — uses `sum(out)` for termination instead of subtracting `target`; otherwise identical logic (closure style, `i+1`, same sort+skip). Slower termination check but easier to read if you prefer comparing against the raw target.

<<< @/problems/40-combination-sum-ii/solution.v2.py
