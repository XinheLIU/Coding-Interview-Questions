# Depth-First Search & Backtracking

Last updated: 2026-08-25

Depth-first search walks a graph/tree all the way down before backing up. **Backtracking is DFS over a tree you build on the fly** — the tree is implicit, branches are *choices*, and leaves are *solutions*. When you "backtrack", you undo the last choice and try the next branch.

## What is backtracking? The three problem shapes

Backtracking solves **choice enumeration** problems — problems where you must explore every way to build something under constraints. Three classic shapes dominate interviews:

### 1. Subsets (78) — record every node

**Problem**: enumerate all subsequences of `[1,2,3]`  
**Answer**: `[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]` — every node in the tree is a valid subset

```
            []                   ← record
       /    |    \
     [1]   [2]   [3]             ← record all
    /  \    |
 [1,2][1,3][2,3]                 ← record all
   |
[1,2,3]                          ← record
```

- **Recording**: at every node before recursing
- **Branches**: for each remaining element, choose "take it" (one branch per element starting from `start`)
- **Base case**: implicit (no more elements to consider)
- **Key constraint**: `start` index prevents `[1,2]` vs `[2,1]` duplicates by enforcing "only consider elements ≥ last chosen"

### 2. Combinations (77) — fixed-size subsets

**Problem**: choose exactly `k=2` from `[1,2,3,4]`  
**Answer**: `[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]` — only leaves at depth k

```
              ∅
        /   |   |   \
       1    2   3   4
      /|\   |\   |
     2 3 4  3 4  4
    [1,2][1,3][1,4][2,3][2,4][3,4]  ← only depth-k nodes recorded
```

- **Recording**: only at leaves where `len(out) == k`
- **Branches**: same as subsets (elements from `start` onward)
- **Base case**: `len(out) == k`
- **vs Subsets**: added a size constraint; changed when to record

### 3. Permutations (46) — order matters, exhaust all elements

**Problem**: arrange `[1,2,3]` in all orders  
**Answer**: `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]` — n! leaves

```
              [1,2,3]
        /       |       \
       1        2        3          choose one
      / \      / \      / \
     2   3    1   3    1   2        choose from remaining
     |   |    |   |    |   |
     3   2    3   1    2   1        last one standing
   [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
```

- **Recording**: at leaves when candidate pool exhausted
- **Branches**: *all* remaining elements (no `start` index — order matters, so `[1,2]` ≠ `[2,1]`)
- **Base case**: `len(out) == n` or `nums` is empty
- **vs Combinations**: no `start` index; each level revisits the whole pool minus what was already chosen

### The visual difference

```
Subsets:        →  "take or skip" each element, record everywhere
Combinations:   →  "take or skip" until size k, record only at depth k
Permutations:   →  "arrange" all elements, record when all used
```

| Shape | Recording rule | Loop range | Output count |
|-------|---------------|------------|--------------|
| **Subsets** | every node | `start..n` | 2ⁿ |
| **Combinations** | only `len==k` | `start..n` | C(n,k) = n!/(k!(n-k)!) |
| **Permutations** | only `len==n` | all unused | n! |

All three use the same six-line template; only `is_solution`, `choices`, and `is_valid` change.

This page answers the three questions that linger after you've solved your first few backtracking problems:

1. Why does the code look different every time — is there one template?
2. Why do some solutions pass state as parameters and others use a closure / return values — which is faster?
3. What actually counts as the "hard" part of backtracking?

## The one template (it is one)

Forget the surface differences. Every backtracking solution is the same skeleton:

```py
def backtrack(state):
    if is_solution(state):        # 1. base case — stop, record
        record(state)
        return
    for choice in choices(state): # 2. try each option at this level
        if not is_valid(choice):  # 3. prune (optional, and where the difficulty lives)
            continue
        make(choice)              # 4. commit
        backtrack(state)          # 5. recurse
        undo(choice)              # 6. undo (so the next sibling sees a clean state)
```

Three of those six lines are the same in every problem. **The only lines that change — and the entire point of the problem — are 1, 2, and 3.** Your brain should be trained to fill in those three blanks per problem and treat the rest as boilerplate:

| line | what you decide per problem |
|------|------------------------------|
| `is_solution(state)` | when is a path complete? (17: length == n; 39/40: sum == target; sudoku: all cells filled) |
| `choices(state)` | what are the branches? (17: letters of this digit; 39/40: numbers at/after `start`) |
| `is_valid(choice)` | what makes a branch dead? (39/40: sum would exceed target; sudoku: digit breaks row/col/box; 40 adds: duplicate value) |
| `make` / `undo` | what "advance" and "retreat" mean (typically append/pop a list, or pass a new string and skip undo) |

So the question is never "write backtracking from scratch" — it is "what are the base case, the choices, and the prune for *this* problem". Everything else is a fixed form.

## Question 1: why is the code style never the same?

Because state can be carried three ways, and authors mix them freely. All three are the *same* algorithm:

```py
# (a) State threaded through as parameters — the explicit, testable form.
def dfs(digits, level, out, res):
    if len(out) == len(digits):
        res.append(out)
        return
    for c in MAP[digits[level]]:
        dfs(digits, level + 1, out + c, res)   # out+c makes a NEW string, no undo needed

# (b) Closure over the constants — only what *changes* is a parameter.
def letterCombinations(self, digits):
    def dfs(level, out):                        # MAP, res live in the enclosing scope
        if len(out) == len(digits):
            res.append(out); return
        for c in MAP[digits[level]]:
            dfs(level + 1, out + c)
    res = []
    dfs(0, "")
    return res

# (c) Return-value style — leaf emits a list; parent collects children's lists.
def dfs(level):
    if level == len(digits):
        return [""]                             # a leaf contributes one empty-string prefix
    return [c + suffix
            for c in MAP[digits[level]]
            for suffix in dfs(level + 1)]
```

There is no "right" one; each is a legitimate solution you'll see in the wild. Pick one and stay consistent in an interview. (A) is the most explicit and debuggable; (B) is the shortest; (C) is "functional" and rarely worth it for more than two levels.

### A fourth style exists for grid problems: return-a-boolean, in-place

Sudoku (`solution.py`) looks *nothing* like 17/39/40 — no explicit result list, `board` mutated in place, `return True/False`. That is a different *shape* of problem:

- 17/39/40 are **enumerate-everything** — the answer is a set of solutions, you collect them all.
- Sudoku is **find-one-solution** — the answer is a `True/False` you propagate up; the first success short-circuits.

That single difference changes the whole skeleton. "Find one" → recurse returns bool, unwind on `True`, don't enumerate. "Enumerate all" → recurse returns nothing, never unwind early, append every leaf. Both are backtracking; the *termination contract* differs.

| shape | what the recursion returns | what you propagate |
|-------|---------------------------|--------------------|
| enumerate all (17, 39, 40, permutations, subsets) | nothing (void) | side-effect: append to a shared `res` |
| find one (sudoku, word search) | `bool` | "did anyone below me succeed?" — unwind on `True` |
| count (a few DP-adjacent problems) | `int` | sum of children's counts |

Sudoku's `intersection = row[i] & col[j] & grid[g]` is not a different template — it is just a very good `choices(state)`: instead of trying all 9 digits, try only the digits valid in all three units (branch factor ~1–3, not 9). Then `is_valid` disappears because a choice is *by construction* valid. Prune folded into choice-generation. That is why sudoku reads as foreign — its `choices` is clever, not its skeleton.

### Reading this section backward

When a solution looks "different", do not ask "which template is this". Ask which of **the three per-problem blanks** got filled differently, and which **of the three state-carrying styles** it uses. Sudoku is "find-one" + "choices = set intersection". 17 is "enumerate-all" + "choices = letters". That accounts for ~everything that looks inconsistent.

## Question 2: parameters vs closure vs return value — which is fastest?

The honest answer: **none of this matters for backtracking.** The cost is dominated by the recursion tree (exponentially many nodes), and state-passing is O(1) copies of a reference or a small list per node.

But the *sub-question* inside your question — **`out + i` (immutable) vs `append`/`pop` (mutable)** — is real and worth knowing:

```py
# immutable — allocate a new list/string at EVERY node
dfs(digits, level + 1, out + c)        # O(len(out)) copy per branch, no undo

# mutable — one shared list, append then pop
out.append(candidates[i])
dfs(..., i, out)
out.pop()                              # O(1) amortized; must be paired with an undo
```

| | `out + c` (immutable) | `append` / `pop` (mutable) |
|---|---|---|
| allocation | new object every node → O(len) time + churn | none (reuse one list) |
| correctness | can't corrupt siblings (parent's `out` untouched) | must remember the `pop`, or siblings see stale state |
| readability | very clean, no undo | explicit, shows the backtracking literally |

Realistically the two are within a small constant of each other for interview-sized inputs; the garbage-collector-friendly immutable form can even *win* when `out` is a short list. Choose by clarity, not by micro-optimizing. The one place the mutable form matters: when `out` is large (e.g. building a whole board), copying it at every node is genuinely wasteful — copy only when you record the answer (`res.append(out[:])`), mutate in place between.

**Note** this is the real reason `res.append(out[:])` has a slice everywhere: `out` is mutated as the search proceeds, so you must snapshot it (`[:]`) — appending `out` itself would record a reference whose contents change later, aliasing every answer to the last one.

**The `sum(out)` vs `target - x` decision is the efficiency question that actually matters**, more than state-passing style:

```py
# recompute the sum at every node — O(len) each time you check the base case
if sum(out) == target: ...

# subtract as you go — O(1) check, and the target doubles as the remaining budget
dfs(..., target - candidates[i], ...)   # terminate when target < 0 or == 0
```

`target - x` is both faster and more elegant: the parameter is now "how much do I still need to reach". Prefer it; most editorial solutions do.

**Bottom line for efficiency:** subtract-don't-sum > append/pop ≈ immutable > closure-vs-parameters (irrelevant). Spend your attention on `is_valid` (pruning), not on argument passing — pruning is where exponential blow-up gets tamed, and it is the only thing that moves the needle.

## Question 3: what is actually hard about backtracking

Backtracking's difficulty is not the recursion (you know DFS). It is three specific, learnable things, in order of how often they cause a wrong answer:

### 1. Ordering vs. combinations — the `start` index

The single most common bug: emitting both `[2,3]` and `[3,2]`. Fixing it means understanding *why* `start` enforces a canonical order and passing `start=i` (allow reuse) vs `start=i+1` (forbid reuse). This is the line that distinguishes 39 (`i`) from 40 (`i+1`). Get the `start` semantics wrong and you either double-count or miss answers — no amount of debugging the rest helps.

How to think about it: before coding, ask *"does the order of my choices matter for the answer?"* Permutations → yes (full range each level). Combinations/subsets → no → you need a `start` (or a chosen/un-chosen bitmask) that only ever picks indices ≥ the last one.

### 2. Deduplication (when the input has duplicates)

Two different ideas hide behind "duplicate":

- **40 / 90 / 47** — the *input* contains duplicates, the *answer* must not. Sort first (clusters equal values), then skip a value that equals the previous one **at the same recursion level** — the `if i > start and candidates[i] == candidates[i-1]: continue` line. The subtlety is `i > start`, not `i > 0`: you must skip *sibling* duplicates but still allow the `[1,1,…]` running case.
- **generating the same multiset two ways** — handled by `start` (point 1), not by dedup.

Think of it as: one pass to prevent *same value twice at the same level*, and `start` to prevent *same set in two orders*. They are orthogonal; most hard combination problems need both.

### 3. Encoding constraints cheaply (the prune)

Search cost lives in the branch factor. The better your `is_valid`, the fewer dead branches you visit.

- 39/40: prune on a running sum (and the `target - x` trick) — trims anything that already overshoots.
- Sudoku: don't trial-and-error all 9 digits then `is_valid`-check each; precompute `row`/`col`/`box` sets and iterate `&` of them, so an invalid digit is never even a branch.
- N-Queens: same idea — track occupied columns/diagonals so each level's choices are already legal.

The thinking move: **prune as early as possible, ideally by shrinking the choice set rather than rejecting after the fact.** Reject-after still works and is easier to write; shrink-first is the difference between a solution that times out and one that runs instantly.

### A two-minute mental checklist before coding any backtracking problem

1. Enumerate-all, find-one, or count? → picks the recursion's return contract.
2. Does order matter? → picks `start` semantics (none / `i` / `i+1` / permutation-style full range).
3. Can the input repeat? → decide sort+skip.
4. What kills a branch early? → the prune (often a running sum or a validity set).
5. Mutable or immutable `out`? → `append`/`pop` or `out + x`; either way, `res.append(out[:])` snapshots.

Answer those five and the code writes itself; the six-line template is the scaffolding.

## Time Complexity Analysis

Backtracking complexity has two factors: **tree size** (how many nodes you visit) and **work per node** (what you do at each). Both are shaped by the problem.

### Tree size — the exponential term

| Problem | Tree size | Why |
|---------|-----------|-----|
| **Subsets** | O(2ⁿ) | binary choice per element: take or skip |
| **Combinations(n,k)** | O(C(n,k)) ≈ O(nᵏ/k!) | visit only nodes up to depth k; binomial coefficient |
| **Permutations** | O(n!) | n choices at level 1, n-1 at level 2, …, 1 at level n |
| **Combination Sum** | O(target/min)ⁿ worst | unbounded reuse → depth ≈ target/min_candidate; branch factor ≈ n |
| **Sudoku** | O(9^m) where m=empty cells | 9 digits per cell, but **heavy pruning** (row/col/box) cuts this massively |

The exponent is determined by:
- **Depth**: how many choices in sequence (k for combinations, n for permutations, variable for combination sum)
- **Branch factor**: how many options per level (n for full range, shrinking for permutations, ≤9 for sudoku)

### Work per node — the polynomial term

At each node you:
1. Check termination: O(1) typically
2. Generate choices: O(n) iteration or O(1) if precomputed
3. Make/undo: O(1) for append/pop, O(k) for copying `out[:k]`
4. Record solution: O(k) to copy a k-element subset/combination

| Problem | Per-node cost | Total |
|---------|---------------|-------|
| Subsets | O(n) to copy each subset | **O(2ⁿ · n)** |
| Combinations(n,k) | O(k) to copy | **O(C(n,k) · k)** |
| Permutations | O(n) to slice `nums[:i]+nums[i+1:]` | **O(n! · n)** |
| Letter Combinations | O(1) append char to string | **O(4ⁿ · n)** where n = digit count |

**Why the polynomial factor matters**: When n is small (n ≤ 10, typical in interviews), 2¹⁰ = 1024 and 10! = 3.6M are both instant. The hidden O(n) or O(n²) in poorly-written code (e.g. recomputing `sum(out)` at every node, or copying the whole board) is what makes it timeout. Always check:
- Are you copying O(n) data at every node when you could append/pop O(1)?
- Are you recomputing something (like `sum(out)`) that could be threaded as a parameter?

### Pruning changes everything

The formulas above are **worst-case** (all branches explored). Real problems:
- **Combination Sum with early `sum > target` prune**: cuts the tree from O((target/min)ⁿ) to something far smaller — empirically closer to O(2ⁿ) when candidates are well-distributed.
- **Sudoku with set intersection**: reduces branch factor from 9 to ~1–3 on average, turning O(9⁸¹) (impossible) into O(9²⁰) (instant).
- **Deduplication in Permutations II**: when input is `[1,1,1,1,2]`, the formula says 5! = 120, but actual unique permutations = 5 — pruning 96% of the tree.

**Golden rule**: Exponential base matters more than polynomial factor. Cutting branch factor from 9 to 3 (sudoku) saves more than shaving O(n) per node. Focus pruning effort on reducing branches, not on micro-optimizing per-node work.

### Practical interview heuristic

When asked "what's the time complexity":
1. Count the **tree size**: 2ⁿ / n! / C(n,k) / ...
2. Multiply by **per-node work**: usually O(k) or O(n)
3. If heavy pruning exists, mention it: "O(2ⁿ · n) worst-case, but early termination on `sum > target` cuts the tree significantly in practice"

Space is almost always **O(depth)** = O(n) or O(k) for the call stack, plus O(output) for the result list.

## Pruning in depth — the stop condition

Pruning is not "nice to have" — it's the difference between AC and TLE. But "prune early" has three levels of sophistication, and recognizing which one your problem needs is a learnable skill.

### Level 1: Prune after choosing (reject invalid branches)

The `is_valid(choice)` check inside the loop — try a branch, immediately reject if invalid, continue to the next sibling.

**Combination Sum (39)**:
```python
for i in range(start, len(candidates)):
    if sum(out) + candidates[i] > target:  # ← prune after proposing i
        continue
    dfs(candidates, i, out + [candidates[i]], ...)
```

**Cost**: You still *consider* every candidate (iterate the full range), you just skip the recursive call. For n candidates, that's still O(n) work at this node.

**When it's enough**: When the candidate set is small or the prune is cheap. Most combination/subset problems.

### Level 2: Prune before generating (shrink the choice set)

Instead of generating all choices then rejecting some, compute only the valid choices up front.

**Sudoku (37)** — the `row & col & grid` intersection:
```python
choices = available_row[r] & available_col[c] & available_grid[g]
for digit in choices:       # ← only 1–3 iterations, not 9
    board[r][c] = digit
    # mark digit as used in row/col/grid
    dfs(...)
    # unmark
```

Without this, you'd try all 9 digits and check validity after — 9 recursive calls per empty cell, most invalid. With intersection, you try ~1–3 digits — branch factor drops from 9 to 2–3, saving exponentially.

**Cost**: O(1) set intersection per node (if precomputed), but must maintain the constraint sets (row/col/grid bitmasks or sets) as you make/undo choices.

**When you need it**: When the candidate pool is large (e.g. 9 digits in sudoku, 26 letters in word search) and validity can be precomputed via constraint sets (occupancy masks, availability bitsets).

### Level 3: Sort + early break (order matters)

When the array is **sorted** and the prune condition is **monotonic** (e.g. "sum too large"), you can *break* instead of *continue* — once one candidate fails, all later ones fail too.

**Combination Sum with sorted candidates**:
```python
candidates.sort()  # ← enables early break
for i in range(start, len(candidates)):
    if sum(out) + candidates[i] > target:
        break  # ← all candidates[j] for j > i are even larger; stop the loop entirely
    dfs(candidates, i, out + [candidates[i]], ...)
```

**vs level 1**: `continue` skips this candidate and tries the next; `break` stops the entire loop at this level. On a sorted array where the condition is monotonic, `break` can cut the iteration from O(n) to O(log n) effectively (you stop as soon as you overshoot).

**When you need it**: Numeric problems where "too large" or "too small" is a thing (combination sum, partition problems). Always sort first to make the prune monotonic.

### Summary: three tiers of pruning

| Tier | What | When | Example |
|------|------|------|---------|
| **1. Continue** | Check `is_valid`, skip invalid | Always — the baseline | `if i > start and arr[i] == arr[i-1]: continue` |
| **2. Shrink choices** | Precompute valid set, iterate only those | Large candidate pool + precomputable constraints | Sudoku's `row & col & grid` |
| **3. Early break** | Stop loop when monotonic condition fails | Sorted data + monotonic prune | `if sum > target: break` on sorted array |

**Interview tip**: Start with tier 1 (continue). If TLE, check:
- Can I sort and break? → adds tier 3
- Can I precompute valid choices? → adds tier 2

Most problems need only tier 1 + 3. Tier 2 (shrink-first) is the "aha" insight in hard problems like sudoku and N-queens, but is overkill for simple combination/subset enumeration.

## The classic DFS template (for reference)

The two recipes below are the *graph/tree* DFS, the parent of backtracking. Note the structural identity: the `visited` set *is* the prune (step 3), and the children loop *is* `choices` (step 2). When you "backtrack" the visited set you get DFS for *enumerating* (that's what backtracking is); when you leave it marked you get DFS for *searching*.

```py
# recursive
visited = set()

def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return

    visited.add(node)

    # process current node here.
    ...
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)

# iterative
def DFS(self, tree):
    if tree.root is None:
        return []

    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # other processing work
```

- Applicable to most any problems
- storage cost low

## Applications

- [Flood Fill](https://en.wikipedia.org/wiki/Flood_fill) — the flat, non-recursive case where the "branches" are 4-directional grid neighbors and the "visited set" is the entire prune.

## Heuristic Search

A\* algorithm: use Priority Queue

```py
def AstarSearch(graph, start, end):
    pq = collections.priority_queue() # Valuation function: key for performance
    pq.append([start])
    visited.add(start)

    while pq:
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```

* key is [similarity measures](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)
