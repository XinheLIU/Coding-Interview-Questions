---
id: 191
title: Number Of 1 Bits
slug: number-of-1-bits
difficulty:
topics: [bitwise]
leetcode: https://leetcode.com/problems/number-of-1-bits/
relations: [{"type": "same-pattern", "target": 231, "reason": "Power of Two is the n & (n-1) == 0 special case of the clear-lowest-set-bit trick used to count bits."}, {"type": "builds-on", "target": 338, "reason": "Counting Bits caches results for every i < n, replacing the per-number loop with dp[i] = dp[i >> 1] + (i & 1)."}]
---

# 191. Number Of 1 Bits

> Notes / intuition / complexity — TODO.

<<< @/problems/191-number-of-1-bits/solution.py
