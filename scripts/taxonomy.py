#!/usr/bin/env python3
"""The book's chapter taxonomy — the single source of truth for how topics roll up.

`scripts/gen_index.py` imports this to decide which chapter each problem belongs
to and to lay out the homepage curriculum map. Stdlib only, no side effects.

Two rules govern the mapping:

1. Every topic a problem carries must be declared in `TOPICS`. An undeclared tag
   is a typo and is rejected loudly rather than silently spawning an orphan page.
2. A problem's chapter is the chapter of its highest-priority topic. Ties are
   impossible because priorities are unique. A `chapter:` line in a problem's
   frontmatter overrides the derived value.
"""
from __future__ import annotations

from typing import NamedTuple


class Chapter(NamedTuple):
    id: str
    title: str
    page: str
    blurb: str
    col: int  # fixed grid coordinates for the homepage map, so the layout is
    row: int  # deterministic instead of force-simulated


# Curriculum order: the sequence a reader is meant to walk. SQL sits off the
# spine — it is a separate skill, not a later stage of the same one.
CHAPTERS: tuple[Chapter, ...] = (
    Chapter(
        "linear-structures",
        "Linear Structures",
        "/book/linear-structures",
        "Arrays, strings, linked lists, hashing, stacks and queues — where indices and pointers earn their keep.",
        0,
        1,
    ),
    Chapter(
        "trees",
        "Trees & Heaps",
        "/book/trees",
        "The first branching structure: binary trees, BSTs, tries, heaps.",
        1,
        0,
    ),
    Chapter(
        "recursion",
        "Recursion & Divide and Conquer",
        "/book/recursion",
        "Trusting the recursive call, and splitting a problem until it is trivial.",
        1,
        2,
    ),
    Chapter(
        "search-and-sort",
        "Search & Sort",
        "/book/search-and-sort",
        "Ordering, halving, and systematic exploration: sorting, binary search, DFS, BFS, backtracking, graphs.",
        2,
        1,
    ),
    Chapter(
        "dynamic-programming",
        "Dynamic Programming",
        "/book/dynamic-programming",
        "Naming a state, writing its transition, and paying for each subproblem once.",
        3,
        1,
    ),
    Chapter(
        "techniques",
        "Techniques",
        "/book/techniques",
        "Sharp tools that assume the fundamentals: bit tricks, greedy exchange arguments, math, data-structure design.",
        4,
        1,
    ),
    Chapter(
        "sql",
        "SQL",
        "/book/sql",
        "Set-at-a-time thinking: joins, grouping, and window functions.",
        4,
        2.6,
    ),
)

CHAPTERS_BY_ID = {chapter.id: chapter for chapter in CHAPTERS}

# Prerequisite edges drawn on the homepage map. SQL is intentionally unconnected.
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
    priority: int  # higher wins when a problem carries topics from two chapters


# Priority intent, high to low: the tag that names the *hardest idea in the
# solution* should win. `dfs` sits below the tree tags on purpose, so
# #104 Maximum Depth of Binary Tree stays in Trees while #200 Number of Islands
# lands in Search & Sort.
TOPICS: dict[str, TopicSpec] = {
    # SQL — a separate skill, always wins.
    "sql": TopicSpec("sql", "SQL", 100),

    # Dynamic programming.
    "knapsack": TopicSpec("dynamic-programming", "Knapsack", 91),
    "dynamic-programming": TopicSpec("dynamic-programming", "Core DP", 90),

    # Design outranks the containers it is built from — #146 LRU Cache is a
    # design problem, not a linked-list problem.
    "design": TopicSpec("techniques", "Data Structure Design", 80),

    # Trees and heaps.
    "trie": TopicSpec("trees", "Tries", 74),
    "heap-priority-queue": TopicSpec("trees", "Heaps & Priority Queues", 73),
    "binary-search-tree": TopicSpec("trees", "Binary Search Trees", 72),
    "binary-tree": TopicSpec("trees", "Binary Trees", 71),
    "traversal": TopicSpec("trees", "Tree Traversal", 70),
    "level-order": TopicSpec("trees", "Tree Traversal", 69),

    # Algorithmic foundations. These sit above the search tags on purpose: a
    # solution that splits-solves-combines is teaching divide and conquer, even
    # when the split happens to be a binary search or a sort.
    "divide-and-conquer": TopicSpec("recursion", "Divide and Conquer", 64),
    "recursion": TopicSpec("recursion", "Recursion", 63),

    # Systematic exploration.
    "back-tracking": TopicSpec("search-and-sort", "Backtracking", 62),
    "union-find": TopicSpec("search-and-sort", "Graphs", 61),
    "graph": TopicSpec("search-and-sort", "Graphs", 60),
    "dfs": TopicSpec("search-and-sort", "Depth-First Search", 59),
    "bfs": TopicSpec("search-and-sort", "Breadth-First Search", 58),
    "binary-search": TopicSpec("search-and-sort", "Binary Search", 57),
    "sorting": TopicSpec("search-and-sort", "Sorting", 56),

    # Sharp tools.
    "bitwise": TopicSpec("techniques", "Bit Manipulation", 42),
    "greedy": TopicSpec("techniques", "Greedy", 41),
    "math": TopicSpec("techniques", "Math & Number Theory", 40),

    # Linear structures, most specific pattern first.
    "sliding-window": TopicSpec("linear-structures", "Sliding Window", 32),
    "two-pointers": TopicSpec("linear-structures", "Two Pointers", 31),
    "cum-sum": TopicSpec("linear-structures", "Prefix Sums", 30),
    "k-sum": TopicSpec("linear-structures", "Hashing & k-Sum", 28),
    "stack": TopicSpec("linear-structures", "Stacks & Queues", 27),
    "queue": TopicSpec("linear-structures", "Stacks & Queues", 26),
    "linked-list": TopicSpec("linear-structures", "Linked Lists", 25),
    "hash-table": TopicSpec("linear-structures", "Hashing & k-Sum", 24),
    "palindrome": TopicSpec("linear-structures", "Strings", 22),
    "substring": TopicSpec("linear-structures", "Strings", 21),
    "string": TopicSpec("linear-structures", "Strings", 20),
    "2d-array": TopicSpec("linear-structures", "Arrays & Matrices", 11),
    "array": TopicSpec("linear-structures", "Arrays & Matrices", 10),
}

assert len({spec.priority for spec in TOPICS.values()}) == len(TOPICS), \
    "topic priorities must be unique so chapter assignment is deterministic"
assert {spec.chapter for spec in TOPICS.values()} <= set(CHAPTERS_BY_ID), \
    "every topic must point at a declared chapter"


def classify(topics: list[str]) -> tuple[str, str]:
    """Return the (chapter id, section) for a problem carrying `topics`.

    Raises KeyError if a topic is undeclared — callers surface it as an error.
    """
    if not topics:
        raise ValueError("a problem must carry at least one topic")
    winner = max(topics, key=lambda topic: TOPICS[topic].priority)
    spec = TOPICS[winner]
    return spec.chapter, spec.section


def sections_of(chapter_id: str) -> list[str]:
    """Sections of a chapter, in the priority order their topics declare."""
    specs = [spec for spec in TOPICS.values() if spec.chapter == chapter_id]
    ordered: list[str] = []
    for spec in sorted(specs, key=lambda s: -s.priority):
        if spec.section not in ordered:
            ordered.append(spec.section)
    return ordered
