---
id: 141
title: Linked List Cycle
slug: linked-list-cycle
difficulty: Easy
topics: [linked-list, two-pointers]
leetcode: https://leetcode.com/problems/linked-list-cycle/
relations: []
---

# 141. Linked List Cycle

Last updated: 2026-08-10

## Why this problem matters

The cleanest demonstration that two pointers at different speeds extract structural information a
single pointer cannot. The naive answer — a hash set of visited nodes — is correct, `O(n)` time, and
`O(n)` space. Floyd's gets the same answer in `O(1)` space with no auxiliary structure at all.

## The key insight

**Fast gains exactly one position on slow per iteration, so inside a cycle the gap is taken mod L
and must eventually reach zero.** That is the entire proof, and it is why fast moves 2 and not 3 —
a larger step still terminates but no longer guarantees a gap of one, so the argument gets harder
without buying anything.

The loop guard `fast and fast.next` is doing double duty: only `fast` can run off the end, so
checking it also protects `slow`, and checking `fast.next` is what makes `fast.next.next` safe.

Both implementations use the same names: `slow`, `fast`.

## Python

### Floyd's cycle detection

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/141-linked-list-cycle/solution.py

## C++

### Floyd's cycle detection

*Time* `O(n)`, *space* `O(1)`

<<< @/problems/141-linked-list-cycle/solution.cpp

## The extensibility

- **Find the entry node, not just the fact of a cycle** — [142](https://leetcode.com/problems/linked-list-cycle-ii/)
  adds a second phase on top of this exact loop. The whole extension is four extra lines.
- **Measure the cycle length** — once the pointers meet, hold one still and walk the other until it
  returns; the step count is `L`.
- **Find the midpoint** — the same fast/slow machinery with no cycle: when fast hits the end, slow is
  at the middle. That underpins
  [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) and merge sort on lists.
- **Cycle detection outside linked lists** — the same argument finds a repeated value in an array where
  indices point at indices ([287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)),
  which is the version that surprises people.

## Variations to ask

1. Now return the node where the cycle begins. (*The natural follow-up — #142.*)
2. How long is the cycle? (*Tests whether they understand the meeting point or just memorized the loop.*)
3. Why does fast move two steps? Would three work? (*Separates the proof from the pattern.*)
4. Solve it with `O(n)` space first. (*A hash set is a fine first answer; the interest is in what replaces it.*)
