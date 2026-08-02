---
id: 53
title: Maximum Subarray
slug: maximum-subarray
difficulty: Medium
topics: [array, dynamic-programming, greedy]
leetcode: https://leetcode.com/problems/maximum-subarray/
relations: [{"type": "builds-on", "target": 509, "reason": "Applies the 1D DP recurrence pattern to subarrays — dp[i] depends only on dp[i-1]."}]
---

# 53. Maximum Subarray

Last updated: 2026-08-02

## Why this problem matters

The first "subarray DP" problem. It teaches you that `dp[i]` can mean "best solution **ending at** position i" rather than "best solution **up to** position i." This framing makes the transition local and the answer a scan over all `dp[i]`.

## The key insight

**State definition matters more than the algorithm.** Define `dp[i] = maximum sum of any subarray ending at index i`. The transition becomes trivial: either extend the previous subarray (`dp[i-1] + nums[i]`) or start fresh from `nums[i]`.

## The extensibility

This problem is exceptionally extensible — it's a ladder from brute force to optimal algorithms, a bridge to multiple problem families, and a 2D generalization template. Wu Jun's *The Beauty of Algorithms* uses it in Chapter 1 to teach Big O notation through lived algorithmic improvement.

### One-dimensional extensions

#### 1. From maximum value to interval boundaries

The basic LeetCode 53 returns only the maximum sum. The interview follow-up asks for the actual `[left, right]` indices of the optimal subarray.

**Key insight:** Kadane's algorithm naturally tracks where the current subarray starts. When `cur_sum` becomes negative and we "restart" from the next element, that next element becomes the new tentative start. When we update the global maximum, we lock in the current boundaries.

```python
def maxSubArrayWithIndices(nums):
    max_sum = cur_sum = nums[0]
    max_left = max_right = 0
    temp_start = 0  # Tentative start of current subarray
    
    for i in range(1, len(nums)):
        if cur_sum < 0:
            cur_sum = nums[i]
            temp_start = i  # Restart from here
        else:
            cur_sum += nums[i]
        
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_left = temp_start
            max_right = i
    
    return max_sum, max_left, max_right
```

**Time:** still `O(n)` with one forward pass. No reverse scan needed.

#### 2. The algorithmic complexity ladder

This problem demonstrates the full spectrum from brute force to optimal:

- **O(n³)** — Triple loop: try every `[i, j]` pair, sum from scratch each time
- **O(n²)** — Prefix sum optimization: precompute cumulative sums, then `sum[i:j] = prefix[j] - prefix[i-1]` in `O(1)`
- **O(n log n)** — Divide and conquer: split at mid, max subarray is either entirely in left half, entirely in right half, or crosses mid (requires linear scan for the crossing case)
- **O(n)** — Kadane's algorithm: the DP recurrence `dp[i] = max(nums[i], dp[i-1] + nums[i])`

The jump from `O(n²)` to `O(n)` is the insight that you don't need to consider all intervals — only those that are locally optimal.

### Related problem families

#### 3. Stock trading via difference arrays

Transform prices into daily differences: `diff[i] = prices[i+1] - prices[i]`. Maximum profit from one buy-sell = maximum subarray sum of `diff`.

- **[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)** — One transaction: run Kadane on the difference array
- **[122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)** — Unlimited transactions: greedily sum all positive differences
- **[309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)** — State machine DP with cooldown constraint
- **[714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)** — Greedy with fee adjustment

#### 4. DP variants

- **[152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)** — Track both `max_prod` and `min_prod` because a negative times a negative flips to positive
- **[918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)** — Either the max subarray doesn't wrap (standard Kadane), or it wraps (= `total_sum - min_subarray`)
- **[1749. Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/)** — Run Kadane twice: once for max sum, once for min sum (flip signs or track min explicitly)

#### 5. Existence queries instead of max

Given a target sum `k`, find whether any subarray sums to exactly `k`. This shifts from optimization to decision: use a hash set of prefix sums and check if `prefix[i] - k` was seen before.

### Two-dimensional generalization

#### 6. Maximum sum rectangle in a matrix

**Problem:** Given an `m × n` matrix, find the rectangle with the largest sum.

**Solution:** Fix top and bottom rows, compress all rows between them into a 1D array (each column becomes one value = sum of that column from top to bottom), then run Kadane on the compressed array. Repeat for all `O(m²)` pairs of rows.

```python
def maxSumRectangle(matrix):
    m, n = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    for top in range(m):
        col_sums = [0] * n  # Compressed 1D array
        for bottom in range(top, m):
            # Add the current row to col_sums
            for col in range(n):
                col_sums[col] += matrix[bottom][col]
            
            # Run Kadane on col_sums
            max_sum = max(max_sum, kadane(col_sums))
    
    return max_sum
```

**Time:** `O(m² n)`. For a square matrix, that's `O(n³)`.

### Algorithmic thinking extensions

#### 7. Kadane as the DP entry point

The recurrence `dp[i] = max(nums[i], dp[i-1] + nums[i])` is one of the simplest DP transitions. It teaches:

- **State definition:** `dp[i]` = best solution *ending at* position `i` (not *up to* `i`)
- **Local optimality:** At each step, decide whether to extend or restart
- **Global answer:** The answer is `max(dp)`, not `dp[n-1]`

Once this clicks, problems like [198. House Robber](https://leetcode.com/problems/house-robber/), [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), and [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) become pattern recognition.

#### 8. Divide and conquer as a follow-up

LeetCode 53's follow-up explicitly asks: *Try coding another solution using the divide and conquer approach.*

**Idea:** Split the array at mid. The max subarray is one of:
1. Entirely in `nums[:mid]` (recurse left)
2. Entirely in `nums[mid:]` (recurse right)
3. Crosses `mid` (find max suffix of left + max prefix of right)

The crossing case requires a linear scan, so recurrence is `T(n) = 2T(n/2) + O(n) → O(n log n)`.

This is slower than Kadane but demonstrates the divide-and-conquer pattern — useful for problems like [215. Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/) (quickselect) and merge sort.

## Interview variations to ask

1. Return the actual `[left, right]` interval, not just the sum. (*Practice boundary tracking.*)
2. What if the array wraps (circular)? (*Test understanding of total_sum - min_subarray.*)
3. What if we want maximum **product** instead of sum? (*Forces tracking both max and min.*)
4. Find all subarrays with sum ≥ k. (*Shifts from max to counting/filtering.*)
5. What's the O(n log n) divide-and-conquer solution? (*Tests recursion and merge logic.*)
6. Extend to 2D: maximum sum rectangle. (*Tests compression and nested iteration.*)
7. Given a target sum, find if any subarray equals it. (*Prefix sum + hash set.*)
8. At most K non-overlapping subarrays with maximum total sum. (*DP on DP: state becomes [position, k_remaining].*)

## Why Wu Jun chose this problem for Chapter 1

It's pedagogically perfect:
- **Concrete and visual** — anyone can brute-force it, so the optimizations feel earned, not magical
- **Clear complexity ladder** — the jump from O(n²) to O(n) is visceral
- **Transferable insight** — once you see "only track locally optimal suffixes," dozens of other problems unlock
- **Interview ubiquity** — shows up in stock trading, sliding window, DP fundamentals, and 2D generalization

## Solution variants

This problem has two implementations showing different styles of the same Kadane's algorithm:
- `solution.py` (below) — In-place DP reusing the input array
- `solution.v2.py` — Explicit tracking with separate variables

*Time* `O(n)`, *space* `O(1)`.

<<< @/problems/53-maximum-subarray/solution.py
