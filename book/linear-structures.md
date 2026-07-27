---
chapter: linear-structures
---

# Linear Structures

Last updated: 2026-07-26

Arrays, strings, linked lists, hash tables, stacks and queues. This is the
foundation chapter: everything later in the book is built out of these, and the
habits you form here — reaching for a sentinel node, knowing when a hash map buys
you an order of magnitude — are the ones you reuse for the rest of your career.

The through-line is a single trade-off, restated in different clothes.

## The trade-off, sharpened

Arrays buy **O(1) random access** with contiguity (address is `base + i*size`, and neighbors share a cache line). Linked lists buy **O(1) splice** with pointers, paying it back as O(n) access. Choosing between them is "space for time" in miniature: arrays win when reads dominate or memory/cache is tight; lists win when insert/delete churn is high and you can spend memory for speed.

## Non-obvious moves

- **Unordered insert into an array is O(1).** If order doesn't matter, swap the target slot's element to the end and drop the new value in — the quicksort partition move. No shift.
- **Batch delete via mark-and-sweep.** Defer compaction; mark deleted, sweep once when forced. Amortizes N deletes into one pass (GC's sweep phase).
- **`prev` pointer earns its keep on delete/reverse.** Singly linked delete needs the predecessor → O(n) scan. Doubly linked → O(1). That's the whole reason LRU uses a doubly linked list.
- **Boxing overhead is real.** A container of `Integer` pays an allocation + indirection per element; a primitive array doesn't. Only matters in hot paths.

## Applications worth naming

- **LRU cache** = doubly linked list (recency order, head = MRU, tail = evict) + hash map (key → node). The list gives O(1) reorder/evict; the map gives O(1) lookup. Neither alone suffices.
- Browser back/forward, undo stacks, task queues — all list-shaped at heart.
- Array abstractions show up in DB indexes and dynamic-array internals; the cache-friendliness argument is the reason.

## What these problems actually probe

- **Pointer ordering.** Link forward *before* repointing the predecessor, or you drop the tail:
  ```python
  new.next = p.next   # save the forward link first
  p.next = new        # then overwrite p.next
  ```
- **Sentinel node.** A dummy head collapses first-node / last-node / head cases into the interior path. Candidates who reach for it write fewer branches and fewer bugs — a fast signal.
- **Boundaries that separate levels:** empty, one node, two nodes, head/tail operations.
- **Range.** Brute → optimized → optimal on the same prompt lets you watch the candidate *move*, which is the real measurement.

## As algorithm vehicles

- *Arrays:* two pointers, sliding window, prefix sums, binary search.
- *Lists:* fast/slow pointers (midpoint, cycle), in-place reversal, merge sorted.


<ChapterGraph chapter="linear-structures" />

<ChapterIndex chapter="linear-structures" />
