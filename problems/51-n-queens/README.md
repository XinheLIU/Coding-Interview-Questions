---
id: 51
title: N Queens
slug: n-queens
difficulty:
topics: [dfs]
leetcode: https://leetcode.com/problems/n-queens/
relations: [{"type": "specializes", "target": 52, "reason": "N-Queens II only counts solutions, so the same diagonal-conflict DFS increments a counter instead of materialising boards."}, {"type": "same-pattern", "target": 37, "reason": "Sudoku Solver is the same constraint-propagation backtracking: place, check conflicts, recurse, undo."}]
---

# 51. N Queens

> Notes / intuition / complexity — TODO.

<<< @/problems/51-n-queens/solution.py
