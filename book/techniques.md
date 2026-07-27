---
chapter: techniques
---

# Techniques

Last updated: 2026-07-26

Sharp tools that assume the fundamentals. Nothing here is a new way of thinking the
way trees or DP are — these are specific instruments you reach for once you
recognize the shape of the problem. That recognition is the only thing worth
practising.

## Bit manipulation

Bits are useful in exactly three situations. Outside them, bit tricks are a
readability tax.

**1. XOR cancels pairs.** `x ^ x == 0` and `x ^ 0 == x`, so XOR-ing a whole array
leaves only the element that appears an odd number of times. That is the entire
solution to #136 Single Number, and the same self-cancelling property solves #268
Missing Number by XOR-ing indices against values.

**2. `n & (n - 1)` clears the lowest set bit.** Everything follows from this:

```python
n & (n - 1) == 0    # n is a power of two (#231) — only one bit was set
while n: n &= n-1; c += 1   # popcount (#191) — one iteration per set bit, not per bit
n & (-n)            # isolate the lowest set bit — the Binary Indexed Tree step (#307)
```

**3. A bitmask is a set.** When the universe is small (≤ ~20 elements), an integer
*is* a subset: bit `i` set means element `i` is present. Union is `|`, intersection
`&`, membership `mask >> i & 1`. This turns "iterate all subsets" into
`for mask in range(1 << n)` and is what makes subset-DP tractable.

## Greedy

Greedy is the most dangerous technique in the book, because a wrong greedy passes
the examples and fails the hidden tests. The bar for using one is an
**exchange argument**: show that any optimal solution can be transformed, step by
step, into the greedy one without getting worse.

If you cannot articulate that argument, you do not have a greedy algorithm — you
have a guess. Use DP instead.

Where greedy provably works:

- **#55 Jump Game** — track the farthest reachable index. Taking the maximum reach
  at every step never rules out a solution, because reach is monotone.
- **#122 Buy and Sell Stock II** — with unlimited transactions, every positive delta
  is independently capturable. Note that #121 (one transaction) and #123 (two) are
  *not* greedy: the constraint couples the choices, so they need DP.
- **#455 Assign Cookies**, **#860 Lemonade Change** — sort, then match the smallest
  sufficient resource. Classic exchange argument.

The contrast between #122 and #123 is the lesson: **a constraint that couples
decisions kills greedy.**

## Math

Most "math" problems are one observation plus a loop. The observation is the
problem.

- **Digit manipulation** — `divmod(n, 10)` peels the last digit; used in #202 Happy
  Number, #263 Ugly Number.
- **Modular arithmetic for grouping** — #1010 Pairs of Songs Divisible by 60 works
  because `(a + b) % 60 == 0` means `b % 60 == (60 - a % 60) % 60`. Count
  remainders, don't compare pairs.
- **Overflow and negative division.** Python's `//` floors toward negative infinity,
  which is *not* what C-family truncation does. #227 Basic Calculator II and #29
  need the explicit correction — a real source of wrong answers.
- **Closed forms beat loops** when they exist: #441 Arranging Coins is the quadratic
  formula, though a binary search on the answer is easier to get right.

## Data structure design

Design problems ask a different question from algorithm problems: *given required
time bounds on several operations, what combination of structures achieves all of
them at once?* No single structure ever does — the answer is always a **pairing**,
where each half covers the other's weakness.

| problem | pairing | why |
|---|---|---|
| **#146 LRU Cache** | hash map + doubly linked list | map gives `O(1)` lookup; list gives `O(1)` reorder and evict |
| **#155 Min Stack** | stack + min-stack | auxiliary stack remembers the minimum *as of* each depth |
| **#380 Insert/Delete/GetRandom** | hash map + dynamic array | array gives `O(1)` random index; map gives `O(1)` locate; delete swaps with the last slot |
| **#295 Median from Stream** | max-heap + min-heap | two halves, each with its boundary element on top |

The recurring move in the last two rows is worth naming: **swap-with-last** turns
an `O(n)` array deletion into `O(1)` when order does not matter, and **two
structures facing each other** exposes a boundary element in `O(1)`.

Before writing code, state the required complexity of *every* operation. The bound
you overlook is the one the design fails on.

<ChapterGraph chapter="techniques" />

<ChapterIndex chapter="techniques" />
