---
id: 74
title: Search A 2 D Matrix
slug: search-a-2-d-matrix
difficulty: medium
topics: [binary-search, 2d-array]
leetcode: https://leetcode.com/problems/search-a-2-d-matrix/
relations: [{"type": "specializes", "target": 240, "reason": "Search a 2D Matrix II loses the fully-sorted-flattening property, so the search walks from a corner instead of halving."}]
---

# 74. Search A 2 D Matrix

## Approach: Binary Search with Index Mapping

The matrix is sorted row-wise and column-wise such that you can treat it as a flattened sorted array. Map 1D binary search indices back to 2D coordinates.

**Key insight**: For a matrix with `n` columns, `row = mid // n` and `col = mid % n`.

**Time**: O(log(m×n))  
**Space**: O(1)

<<< @/problems/74-search-a-2-d-matrix/solution.py

## Alternate Approach: Staircase Search

Start from top-right (or bottom-left). Move left if current > target, down if current < target. This works for the more general case (problem 240) but is O(m+n) instead of O(log(m×n)).

<<< @/problems/74-search-a-2-d-matrix/solution.v2.py
