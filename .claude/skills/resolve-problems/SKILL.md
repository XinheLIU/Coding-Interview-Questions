---
name: resolve-problems
description: File LeetCode solutions into problems/, extract alternate approaches buried in comments into real solution.v<n> files, unify variable naming across languages and add invariant comments, establish evidence-backed knowledge-graph relationships, and write READMEs that present each language and each approach with its own complexity. Use only when the user explicitly asks to "resolve" or organize specific problems.
---

# Resolve and Enrich Problem Solutions

Last updated: 2026-08-10

**Invocation:** Only when the user explicitly requests it. Do not auto-trigger based on git status.

**Core jobs:**
1. File the solution in the right place (steps 1–3)
2. Extract alternate approaches buried in comments into real `solution.v<n>.<ext>` files (step 4)
3. Unify naming across languages and add invariant comments (step 5)
4. Write a README that shows each language and each approach with its own complexity (step 6)
5. Establish evidence-backed relationships between problems (step 7)

**Read `.claude/skills/shared/code-presentation.md` before touching code or writing a README.**
It holds the naming, comment, complexity, and heading rules that steps 4–6 all depend on, and
it is shared with the `write-article` skill so chapters and READMEs present code identically.

## 1. Find the candidates

The user specifies which problems to work on. Common patterns:
- Problems in `_unresolved/` that need filing
- Existing problems that need documentation improvements
- A list of problem IDs the user mentions

For problems in `_unresolved/`, derive the target from `@lc` markers (see step 2).

## 2. Derive the target folder from the `@lc` marker

LeetCode-extension files carry a header:

```
# @lc app=leetcode id=41 lang=python3
# [41] First Missing Positive
```

- **id** → the folder id (bare, not zero-padded).
- **slug** → kebab-case of the title, matching existing folders. Prefer the URL slug from the `https://leetcode.com/problems/<slug>/` line if present; else kebab-case the title. Sanity-check against sibling folders (`ls problems/ | grep -i <keyword>`) so you don't create a near-duplicate slug.
- **ext** from `lang`: `python3`→`py`, `cpp`→`cpp`, `mysql`/`mssql`→`sql`, etc.

Target: `problems/<id>-<slug>/solution.<ext>`.

**No `@lc` marker** (slug-only files like `2-sum-closest.py`, or `draft.py`): id can't be derived — these are often non-LeetCode / LintCode notes. Don't guess. List them and ask the user, or leave in `_unresolved`.

## 3. Decide the filename — new problem, or new approach?

For each candidate, check whether `problems/<id>-<slug>/` already exists.

- **Folder doesn't exist** → new problem. Create the folder, move the file to `solution.<ext>`, and create `README.md` (see step 6).
- **Folder exists, no `solution.<ext>` of that language yet** → move it to `solution.<ext>`.
- **Folder exists and already has `solution.<ext>`** → this is a *new approach* to a solved problem. Compare the two:
  - **Genuinely different algorithm** (different idea, not a tweak) → file it as the next free variant: `solution.v2.<ext>`, then `solution.v3.<ext>`, etc. (Repo convention is `solution.v<n>.<ext>` — **not** `solution-2`. A descriptive variant like `solution.dp.py` is also fine when the approach has an obvious name.)
  - **Same approach** (same algorithm, only cosmetic/marker differences, or the existing version is equal-or-better) → it's a duplicate. **Don't create a variant and don't ask.** Discard the `_unresolved` copy. If it carries `@lc code=start/end` markers the existing `solution.<ext>` lacks, first port those markers into the existing file (wrap the code, keep the existing logic), then delete the copy. Only pause to ask if the unresolved copy is *materially better* than the existing one (e.g. fixes a bug the existing one has) — then confirm before overwriting.

> Watch for the split case: an `_unresolved/<id>.<slug>.py` file *and* a same-day edit to `problems/<id>-<slug>/solution.py`. That usually means the folder holds approach 1 and the unresolved file is approach 2 → file it as `solution.v2.py`.

## 4. Extract alternate approaches buried in comments

Older solutions in this repo often carry a second implementation **commented out inside the
primary file** — a Python `'''...'''` block, a C++ `/* ... */`, or a run of `#`/`//` lines.
That code is invisible on the site and rots silently. Promote it to a real file.

1. **Scan the primary solution** for commented-out implementations. Distinguish them from the
   LeetCode boilerplate (`# Definition for singly-linked list.`) and from the `@lc` markers,
   which stay.
2. **Apply the step-3 test.** Genuinely different algorithm → promote. Cosmetic rewrite of the
   same algorithm (a tuple-assignment version of the same loop) → delete it; it teaches nothing
   the primary file doesn't.
3. **Verify it actually runs before promoting it.** This code has never been executed — it was
   commented out precisely so nobody had to check. Broken variants found in this repo include a
   recursive `swapPairs` returning `None` instead of `head` (truncates odd-length lists) and a
   reversal mixing `head` and `node` identifiers (`NameError`). Read it line by line against the
   invariant; where it is wrong, **fix it**, and report every fix in the step 9 summary. Never
   promote code you have not convinced yourself is correct.
4. **Write it as the next free variant** — `solution.v2.<ext>`, then `solution.v3.<ext>`. Give it
   the same `@lc` header as the primary file plus an approach line, the convention
   `problems/53-maximum-subarray/solution.v2.py` sets:

   ```python
   #
   # @lc app=leetcode id=24 lang=python3
   #
   # [24] Swap Nodes in Pairs
   #
   # Approach 2: Recursive
   ```
5. **Delete the commented-out block from the primary file.** One approach per file; the README
   is what links them.
6. Every promoted variant gets an H3 and a transclusion in the README (step 6). A variant file
   that no README transcludes is invisible — that is the state 94 existing `solution.v*.*` files
   are already in.

## 5. Unify naming and add invariant comments

Follow `.claude/skills/shared/code-presentation.md`. The two moves that matter most:

- **Rename across every language file of the problem in one pass.** The value of showing Python
  and C++ side by side is that a reader can compare them without translating; that breaks the
  moment `prev` in one is `pre` in the other. Pick the canonical set from the contract, then apply
  it to `solution.<ext>` and every `solution.v*.<ext>` together.
- **Fix builtin shadowing while you are there** — `next`, `list`, `sum`, `id`. It is the most
  common defect in this repo's older solutions.

Then add the header comment block naming the state and the transition, plus inline comments only
where the step is non-obvious (load-bearing statement order, reversed iteration, a guard's purpose,
an amortization argument). Never a comment that restates its line.

Do not restructure working logic beyond this. Renaming, comments, and a genuine bug fix are in
scope; rewriting a correct solution into your preferred style is not.

## 6. Write the README

Use `references/readme-template.md` — it has the full skeleton and a filled example.
Body order:

```
# <id>. <Title> → Last updated → Why this problem matters → The key insight
→ ## <Language> / ### <Approach> (+ complexity + transclusion) per language
→ The extensibility → Variations to ask
```

The rules that make it readable, all from the shared contract:

- **State the shared idea once**, above the language sections — the invariant every implementation
  uses. Don't re-explain it per language.
- **One H2 per language, one H3 per approach**, even when there is only one of either.
- **Every H3 carries its own complexity line** before the code, with recursion stack counted in
  space. That difference is why both variants exist.
- **Transclude every `solution*.<ext>` in the folder.** No orphans.
- **End with prose, not a code block** — the theme injects `<h2>Knowledge graph` after the whole
  body via `#doc-after`, and never hand-write a related-problems section yourself.

Frontmatter is unchanged and must match existing problems exactly:

```yaml
---
id: 41
title: First Missing Positive
slug: first-missing-positive
difficulty:            # fill from the problem if known, else leave blank
topics: [array, hashing]
leetcode: https://leetcode.com/problems/first-missing-positive/
relations: []
---
```

Fill `topics` from the `@lc` tags / your read of the solution. Leave `difficulty` blank if unknown rather than guessing.

**Every topic must already be declared in `scripts/taxonomy.py`.** An unknown tag makes `gen_index.py` fail rather than silently creating an orphan topic page — check `TOPICS` there before inventing a name, and prefer an existing tag over a near-synonym. Tag the *technique the solution uses*, not the problem's surface: the topic with the highest priority decides which book chapter the problem lands in.

When updating an **existing** README that still holds the `> Notes / intuition / complexity — TODO.`
stub, replace the whole body — the stub's bare back-to-back transclusions are exactly what this
layout is replacing.

## 7. Find what the problem builds on

For every candidate, ensure its README has a `relations` field. Preserve existing relationships.

1. Read the filed solution and state its central invariant or transformation.
2. Search existing problem READMEs and solutions for an earlier problem that teaches a prerequisite reused here. A shared topic tag is not enough. `python3 scripts/suggest_relations.py --chapter <chapter-id>` lists nearby unconnected problems and title series with a missing internal edge — useful as a candidate list, not as evidence.
3. When the evidence is clear, add a directed `builds-on` relation as valid inline JSON:

```yaml
relations: [{"type": "builds-on", "target": 20, "reason": "Reuses stack-based parenthesis matching, then tracks substring boundaries."}]
```

Keep the reason to one sentence and name the reused idea. Do not add the reverse edge; `scripts/gen_index.py` derives it. If no predecessor is defensible, ask the user whether the problem intentionally has no `builds-on` edge or which problem they see as its prerequisite. Group this into one question when resolving multiple problems. Do not guess.

Pick the type by what the relationship actually is — `builds-on` (reuses a prerequisite idea), `specializes` (adds a constraint to the same recurrence or template), `generalizes` (the inverse), `same-pattern` (different surface, same machinery), `contrasts` (looks similar, needs a different tool, and knowing why is the lesson). For a numbered series such as Climbing Stairs → Min Cost Climbing Stairs, link each step to the next rather than fanning everything off the first problem: the chain is what shows the progression.

Refresh the README's `Last updated: YYYY-MM-DD` line whenever its metadata changes.

## 8. Use `git mv`, then regenerate

- Prefer `git mv` so history/rename is tracked (untracked files: plain move is fine).
- After all moves: `python3 scripts/gen_index.py` (validates topics, resolves chapters, refreshes indexes + sidebar + graph). If it fails on an unknown topic, fix the tag — do not add it to the taxonomy just to silence the error unless it is genuinely a new technique.
- Verify: `npm run docs:build` catches broken `@/` includes and dead links. It is the only check that a transclusion you wrote points at a file that exists.
- **Never run `scripts/reorg.py --apply`.** It rewrites every problem README body back to the TODO stub — it is a one-time migration script that predates written READMEs.

## 9. Report, don't commit

Summarize:

- what moved where, and any files left in `_unresolved` with the reason
- **every variant promoted out of comments**, and **every bug you fixed in one** — these are logic
  changes to code the user has not read, so they must be surfaced, not buried
- every identifier renamed, grouped by problem

**Do not commit** unless the user explicitly asks.
