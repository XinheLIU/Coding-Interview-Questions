# Development Guide

Last updated: 2026-08-10

## Prerequisites

- Node.js 22
- npm
- Python 3
- VS Code with the [LeetCode extension](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode) when adding solutions through the editor

## Local setup

```bash
npm install
npm run docs:dev
```

The development site runs at `http://localhost:5173/Coding-Interview-Questions/`.

Build the production site before submitting a change:

```bash
npm run docs:build
```

The build validates solution includes and internal links.

## Repository structure

```text
problems/<id>-<slug>/
    solution.py            # or .cpp / .sql
    solution.<variant>.py  # another approach in the same language
    README.md              # metadata, notes, and solution include
book/
    *.md                   # curriculum and prose chapters
    by-topic/              # generated topic indexes
    by-difficulty/         # generated difficulty indexes
scripts/
    taxonomy.py            # meta/leaf hierarchy and topic classification
    gen_index.py           # generates indexes, sidebar, and graph
    suggest_relations.py   # reports gaps in the knowledge graph
```

## How the book works

Chapters embed solution files instead of copying their code:

```md
<<< @/problems/1143-longest-common-subsequence/solution.py
```

Only the solution file is edited. VitePress transcludes its current contents when the site is built.

Each problem's `README.md` frontmatter supplies its metadata:

```yaml
---
id: 70
title: Climbing Stairs
difficulty: Easy
topics: [dynamic-programming]
leetcode: https://leetcode.com/problems/climbing-stairs/
relations: []
---
```

`scripts/taxonomy.py` defines seven meta-chapters and their concept-sized leaf chapters. Every topic maps to a leaf; a problem's highest-priority topic determines its leaf unless frontmatter contains an explicit leaf `chapter` override. Meta chapters aggregate their descendants and cannot own problems directly.

Relationships are typed, directed edges between problems:

```yaml
relations: [{"type": "specializes", "target": 746, "reason": "Adds a cost per stair to the same two-state recurrence."}]
```

Supported types are `builds-on`, `specializes`, `generalizes`, `same-pattern`, and `contrasts`. Add an edge only when its reason identifies a shared invariant, transformation, or meaningful contrast.

## Add or update a problem

The repository's `.vscode/settings.json` configures the LeetCode extension to write solutions to:

```text
problems/<id>-<slug>/solution.<ext>
```

After adding a solution:

1. Add or update the problem's `README.md` frontmatter.
2. Inspect related solutions for a defensible predecessor.
3. Regenerate derived files:

   ```bash
   python3 scripts/gen_index.py
   ```

4. Verify the site:

   ```bash
   npm run docs:build
   ```

Do not edit files under `book/by-topic/`, `book/by-difficulty/`, `.vitepress/sidebar-chapters.json`, `.vitepress/sidebar-problems.json`, or `.vitepress/problem-graph.json` by hand.

[Back to the repository overview](../ReadMe.md)
