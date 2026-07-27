---
chapter: dynamic-programming
---

# Dynamic Programming

Last updated: 2026-07-26

DP turns an exponential search into a polynomial table fill. The recurring job is
to name a **state**, write the **transition** between states, and pin down the
**base cases** and **answer cell**. Everything below embeds the real solution
files — edit a `.py` and this page updates.

## Why this chapter comes late

DP is memoized recursion with the recursion removed. You need the
[recursion chapter](/book/recursion) to see the subproblem structure, and you need
to have felt an exponential search actually blow up — which is what
[backtracking](/book/search-and-sort) gives you — before "pay for each subproblem
once" lands as a relief rather than a rule.

The tell for DP is **overlapping subproblems**: the recursion tree visits the same
state more than once. If subproblems are disjoint, you have divide and conquer; if
a locally best choice is provably safe, you have a greedy. Only when neither holds
do you need the table.

## Naming the state is the whole job

Everything else is mechanical. Get the state wrong and no amount of debugging
saves the transition. Two questions:

1. **What does `dp[i]` mean, in one sentence, including whether `i` is a length or
   an index?** Off-by-one bugs are almost always an unclear answer here.
2. **How many dimensions does the constraint force?** One per independent thing you
   must remember. #123 Buy/Sell Stock III needs a transaction count; #474 Ones and
   Zeroes needs two capacities.

A `+1` padding row that encodes "the empty input" removes every boundary special
case from the inner loop. That is why the LCS grid below is `(n+1) × (m+1)`.

## Longest Common Subsequence ([#1143](https://leetcode.com/problems/longest-common-subsequence/))

**State.** `dp[i][j]` = length of the LCS of `text1[:i]` and `text2[:j]`.

**Transition.** If the last characters match, they must both belong to the LCS, so
we extend the diagonal: `dp[i][j] = dp[i-1][j-1] + 1`. Otherwise we drop one
character from either string and take the better of the two: `max(dp[i][j-1],
dp[i-1][j])`.

**Why the `+1` grid.** Padding row/column `0` with zeros encodes "one string is
empty → LCS is 0", which removes all boundary special-casing from the inner loop.

*Time* `O(nm)`, *space* `O(nm)`.

<<< @/problems/1143-longest-common-subsequence/solution.py

## Minimum Path Sum ([#64](https://leetcode.com/problems/minimum-path-sum/))

**State.** `dp[i][j]` = cheapest cost to reach cell `(i, j)` from the top-left,
moving only right or down.

**Transition.** A cell is reachable only from above or from the left, so
`dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`. The first row and column are
seeded as prefix sums because they have a single predecessor.

**The optimization worth knowing.** Each cell depends only on the row above and the
cell to the left, so the table collapses to a single 1-D array — `O(n)` space. That
rolled version is kept as a comment at the bottom of the file below.

*Time* `O(mn)`, *space* `O(mn)` → `O(n)` rolled.

<<< @/problems/64-minimum-path-sum/solution.py


<ChapterGraph chapter="dynamic-programming" />

<ChapterIndex chapter="dynamic-programming" />
