#!/usr/bin/env python3
"""The book's two-level curriculum taxonomy.

Meta-chapters are the seven broad curriculum stages shown on the homepage.
Leaf chapters are the concept-sized teaching units beneath them.  Every topic
maps to exactly one leaf; a problem carrying several topics is placed in the
leaf belonging to its highest-priority topic.
"""
from __future__ import annotations

from typing import NamedTuple


class Chapter(NamedTuple):
    id: str
    title: str
    page: str
    blurb: str
    col: int
    row: float
    parent: str | None = None


# The seven stable level-1 URLs.  Their pages are now hubs for child chapters.
META_CHAPTERS: tuple[Chapter, ...] = (
    Chapter("linear-structures", "Linear Structures", "/book/linear-structures",
            "Arrays, strings, linked lists, hashing, stacks and queues.", 0, 1),
    Chapter("trees", "Trees & Heaps", "/book/trees",
            "Branching structures and the recursive invariants they expose.", 1, 0),
    Chapter("recursion", "Recursion & Divide and Conquer", "/book/recursion",
            "Trusting recursive calls and splitting problems into independent parts.", 1, 2),
    Chapter("search-and-sort", "Search & Sort", "/book/search-and-sort",
            "Ordering, halving, systematic exploration, and graph search.", 2, 1),
    Chapter("dynamic-programming", "Dynamic Programming", "/book/dynamic-programming",
            "Naming states, transitions, and the subproblems worth paying for once.", 3, 1),
    Chapter("techniques", "Techniques", "/book/techniques",
            "Sharp tools: design, bit tricks, greedy exchange, and mathematical reasoning.", 4, 1),
    Chapter("sql", "SQL", "/book/sql",
            "Set-at-a-time thinking: joins, grouping, and window functions.", 4, 2.6),
)


# Ordered level-2 teaching units.  Coordinates are unused by the homepage,
# but keeping them available makes the graph data uniform and deterministic.
LEAF_CHAPTERS: tuple[Chapter, ...] = (
    Chapter("arrays", "Arrays & Matrices", "/book/arrays",
            "Contiguous storage, index arithmetic, and array-shaped invariants.", 0, 0, "linear-structures"),
    Chapter("strings", "Strings", "/book/strings",
            "Character sequences, boundaries, and substring invariants.", 0, 0, "linear-structures"),
    Chapter("hashing", "Hashing", "/book/hashing",
            "Trading memory for constant-time lookup, counting, and membership.", 0, 0, "linear-structures"),
    Chapter("linked-lists", "Linked Lists", "/book/linked-lists",
            "Pointer ordering, sentinels, reversal, and fast/slow traversal.", 0, 0, "linear-structures"),
    Chapter("stacks-and-queues", "Stacks & Queues", "/book/stacks-and-queues",
            "LIFO/FIFO state machines and the boundaries they make explicit.", 0, 0, "linear-structures"),
    Chapter("binary-trees", "Binary Trees", "/book/binary-trees",
            "Recursive branching, traversal order, and subtree contracts.", 0, 0, "trees"),
    Chapter("binary-search-trees", "Binary Search Trees", "/book/binary-search-trees",
            "Ordering invariants that turn a tree walk into logarithmic search.", 0, 0, "trees"),
    Chapter("heaps", "Heaps & Priority Queues", "/book/heaps",
            "Partial order for top-k, streaming, and k-way frontier problems.", 0, 0, "trees"),
    Chapter("tries", "Tries", "/book/tries",
            "Prefix-shaped storage for dictionary and autocomplete queries.", 0, 0, "trees"),
    Chapter("recursion-basics", "Recursion", "/book/recursion-basics",
            "Base cases, recursive contracts, and trusting a smaller instance.", 0, 0, "recursion"),
    Chapter("divide-and-conquer", "Divide and Conquer", "/book/divide-and-conquer",
            "Split, solve, combine — and account for the resulting recurrence.", 0, 0, "recursion"),
    Chapter("binary-search", "Binary Search", "/book/binary-search",
            "Discarding half the search space while preserving a boundary invariant.", 0, 0, "search-and-sort"),
    Chapter("sorting", "Sorting", "/book/sorting",
            "Ordering as a primitive: partition, merge, counting, and stability.", 0, 0, "search-and-sort"),
    Chapter("graphs-and-traversal", "Graphs & Traversal", "/book/graphs-and-traversal",
            "Reachability, shortest paths, components, and graph-frontier state.", 0, 0, "search-and-sort"),
    Chapter("backtracking", "Backtracking", "/book/backtracking",
            "Enumerating a constrained search tree with reversible choices.", 0, 0, "search-and-sort"),
    Chapter("core-dp", "Core Dynamic Programming", "/book/core-dp",
            "State, transition, base case, and one payment per subproblem.", 0, 0, "dynamic-programming"),
    Chapter("knapsack-dp", "Knapsack DP", "/book/knapsack-dp",
            "Capacity states, inclusion choices, and one-dimensional compression.", 0, 0, "dynamic-programming"),
    Chapter("data-structure-design", "Data Structure Design", "/book/data-structure-design",
            "Compose primitive structures around the operations the API promises.", 0, 0, "techniques"),
    Chapter("bit-manipulation", "Bit Manipulation", "/book/bit-manipulation",
            "Masks, shifts, and invariants encoded directly in machine bits.", 0, 0, "techniques"),
    Chapter("greedy", "Greedy", "/book/greedy",
            "Make the locally safe choice and prove why it cannot hurt the optimum.", 0, 0, "techniques"),
    Chapter("math-number-theory", "Math & Number Theory", "/book/math-number-theory",
            "Algebraic structure, divisibility, and numerical observations that remove search.", 0, 0, "techniques"),
    Chapter("sql-queries", "SQL", "/book/sql-queries",
            "Joins, grouping, windows, and set-at-a-time transformations.", 0, 0, "sql"),
)


CHAPTERS: tuple[Chapter, ...] = META_CHAPTERS + LEAF_CHAPTERS
CHAPTERS_BY_ID = {chapter.id: chapter for chapter in CHAPTERS}
META_CHAPTERS_BY_ID = {chapter.id: chapter for chapter in META_CHAPTERS}
LEAF_CHAPTERS_BY_ID = {chapter.id: chapter for chapter in LEAF_CHAPTERS}


def children_of(chapter_id: str) -> tuple[Chapter, ...]:
    return tuple(chapter for chapter in LEAF_CHAPTERS if chapter.parent == chapter_id)


def descendants_of(chapter_id: str) -> tuple[Chapter, ...]:
    if chapter_id in LEAF_CHAPTERS_BY_ID:
        return (LEAF_CHAPTERS_BY_ID[chapter_id],)
    return children_of(chapter_id)


# Prerequisite edges remain at the level-1 curriculum scale. SQL is separate.
CHAPTER_FLOW: tuple[tuple[str, str], ...] = (
    ("linear-structures", "trees"),
    ("linear-structures", "recursion"),
    ("trees", "search-and-sort"),
    ("recursion", "search-and-sort"),
    ("search-and-sort", "dynamic-programming"),
    ("dynamic-programming", "techniques"),
)


class TopicSpec(NamedTuple):
    chapter: str
    section: str
    priority: int


# Higher-level algorithms win over incidental containers.  Among the linear
# topics, host structures win over reusable patterns so string windows stay in
# Strings while array windows stay in Arrays.
TOPICS: dict[str, TopicSpec] = {
    "sql": TopicSpec("sql-queries", "SQL", 300),
    "knapsack": TopicSpec("knapsack-dp", "Knapsack", 290),
    "dynamic-programming": TopicSpec("core-dp", "Core DP", 280),
    "design": TopicSpec("data-structure-design", "Data Structure Design", 270),
    "trie": TopicSpec("tries", "Tries", 260),
    "heap-priority-queue": TopicSpec("heaps", "Heaps & Priority Queues", 250),
    "binary-search-tree": TopicSpec("binary-search-trees", "Binary Search Trees", 240),
    "binary-tree": TopicSpec("binary-trees", "Binary Trees", 230),
    "traversal": TopicSpec("binary-trees", "Tree Traversal", 220),
    "level-order": TopicSpec("binary-trees", "Tree Traversal", 210),
    "divide-and-conquer": TopicSpec("divide-and-conquer", "Divide and Conquer", 200),
    "recursion": TopicSpec("recursion-basics", "Recursion", 190),
    "back-tracking": TopicSpec("backtracking", "Backtracking", 180),
    "union-find": TopicSpec("graphs-and-traversal", "Graphs", 170),
    "graph": TopicSpec("graphs-and-traversal", "Graphs", 160),
    "dfs": TopicSpec("graphs-and-traversal", "Depth-First Search", 150),
    "bfs": TopicSpec("graphs-and-traversal", "Breadth-First Search", 140),
    "binary-search": TopicSpec("binary-search", "Binary Search", 130),
    "sorting": TopicSpec("sorting", "Sorting", 120),
    "greedy": TopicSpec("greedy", "Greedy", 110),
    "bitwise": TopicSpec("bit-manipulation", "Bit Manipulation", 109),
    "math": TopicSpec("math-number-theory", "Math & Number Theory", 108),
    "k-sum": TopicSpec("arrays", "k-Sum", 91),
    "linked-list": TopicSpec("linked-lists", "Linked Lists", 90),
    "hash-table": TopicSpec("hashing", "Hashing", 89),
    "stack": TopicSpec("stacks-and-queues", "Stacks", 88),
    "queue": TopicSpec("stacks-and-queues", "Queues", 87),
    "string": TopicSpec("strings", "Strings", 86),
    "substring": TopicSpec("strings", "Substrings", 85),
    "palindrome": TopicSpec("strings", "Palindromes", 84),
    "2d-array": TopicSpec("arrays", "Arrays & Matrices", 83),
    "array": TopicSpec("arrays", "Arrays & Matrices", 82),
    "sliding-window": TopicSpec("arrays", "Sliding Window", 81),
    "two-pointers": TopicSpec("arrays", "Two Pointers", 80),
    "cum-sum": TopicSpec("arrays", "Prefix Sums", 79),
}

# Chapter ownership and in-chapter teaching order are different questions. A
# structural topic selects the host leaf, then a more specific pattern can name
# the section inside that leaf.
SECTION_PRIORITY: dict[str, int] = {
    "k-sum": 50,
    "sliding-window": 40,
    "two-pointers": 30,
    "cum-sum": 20,
    "2d-array": 10,
    "array": 0,
    "palindrome": 30,
    "substring": 20,
    "string": 10,
    "level-order": 30,
    "traversal": 20,
    "binary-tree": 10,
}

assert len({spec.priority for spec in TOPICS.values()}) == len(TOPICS), \
    "topic priorities must be unique so chapter assignment is deterministic"
assert {spec.chapter for spec in TOPICS.values()} <= set(LEAF_CHAPTERS_BY_ID), \
    "every topic must point at a declared leaf chapter"
assert {chapter.parent for chapter in LEAF_CHAPTERS} <= set(META_CHAPTERS_BY_ID), \
    "every leaf chapter must point at a declared meta chapter"


def classify(topics: list[str]) -> tuple[str, str]:
    if not topics:
        raise ValueError("a problem must carry at least one topic")
    winner = max(topics, key=lambda topic: TOPICS[topic].priority)
    chapter = TOPICS[winner].chapter
    section_candidates = [topic for topic in topics if TOPICS[topic].chapter == chapter]
    section_winner = max(
        section_candidates,
        key=lambda topic: SECTION_PRIORITY.get(topic, TOPICS[topic].priority),
    )
    return chapter, TOPICS[section_winner].section


def sections_of(chapter_id: str) -> list[str]:
    specs = [spec for spec in TOPICS.values() if spec.chapter == chapter_id]
    section_rank: dict[str, int] = {}
    for topic, spec in TOPICS.items():
        if spec.chapter == chapter_id:
            rank = SECTION_PRIORITY.get(topic, spec.priority)
            section_rank[spec.section] = max(section_rank.get(spec.section, -1), rank)
    return [section for section, _ in sorted(
        section_rank.items(), key=lambda item: -item[1]
    )]
