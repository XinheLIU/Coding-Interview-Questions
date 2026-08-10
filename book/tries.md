---
chapter: tries
---

# Tries

Last updated: 2026-08-10

A trie stores one edge per character, making prefixes explicit rather than
recomputing them from whole strings. The trade-off is predictable: query time is
proportional to the key length, while each node carries child-state overhead.

<ChapterGraph chapter="tries" />

<ChapterIndex chapter="tries" />
