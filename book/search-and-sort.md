---
chapter: search-and-sort
---

# Search & Sort

Last updated: 2026-08-10

Two ideas that look unrelated and are not: **sorting establishes an order you can
exploit**, and **searching exploits an order you already have**. Once you see that
binary search only needs a monotonic predicate — not a sorted array — half the
"hard" problems in this chapter become routine.

This chapter also covers systematic exploration: DFS, BFS, and backtracking. They
belong here because they are search too, over a graph instead of an interval.

<ChapterChildren parent="search-and-sort" />

> Deep dives on the individual templates live in
> [DFS](/book/dfs), [BFS](/book/bfs), and [Binary Search](/book/binary-search).

## Sorting: what to actually remember

You will rarely implement a sort. You will constantly *decide* things about one:

- **`O(n log n)` is the comparison lower bound.** Beating it requires assumptions
  about the data — counting sort needs a bounded range, radix needs fixed-width
  keys. If an interviewer wants `O(n)`, they are hinting at one of those.
- **Stability matters when you sort twice.** Sorting by one key then another only
  preserves the first ordering if the second sort is stable. Python's `sorted` is;
  quicksort is not.
- **The sort is often the whole solution.** #56 Merge Intervals, #252 Meeting
  Rooms, #253 Meeting Rooms II, #1196 — each becomes almost trivial once sorted by
  the right key. Choosing the key *is* the insight.
- **Custom keys beat comparators.** `key=lambda x: (x[0], -x[1])` in #354 Russian
  Doll Envelopes is what reduces a 2-D problem to a 1-D LIS.

## Binary search: the invariant, not the template

The reason binary search is error-prone is that people memorize the loop instead of
the invariant. State it explicitly: **the answer is always inside `[lo, hi]`**.
Every branch must preserve that, and the loop must strictly shrink the range.

The generalization worth internalizing: binary search does not need a sorted array,
it needs a **monotonic predicate** — some `f(x)` that is false, false, …, true,
true. You are searching for the boundary.

```python
# Find the smallest x in [lo, hi] with f(x) == True.
while lo < hi:
    mid = (lo + hi) // 2      # biased low; pairs with hi = mid
    if f(mid): hi = mid       # mid might be the answer — keep it
    else:      lo = mid + 1   # mid is definitely not — discard it
return lo
```

That shape solves problems with no array in sight, because the search space is the
*answer*, not the input:

- **#875 Koko Eating Bananas** — `f(speed) = "can finish in h hours"`. Monotonic in
  speed, so binary search the speed.
- **#774 Minimize Max Distance to Gas Station** — binary search the distance.
- **#719 K-th Smallest Pair Distance** — binary search the distance, count pairs
  below it.

When a problem asks to *minimize a maximum* (or maximize a minimum), reach for this
before anything else.

**The rotated-array family** (#33, #153, #154, #162) is the other half of the
skill: the array is not sorted, but at every midpoint you can still determine which
half *is*, which is enough to discard the other. Duplicates break that determination,
which is exactly why #154 is harder than #153.

## DFS vs BFS: pick by what the question asks

Both visit every reachable node once; the difference is order, and order determines
what each one is good for.

| | DFS | BFS |
|---|---|---|
| structure | stack / recursion | queue |
| finds | *a* path | the **shortest** path |
| memory | `O(h)` — path length | `O(w)` — level width |
| natural for | exhausting possibilities, connectivity | shortest hops, level-by-level |

- **"Shortest / fewest / minimum steps" in an unweighted graph → BFS.** Nothing
  else gives it for free. #127 Word Ladder, #433 Minimum Genetic Mutation, and
  #1306 Jump Game III are the same BFS over different neighbour functions.
- **"All / count / does one exist" → DFS.** #200 Number of Islands, #547 Number of
  Provinces, and #323 all count connected components; only the adjacency
  representation changes.

**Mark visited when you enqueue, not when you dequeue.** Otherwise a node with
several in-edges gets queued several times, and the queue blows up.

## Backtracking = DFS with an undo

Backtracking is DFS over a *decision tree* you never materialize. The skeleton
never changes:

```python
def backtrack(path, choices):
    if is_solution(path):
        results.append(path[:])      # copy — path keeps mutating
        return
    for choice in choices:
        path.append(choice)          # choose
        backtrack(path, remaining)   # explore
        path.pop()                   # un-choose  ← this is the "back" in backtracking
```

Two details account for most of the bugs:

1. **Copy on collect.** `results.append(path)` stores a reference to a list that
   you are about to mutate. Every result ends up identical (and wrong).
2. **De-duplicating with duplicate inputs.** Sort first, then skip an element equal
   to its predecessor *at the same depth*. This one line is the entire difference
   between #46/#47 Permutations, #78/#90 Subsets, and #39/#40 Combination Sum.

Pruning is what makes backtracking viable: return early the moment the partial
solution cannot succeed. #51 N-Queens tracking `x+y` and `x-y` diagonals is the
canonical example — the conflict check is `O(1)` instead of a board scan.

<ChapterIndex chapter="search-and-sort" />
