# Dynamic Programming

DP turns an exponential search into a polynomial table fill. The recurring job is
to name a **state**, write the **transition** between states, and pin down the
**base cases** and **answer cell**. Everything below embeds the real solution
files — edit a `.py` and this page updates.

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
