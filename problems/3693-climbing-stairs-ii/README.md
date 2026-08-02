---
id: 3693
title: Climbing Stairs II
slug: climbing-stairs-ii
difficulty: Medium
topics: [dynamic-programming]
leetcode: https://leetcode.com/problems/climbing-stairs-ii/
relations: [{"type": "builds-on", "target": 509, "reason": "Extends Fibonacci/Climbing Stairs to 3-step choices with weighted costs — same rolling-variable optimization."}, {"type": "builds-on", "target": 70, "reason": "Generalizes Climbing Stairs by adding cost constraints and 3-step option instead of just 1/2 steps."}]
---

# 3693. Climbing Stairs II

Last updated: 2026-08-02

## Why this problem matters

The first **constrained extension** of Climbing Stairs/Fibonacci. It shows that the same DP recurrence structure can handle richer state transitions — here, three step choices (1, 2, or 3) with weighted costs (1x, 4x, 9x respectively). The recurrence still looks back a fixed number of states, so space optimization still collapses to rolling variables.

## The key insight

**The recurrence depth determines space complexity.** Fibonacci looks back 2 states, so you need 2 variables. This problem looks back 3 states (you can arrive from i-1, i-2, or i-3), so you need 3 rolling variables. The cost multipliers (1, 4, 9) are just weights in the transition — they don't change the DP structure.

## The extensibility

- **Different step rules**: What if you can take 1, 2, 3, or 4 steps? Add a fourth rolling variable and adjust the transition.
- **Different cost functions**: What if the cost is exponential, or depends on the step size differently? Same DP structure, different arithmetic in the transition.
- **Bounded steps**: What if you can take at most K steps total, or at most M consecutive same-size steps? Add another dimension to the state.
- **2D generalization**: What if you're climbing a 2D grid with costs, and can move right/down/diagonally? The transition considers more neighbors, but the structure is identical.

## Variations to ask

1. What if the cost multipliers are reversed (1-step costs 9x, 3-step costs 1x)? Does the optimal strategy change?
2. What if you must alternate between 1-step and 2-step moves (no two consecutive same-size steps)?
3. What if each step has a different cost array `costs[i][s]` where `s` is the step size?
4. What if you can skip at most K steps (teleport) for free?

## Relationship to the DP learning path

- **Fibonacci (#509)** teaches the basic 2-state recurrence and space optimization
- **Climbing Stairs (#70)** is equivalent to Fibonacci (counting paths = F(n+1))
- **This problem** extends to 3 states with weighted transitions
- **Min Cost Climbing Stairs (#746)** is a simpler version with only 1/2 steps and per-step costs
- **Triangle (#120)** moves the recurrence to 2D (each cell depends on two neighbors below)

*Time* `O(n)`, *space* `O(1)` (rolling three variables).

<<< @/problems/3693-climbing-stairs-ii/solution.py
