---
chapter: trees
---

# Trees & Heaps

Last updated: 2026-08-10

The first structure that branches. A linked list has one `next`; a tree has two or
more, and that single change is what turns "walk the whole thing" into "walk the
half that matters" — the seed of every logarithmic algorithm in the book.

This is also where recursion stops being a trick and becomes the natural way to
write code. A tree is defined recursively, so the code that processes it is too.

<ChapterChildren parent="trees" />

## Why trees come after linear structures

A tree *is* linear structures, composed. A BST is binary search with pointers
instead of indices. A heap is a complete binary tree flattened back into an array
(`parent = (i-1)//2`, `children = 2i+1, 2i+2`). A trie is a hash map at every node.
None of these make sense until arrays and hash tables are reflexive.

## The recursive contract

Almost every tree problem reduces to filling in one sentence: *"assume the
recursive call is already correct for both children — what do I do with the two
answers?"*

```python
def solve(node):
    if not node: return BASE          # the only place you handle emptiness
    left  = solve(node.left)          # trust it
    right = solve(node.right)         # trust it
    return combine(node.val, left, right)
```

Where problems differ is only in `BASE` and `combine`. Maximum Depth combines with
`1 + max(l, r)`. Same Tree combines with `l and r and vals match`. Diameter needs
two values — the answer through this node, and the answer to return upward — which
is the pattern behind #124 Binary Tree Maximum Path Sum and #543 Diameter.

**The trap.** A function that must return one thing but track another needs either
a `nonlocal` accumulator or a tuple return. Mixing these up is the single most
common tree bug.

## Traversal order is the whole game

- **Pre-order** (node, left, right) — serialization, copying, anything where the
  parent must be handled before its children exist.
- **In-order** (left, node, right) — on a BST this emits sorted order. That single
  fact solves validation (#98), kth smallest, and successor lookup (#285).
- **Post-order** (left, right, node) — anything where the answer depends on the
  children's answers: heights, sums, deletion.
- **Level order** (BFS with a queue) — anything phrased "by level" or "shortest".
  Right Side View (#199) and Largest Value per Row (#515) are the same traversal
  with a different per-level reduction.

Two traversals identify a tree uniquely if one of them is in-order — that is why
#105 and #106 are solvable and #889 (pre + post) needs the extra assumption that
the tree is full.

## BSTs: the invariant is everything

The BST property is not "left is smaller" — it is *"every key in the left subtree
is less than this node"*. Checking only the immediate child is the classic wrong
answer to #98. Carry a `(low, high)` range down instead, or verify that an
in-order walk is strictly increasing.

Once the invariant holds, search/insert/delete are all `O(h)`. Note `h`, not
`log n`: a BST built from sorted input degenerates into a linked list. That gap is
the reason self-balancing trees exist.

## Heaps: partial order is cheaper than total order

A heap only promises the *minimum is on top*, nothing about the rest. That weaker
promise is why `push`/`pop` are `O(log n)` and peeking is `O(1)`, and why you reach
for a heap whenever you need "the k best" rather than "everything, sorted":

- **Top-k** — keep a bounded heap of size k, not a sorted list of n (#703, #692).
- **Streaming median** — two heaps facing each other, max-heap for the low half and
  min-heap for the high half, kept within one element of balance (#295).
- **k-way merge** — one heap slot per list, pop the global minimum, push its
  successor. #23 Merge K Sorted Lists, #373, and #632 are all this one algorithm.

<ChapterIndex chapter="trees" />
