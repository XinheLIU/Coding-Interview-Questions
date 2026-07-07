# Preparing a Coding Interview

Last updated: 2026-07-07

## Repository layout

Solutions are **problem-first**: one folder per problem, every language together.

```text
problems/<id>-<slug>/
    solution.py            # or .cpp / .sql; a variant is solution.v2.py
    README.md              # frontmatter metadata (id, title, difficulty, topics, leetcode) + notes
book/                      # VitePress "book" — prose chapters that transclude the real solution files
    by-topic/  by-difficulty/   # GENERATED indexes — do not edit by hand
scripts/
    reorg.py               # one-time language-first → problem-first migration
    gen_index.py           # regenerate topic/difficulty indexes + sidebar from frontmatter
```

Browse the rendered book locally with `npm run docs:dev`, or build it with `npm run docs:build`.

## VS Code setup — LeetCode extension

Install **[`LeetCode.vscode-leetcode`](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode)** (LeetCode-OpenSource/vscode-leetcode) — the extension every solution here was authored with (they carry its `@lc app=leetcode` markers).

`.vscode/settings.json` already points it at the problem-first layout, so each new solve lands in the right folder automatically:

```jsonc
"leetcode.filePath": {
  "default": { "folder": "problems/${id}-${kebab-case-name}", "filename": "solution.${ext}" }
},
"leetcode.endpoint": "leetcode"   // or "leetcode-cn" for the China site
```

After adding or retagging a problem, run `python3 scripts/gen_index.py` to refresh the topic/difficulty indexes.

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

