# Preparing a Coding Interview

Last updated: 2026-07-27

## Repository layout

Solutions are **problem-first**: one folder per problem, every language together.

```text
problems/<id>-<slug>/
    solution.py            # or .cpp / .sql; a variant is solution.v2.py
    README.md              # frontmatter (id, title, difficulty, topics, leetcode, relations) + notes
book/                      # VitePress "book" — chapters that transclude the real solution files
    linear-structures.md  trees.md  recursion.md  search-and-sort.md
    dynamic-programming.md  techniques.md  sql.md      # the seven curriculum chapters
    by-topic/  by-difficulty/   # GENERATED indexes — do not edit by hand
scripts/
    taxonomy.py            # single source of truth: topic → chapter, section, priority
    gen_index.py           # regenerate chapter data, indexes, sidebar, knowledge graph
    suggest_relations.py   # read-only report on where the graph is still thin
    reorg.py               # one-time language-first → problem-first migration
```

Browse the rendered book locally with `npm run docs:dev`, or build it with `npm run docs:build`.

## The book is a knowledge graph

Two structures sit on top of the same solution files:

**Seven chapters in learning order.** Linear Structures → Trees & Heaps → Recursion & Divide and Conquer → Search & Sort → Dynamic Programming → Techniques, with SQL alongside as a separate skill. Each problem's `topics` decide its chapter — `scripts/taxonomy.py` maps every topic to a chapter and a priority, and the highest-priority topic wins, so the chapter reflects the idea the problem actually teaches.

**Typed relationships between problems.** Each README's `relations` field records directed edges to other problems, each with a reason naming the shared invariant:

```yaml
relations: [{"type": "specializes", "target": 746,
             "reason": "Min Cost Climbing Stairs adds a cost per stair — the Fibonacci recurrence gains a min() overlay."}]
```

Types are `builds-on`, `specializes`, `generalizes`, `same-pattern`, and `contrasts`. Reverse edges are derived, never written twice. This is what makes LeetCode's implicit series explicit: Climbing Stairs → Min Cost Climbing Stairs → House Robber is a chain you can follow, and Two Sum → 3Sum → 3Sum Closest → 4Sum is another.

The homepage renders the chapter map; each chapter page renders its own prerequisite DAG plus a full index of its problems. A shared topic tag is not sufficient evidence for an edge — `python3 scripts/suggest_relations.py` reports thin spots so you know where the next edge belongs, but the reason has to come from reading both solutions.

## VS Code setup — LeetCode extension

Install **[`LeetCode.vscode-leetcode`](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode)** (LeetCode-OpenSource/vscode-leetcode) — the extension every solution here was authored with (they carry its `@lc app=leetcode` markers).

`.vscode/settings.json` already points it at the problem-first layout, so each new solve lands in the right folder automatically:

```jsonc
"leetcode.filePath": {
  "default": { "folder": "problems/${id}-${kebab-case-name}", "filename": "solution.${ext}" }
},
"leetcode.endpoint": "leetcode"   // or "leetcode-cn" for the China site
```

After adding or retagging a problem, run `python3 scripts/gen_index.py` to validate its topics and refresh the chapter map, indexes, sidebar, and graph.

---

### Principles

* Build Knowledge Structures
* Deliberate Practice
  * 5 to 7 times every question and expand
* Constant Feedback
* By Topics and Review

### 7 Steps for a Coding Interview

1. Listen and Clarification
2. Example \(big, non-special cases\)
3. Brute Force Solutions
4. Optimize
   1. Improve Step by Step
   2. Think up all possible Solutions
5. Walk through the solution
   * Explain clearly
   * Time and Space Complexity
6. Code
   1. White board or computer
   2. Coding Style
      1. indentation, naming, variable naming
   3. Modularization
7. Test Cases
   1. small and fast cases first
   2. edge case
   3. big test cases

---

# Coding Style

* Naming - "Naming and Cache Failure" 
  * Camel Style Naming
    * Python, Java
  * snake\_case
    * C++
* Indentation
* Comments
  * file comment at head
  * TO DO
  * parameter specification, function header
  * type hint
* Test Habit
  * function test
    * do test case in mind
  * edge case test
    * stack overflow
    * out of range situation
  * negative case test
    * invalid inputs
* Error Handling
  * Use Return Value
  * Use Global Variable
  * Throw Error
* Robustness
  * Defensive Programing

Suggestions

* leave blank lines \(~20%\)

#### Coding Style Examples

[PEP8 Coding Style Guid for Python](https://www.python.org/dev/peps/pep-0008/)

[Google Python Coding Style](http://google.github.io/styleguide/pyguide.html)

[Google C++ Coding Style Guide](#)

