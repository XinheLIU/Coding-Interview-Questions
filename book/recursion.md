---
chapter: recursion
---

# Recursion & Divide and Conquer

Last updated: 2026-08-10

Recursion is the foundation of algorithmic thinking, and divide and conquer is the
first thing you build with it. The chapter is small on purpose: only a handful of
problems here are *about* the technique. Everything after it — sorting, search,
dynamic programming — is an application.

<ChapterChildren parent="recursion" />

## Recursion: three questions, in order

1. **What is the base case?** The smallest input you can answer without recursing.
   Get this wrong and you get infinite recursion or an off-by-one at the boundary.
2. **How does the input shrink?** Every recursive call must move strictly toward
   the base case. If you cannot name the measure that decreases, the function does
   not terminate.
3. **What do you do with the sub-answer?** This is the actual algorithm; the rest
   is bookkeeping.

The hard part is psychological, not technical: you must **stop tracing the stack**.
Assume the recursive call returns the right answer for a smaller input and write the
one step you are responsible for. Trying to hold four frames in your head at once
is how recursive code gets written wrong.

## Divide and conquer is not just recursion

The name has three parts and all three matter:

| step | question |
|---|---|
| **divide** | how do I split the input? |
| **conquer** | recurse on the pieces |
| **combine** | how do I merge the sub-answers? |

The **combine** step is what separates divide and conquer from plain recursion, and
it is where the cost lives:

- **Merge sort** splits in half for free, then pays `O(n)` to merge → `O(n log n)`.
- **Quicksort** pays `O(n)` to partition, then merges for free → `O(n log n)`
  expected, `O(n²)` when the pivot is adversarial.

Same recursion tree, cost moved from one end to the other. Notice that
**binary search is *not* divide and conquer** — it discards one half rather than
solving both and combining. One subproblem, no combine step. That distinction is
why binary search lives in the next chapter.

## The recursion tree tells you the complexity

Sum the work per level, multiply by the number of levels:

```
T(n) = 2T(n/2) + O(n)     →  log n levels × O(n) per level  =  O(n log n)   # merge sort
T(n) =  T(n/2) + O(1)     →  log n levels × O(1) per level  =  O(log n)     # binary search
T(n) = 2T(n/2) + O(1)     →  n leaves, constant work each   =  O(n)         # tree size
```

If you can write the recurrence, you have the complexity — no memorized master
theorem required.

## Partition: the move worth knowing cold

Quickselect (#215 Kth Largest, #973 K Closest Points) reuses quicksort's partition
but recurses into **only the side containing the answer**. That drops the expected
cost from `O(n log n)` to `O(n)`:

```python
pos = partition(a, l, r)
if pos == k:  return a[pos]        # found it
if pos <  k:  recurse(pos + 1, r)  # answer is on the right
else:         recurse(l, pos - 1)  # answer is on the left
```

Only one branch is taken, so the work per level halves instead of staying flat —
`n + n/2 + n/4 + … = 2n`. This is the same "discard, don't combine" idea as binary
search, applied to an unsorted array.

## When recursion is the wrong choice

- **Overlapping subproblems** → you are recomputing. Memoize, or invert into a
  bottom-up table. That is the whole content of the Dynamic Programming chapter.
- **Deep, thin recursion** (a linked list, a degenerate tree) → Python's default
  limit is 1000 frames. Convert to iteration with an explicit stack.
- **Tail-recursive shapes** → Python does not optimize them. A `while` loop is
  clearer and cheaper.

<ChapterIndex chapter="recursion" />
