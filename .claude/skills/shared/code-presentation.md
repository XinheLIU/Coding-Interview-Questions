# Code presentation contract

Last updated: 2026-08-10

Shared by `resolve-problems` (problem READMEs) and `write-article` (book chapters).
Anywhere code from `problems/` is shown to a reader, these rules apply.

The goal: a reader lands on the page, sees the one idea the problem teaches, then
sees each language as its own section with each approach labelled and priced. They
never have to diff two code blocks to work out what changed.

## 1. Naming — one vocabulary per problem, across all languages

The same concept gets the **same identifier in every language file of that problem**.
If Python calls it `prev`, C++ does not call it `pre`. When you rename, rename across
`solution.py`, `solution.cpp`, `solution.sql` and every `solution.v*.*` together — the
whole point is that a reader can compare implementations without a translation step.

- **Never shadow a builtin.** `next`, `list`, `sum`, `max`, `min`, `id`, `input`, `set`,
  `str`, `type`. Use `next_node` (or `nxt` where the line is already dense).
- **Name by role, not by index or position.** `in_stack`/`out_stack`, not `stack1`/`stack2`.
  `slow`/`fast`, not `p1`/`p2`. The index tells the reader nothing; the role tells them
  what the variable is for.
- **Single letters only for loop indices and dimensions** — `i`, `j`, `k`, `m`, `n`.
  Everything else gets a word.
- **A longer descriptive name beats a short vague one** (project rule). `cur_sum` over `s`.

Canonical sets to reuse rather than reinvent:

| Shape | Names |
|---|---|
| Linked list | `dummy`, `head`, `prev`, `cur`, `next_node` |
| Pair swap / reorder | `dummy`, `prev`, `first`, `second` |
| Two pointers | `slow`/`fast`, or `left`/`right` |
| Stack pair | `in_stack`, `out_stack` |
| 1D DP | `dp`, `cur_sum`, `max_sum`, `prev1`/`prev2` for rolling variables |
| Grid DP | `dp`, `row`, `col` |

Keep LeetCode's given signature untouched — `head`, `nums`, `root`, `s` are fixed by the
problem and are not yours to rename.

## 2. Comments — the invariant or the trick, never the obvious

Two kinds, and nothing else.

**A header block above the method body** naming the state/invariant and the transition.
This is the style `problems/53-maximum-subarray/solution.py` already uses:

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = maximum sum of a subarray ending at index i
        # Transition: dp[i] = max(nums[i], dp[i-1] + nums[i])
        # In-place: reuse nums as the dp table
```

Three lines is usually right. State what the variables *mean* — that is the thing a
reader cannot recover from the code.

**Inline comments only where the step is non-obvious.** Good reasons to write one:

- the order of two statements is load-bearing (`# save the forward link before overwriting it`)
- the loop runs backwards or the iteration is unusual (`# right-to-left: dp[j] still holds the previous row`)
- a guard protects against a specific case (`# fast.next check: even-length lists`)
- an amortization or complexity argument lives here (`# each element transfers at most once → amortized O(1)`)

Never write a comment that restates its line. `# increment i` above `i += 1` is noise.
Comment the invariant or the trick, not the obvious (project rule).

**Preserve the LeetCode extension markers exactly** — `@lc app=leetcode id=... lang=...`,
`@lc code=start`, `@lc code=end`. They keep the file round-trippable through the extension.
Comments go *inside* the `code=start`/`code=end` fence so they survive a sync.

## 3. Complexity — per approach, not per problem

Every approach carries its own line, immediately under its heading and before the code:

```
*Time* `O(n)`, *space* `O(1)`
```

- **Space must count the recursion stack.** An iterative reversal is `O(1)` space; the
  recursive one is `O(n)`. That difference is usually the entire reason both variants are
  worth keeping — if you collapse them to one complexity line, the comparison dies.
- **Say amortized when it is amortized**, with the reason:
  `*Time* amortized `O(1)` per op, worst case `O(n)` — each element moves between stacks at most once`.
- Where `n` is ambiguous, define it: ``*Time* `O(n²)` where n is the number of rows``.

## 4. Heading layout — language first, approach second

Shared idea once, then one H2 per language, one H3 per 写法 inside it:

```markdown
## The key insight

The invariant every language and every approach below shares, stated once —
plus the naming used throughout, if it needs a word.

## Python

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.py

### Recursive

*Time* `O(n)`, *space* `O(n)` — one frame per pair

<<< @/problems/24-swap-nodes-in-pairs/solution.v2.py

## C++

### Iterative with a dummy node

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/24-swap-nodes-in-pairs/solution.cpp
```

Rules:

- **State the shared idea once, above the language sections.** That is the 找共同点 step:
  if the same invariant drives every implementation, the reader should read it once, not
  once per language. Only note per-language differences where they are real (idiomatic
  tuple assignment, manual memory, a builtin one language has and the other doesn't).
- **Use the language H2 even when only one language exists.** It keeps every problem page
  the same shape and makes the missing-language gap visible.
- **The approach H3 names the idea, never the filename.** "Recursive", "Two stacks with
  amortized transfer", "Floyd's cycle detection" — not "solution.v2.py". Name the file in
  the prose only if it helps someone find it on disk.
- **Order approaches by how you'd derive them**: the direct one first, the optimized one
  after. Show the journey, not just the destination.
- **Every `solution.v*.<ext>` on disk gets an H3 and a transclusion.** No orphans. (94
  variant files currently exist in this repo and none are transcluded anywhere — that is
  the gap this contract closes.)
- **Never paste code.** Always `<<< @/problems/<id>-<slug>/solution.<ext>`. To spotlight
  part of a long file, add `#region name` / `#endregion` anchors *to the source file first*,
  then reference `@/path#name`. Never line numbers.

## 5. Hard constraints (verified against this codebase)

- **Never hand-write a "Related problems" or "Knowledge graph" section.**
  `.vitepress/theme/ProblemRelations.vue` renders its own `<h2>Knowledge graph` from
  `problem-graph.json` via the `#doc-after` slot. Relationships live in frontmatter
  `relations` only.
- **`#doc-after` renders after the entire body**, so end a problem README with prose, not
  a code block — otherwise the injected heading collides with a transclusion.
- **`scripts/reorg.py --apply` rewrites every problem README body back to the
  `> Notes / intuition / complexity — TODO.` stub** (`reorg.py:199-211`). It is a one-time
  migration script. Never re-run it once READMEs have been written.
- **`scripts/gen_index.py` never writes README bodies** — it reads frontmatter only. Body
  structure is convention held by these skills, not enforced by any script. `npm run docs:build`
  is the only gate, and it only catches broken `@/` includes and dead links.
