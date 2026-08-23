---
id: 744
title: Find Smallest Letter Greater Than Target
difficulty: Easy
topics: [binary-search, array]
leetcode: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
---

# 744. Find Smallest Letter Greater Than Target

Given a sorted array of characters `letters` and a target character, find the smallest character in the array that is strictly greater than the target. The array wraps around (is circular).

## Approach: Binary Search with Modulo

Use standard binary search to find the insertion point. Since the array wraps around, return `letters[l % len(letters)]` where `l` is the final left pointer position.

**Complexity:**
- Time: O(log n)
- Space: O(1)
