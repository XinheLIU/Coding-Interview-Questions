---
id: 17
title: Letter Combinations Of A Phone Number
slug: letter-combinations-of-a-phone-number
difficulty: Medium
topics: [back-tracking, dfs]
leetcode: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
relations: []
---

# 17. Letter Combinations Of A Phone Number

The simplest backtracking problem, and the clearest template to memorize. Each digit maps to 3–4 letters; the search tree is the Cartesian product of those letters. There is exactly **no pruning** — every path from root to leaf is a valid answer the moment its length reaches `len(digits)`. This is what separates it from 39/40: there the branch is a *sum*, so a partial path can over- or under-shoot and must be pruned; here the only stop condition is depth.

**Intuition.** Fix one letter for the first digit, then recursively combine the rest, then fix the next letter — a textbook depth-first walk where the level of recursion *is* the digit index.

- **State:** `level` (which digit we are filling).
- **Choice:** one of the 3–4 letters of `digits[level]`.
- **Terminate** (record `out`): `len(out) == len(digits)`.
- **No backtrack/undo needed** in the `out + i` style — `out + i` builds a *new* string, so the parent's `out` is untouched. Undo (`append`/`pop`) only matters once `out` is a shared mutable list.

**Complexity.** With `n` digits and `m` (≤4) letters per digit, there are `m^n` leaves, each an `O(n)` string copy → **time O(n·4^n)**, **space O(n)** recursion depth plus O(4^n) output storage.

<<< @/problems/17-letter-combinations-of-a-phone-number/solution.py

## Variants

`solution.v2.py` is the same recursion as a **closure** carrying `kvmaps`/`res` in scope instead of passing them as parameters — fewer args, same shape. Once you internalize "what must change each level, what stays constant", you can read or write either form freely. See [book/dfs.md](/book/dfs) for the two canonical parameter styles.

<<< @/problems/17-letter-combinations-of-a-phone-number/solution.v2.py
