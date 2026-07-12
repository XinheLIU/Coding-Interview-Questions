---
name: resolve-problems
description: Move today's new/changed solutions out of problems/_unresolved/ into the proper problems/<id>-<slug>/ layout with correct filenames. Use when the user asks to "resolve", file, or organize the problems they solved today, or to clean up _unresolved. Detects genuinely new approaches to an existing problem and files them as solution.v2/v3 variants.
---

# Resolve today's solved problems

Take solution files sitting in `problems/_unresolved/` and file them into the problem-first layout. Scope to **today's work** by default (use git status/diff), unless the user says otherwise.

## 1. Find the candidates

```bash
git status --porcelain            # untracked/modified files
```

Focus on untracked files under `problems/_unresolved/` (and any modified ones the user points at). Each is one solution to place.

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

- **Folder doesn't exist** → new problem. Create the folder, move the file to `solution.<ext>`, and create `README.md` (see step 4).
- **Folder exists, no `solution.<ext>` of that language yet** → move it to `solution.<ext>`.
- **Folder exists and already has `solution.<ext>`** → this is a *new approach* to a solved problem. Compare the two:
  - **Genuinely different algorithm** (different idea, not a tweak) → file it as the next free variant: `solution.v2.<ext>`, then `solution.v3.<ext>`, etc. (Repo convention is `solution.v<n>.<ext>` — **not** `solution-2`. A descriptive variant like `solution.dp.py` is also fine when the approach has an obvious name.)
  - **Same approach** (same algorithm, only cosmetic/marker differences, or the existing version is equal-or-better) → it's a duplicate. **Don't create a variant and don't ask.** Discard the `_unresolved` copy. If it carries `@lc code=start/end` markers the existing `solution.<ext>` lacks, first port those markers into the existing file (wrap the code, keep the existing logic), then delete the copy. Only pause to ask if the unresolved copy is *materially better* than the existing one (e.g. fixes a bug the existing one has) — then confirm before overwriting.

> Watch for the split case: an `_unresolved/<id>.<slug>.py` file *and* a same-day edit to `problems/<id>-<slug>/solution.py`. That usually means the folder holds approach 1 and the unresolved file is approach 2 → file it as `solution.v2.py`.

## 4. Create the README when the folder is new

Match existing frontmatter exactly:

```yaml
---
id: 41
title: First Missing Positive
slug: first-missing-positive
difficulty:            # fill from the problem if known, else leave blank
topics: [array, hashing]
leetcode: https://leetcode.com/problems/first-missing-positive/
---

# 41. First Missing Positive

> Notes / intuition / complexity — TODO.
```

Fill `topics` from the `@lc` tags / your read of the solution. Leave `difficulty` blank if unknown rather than guessing.

## 5. Use `git mv`, then regenerate

- Prefer `git mv` so history/rename is tracked (untracked files: plain move is fine).
- After all moves: `python3 scripts/gen_index.py` (refreshes topic/difficulty indexes + sidebar).
- Verify: `npm run docs:build` catches broken `@/` includes and dead links.

## 6. Report, don't commit

Summarize what moved where, flag any files left in `_unresolved` and why. **Do not commit** unless the user explicitly asks.
