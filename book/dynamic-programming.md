---
chapter: dynamic-programming
---

# Dynamic Programming

Last updated: 2026-08-10

DP turns an exponential search into a polynomial table fill. The recurring job is
to name a **state**, write the **transition** between states, and pin down the
**base cases** and **answer cell**. Everything below embeds the real solution
files — edit a `.py` and this page updates.

<ChapterChildren parent="dynamic-programming" />

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

## The learning path: recursion depth → dimensionality

This chapter builds from 1D recurrence to 2D grids, then from simple aggregation (sum) to non-monotonic operations (product), showing how the same DP structure adapts:

1. **Fibonacci (#509)** — the minimal example of overlapping subproblems and space optimization
2. **Climbing Stairs II (#3693)** — extends to 3-step choices with weighted costs, same rolling-variable pattern
3. **Maximum Subarray (#53)** — introduces "max ending at i" state definition for subarrays
4. **Maximum Product Subarray (#152)** — non-monotonic operation requires tracking both extremes
5. **Triangle (#120)** — moves to 2D recurrence, bridge between linear and grid DP
6. **Longest Common Subsequence (#1143)** — full 2D grid with match/mismatch transitions

## Fibonacci Number ([#509](https://leetcode.com/problems/fibonacci-number/))

The smallest possible example of the whole idea: memoize repeated states instead
of recomputing them, and the memo table collapses into a recurrence relation.

Plain recursion `fib(n) = fib(n-1) + fib(n-2)` recomputes `fib(n-2)` once for
every call one level up, so the call tree doubles in size for each unit of `n` —
`O(2^n)`. Nothing about the *values* changed between calls; only the recursion
forgot it had already seen that state.

**State.** `dp[i]` = the `i`-th Fibonacci number.

**Transition.** `dp[i] = dp[i-1] + dp[i-2]`, i.e. cache each state once and reuse
it instead of re-deriving it.

**The optimization worth knowing.** The transition only ever looks two states
back, so the full table is unnecessary — two rolling variables are enough. This
is the same collapse the Minimum Path Sum section below does from a 2-D grid
down to a 1-D row: the space you need is bounded by how far back the transition
reaches, not by how many states you've computed.

*Time* `O(n)`, *space* `O(1)` rolled (`O(n)` with a full memo table).

<<< @/problems/509-fibonacci-number/solution.py

## Climbing Stairs II ([#3693](https://leetcode.com/problems/climbing-stairs-ii/))

Extends Fibonacci to 3-step choices (1, 2, or 3 steps) with weighted costs (1x, 4x, 9x). Shows that when the recurrence looks back k states, you need k rolling variables — the space optimization scales with transition depth.

**State.** `dp[i]` = minimum cost to reach step `i`.

**Transition.** `dp[i] = min(dp[i-1] + cost*1, dp[i-2] + cost*4, dp[i-3] + cost*9) + costs[i]`, choosing the cheapest of three possible previous positions.

**Space optimization.** Three rolling variables `(x, y, z)` represent `(i-3, i-2, i-1)`.

*Time* `O(n)`, *space* `O(1)`.

<<< @/problems/3693-climbing-stairs-ii/solution.py

## Maximum Subarray ([#53](https://leetcode.com/problems/maximum-subarray/)) — The 1D DP entry point

This is the problem that makes the jump from "brute force" to "DP" feel earned rather than magical. Wu Jun's *The Beauty of Algorithms* uses it in Chapter 1 to teach Big O through lived algorithmic improvement: O(n³) → O(n²) → O(n log n) → O(n).

**The state definition that unlocks everything.** Define `dp[i]` = maximum sum of any subarray **ending at** position `i` (not "up to" `i`). This framing makes the transition obvious: either extend the previous subarray if it helps (`dp[i-1] + nums[i]`), or start fresh from the current element (`nums[i]`).

```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

**Why "ending at i" works.** Because every subarray ends somewhere, scanning all `dp[i]` covers all possible subarrays. The global answer is `max(dp)`, not `dp[n-1]`.

**Kadane's algorithm** is this recurrence with space collapsed to O(1): since `dp[i]` only looks one step back, two rolling variables suffice.

**Why this problem is exceptionally extensible:**

- **Return boundaries, not just the sum** — track `temp_start` and update `[left, right]` when the global max updates (still O(n), one pass)
- **Product instead of sum** (#152) — same structure, but track both max and min because negatives flip signs
- **Circular array** (#918) — either the max subarray doesn't wrap (standard Kadane), or it wraps (= `total_sum - min_subarray`)
- **Stock trading via difference arrays** — transform prices to daily differences, then run Kadane (#121, #122, #309, #714)
- **2D generalization** — fix top/bottom rows, compress columns into a 1D array, run Kadane on each compression (O(m² n) for maximum sum rectangle)
- **Divide and conquer follow-up** — split at mid; max subarray is entirely left, entirely right, or crosses mid (O(n log n), asked explicitly in the problem)

*Time* `O(n)`, *space* `O(1)` with rolling variables.

<<< @/problems/53-maximum-subarray/solution.py

**Variant with explicit tracking.** The version above reuses the input array for in-place DP. For clarity or when tracking boundaries, use separate variables:

<<< @/problems/53-maximum-subarray/solution.v2.py

## Maximum Product Subarray ([#152](https://leetcode.com/problems/maximum-product-subarray/))

The twist on Maximum Subarray. Shows that when the operation isn't monotonic (negatives flip signs), you must track **both extremes** — today's minimum might become tomorrow's maximum when multiplied by another negative.

**State.** `dp_max[i]` = max product ending at `i`, `dp_min[i]` = min product ending at `i`.

**Transition.** Consider three choices at each position: start fresh from `nums[i]`, extend max, or extend min (because a negative `nums[i]` makes the min become the max):

```
dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
```

**Why dual tracking is necessary.** Multiplication flips signs — `(-10) * (-5) = 50`. The same negative that ruins today's max might create tomorrow's max.

*Time* `O(n)`, *space* `O(1)` (rolling array).

<<< @/problems/152-maximum-product-subarray/solution.py

## Triangle ([#120](https://leetcode.com/problems/triangle/))

The first **2D recurrence** in the progression. Fibonacci is 1D (`dp[i]` depends on `dp[i-1]` and `dp[i-2]`). Triangle is 2D (`dp[i][j]` depends on `dp[i+1][j]` and `dp[i+1][j+1]`), but the transition is still local — each cell picks the minimum of two neighbors below.

**State.** `dp[i][j]` = minimum path sum from position `(i, j)` to the bottom.

**Transition.** Each cell can only reach the two cells directly below it:
`dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]`.

**Why bottom-up.** Starting from the bottom row, each cell has exactly 2 reachable neighbors below it. Top-down would mean multiple paths converging at each cell.

**Space optimization.** Each row depends only on the row below, so the 2D table collapses to a 1D array of length `n`.

*Time* `O(n²)`, *space* `O(n)` → `O(1)` if in-place.

<<< @/problems/120-triangle/solution.py

See also: `problems/120-triangle/solution.v2.py` — in-place DP modifying the input triangle.

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


<ChapterIndex chapter="dynamic-programming" />
