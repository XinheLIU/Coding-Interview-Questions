---
name: resolve-problems
description: Move today's new/changed solutions out of problems/_unresolved/ into the proper problems/{id}-{slug}/ layout with correct filenames and evidence-backed knowledge-graph relationships. Use when the user asks to "resolve", file, or organize the problems they solved today, or to clean up _unresolved. Detects genuinely new approaches to an existing problem, files them as solution.v2/v3 variants, and identifies what each problem builds on or asks the user when unclear.
---

# Resolve today's solved problems

Last updated: 2026-07-27

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
relations: []
---

# 41. First Missing Positive

Last updated: 2026-07-14

> Notes / intuition / complexity — TODO.
```

Fill `topics` from the `@lc` tags / your read of the solution. Leave `difficulty` blank if unknown rather than guessing.

**Every topic must already be declared in `scripts/taxonomy.py`.** An unknown tag makes `gen_index.py` fail rather than silently creating an orphan topic page — check `TOPICS` there before inventing a name, and prefer an existing tag over a near-synonym. Tag the *technique the solution uses*, not the problem's surface: the topic with the highest priority decides which book chapter the problem lands in.

## 5. Find what the problem builds on

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

## 6. Use `git mv`, then regenerate

- Prefer `git mv` so history/rename is tracked (untracked files: plain move is fine).
- After all moves: `python3 scripts/gen_index.py` (validates topics, resolves chapters, refreshes indexes + sidebar + graph). If it fails on an unknown topic, fix the tag — do not add it to the taxonomy just to silence the error unless it is genuinely a new technique.
- Verify: `npm run docs:build` catches broken `@/` includes and dead links.

## 7. Report, don't commit

Summarize what moved where, flag any files left in `_unresolved` and why. **Do not commit** unless the user explicitly asks.
