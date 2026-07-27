---
id: 121
title: Best Time To Buy And Sell Stock
slug: best-time-to-buy-and-sell-stock
difficulty:
topics: [dynamic-programming]
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
relations: [{"type": "specializes", "target": 122, "reason": "Unlimited transactions turns the problem into summing every positive price delta."}, {"type": "specializes", "target": 309, "reason": "Adds a cooldown day — the greedy accumulation from II becomes a DP on hold/sold/cooldown states."}, {"type": "specializes", "target": 714, "reason": "Adds a per-transaction fee — same unlimited-transaction structure but subtract fee on each sell."}, {"type": "specializes", "target": 123, "reason": "At-most-2 transactions splits into a forward pass for the first and a backward pass for the second."}]
---

# 121. Best Time To Buy And Sell Stock

> Notes / intuition / complexity — TODO.

<<< @/problems/121-best-time-to-buy-and-sell-stock/solution.cpp
<<< @/problems/121-best-time-to-buy-and-sell-stock/solution.py
