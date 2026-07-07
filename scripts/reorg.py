#!/usr/bin/env python3
"""One-time migration: language-first tree -> problem-first `problems/<id>-<slug>/`.

Dry-run by default (writes _migration_report.md, moves nothing). Pass --apply to
execute via `git mv`. Stdlib only.

Strategy
--------
1. Parse every solution file. Directly extract id+slug when the filename carries an
   id (`56.merge-intervals.py`, `184.Department Highest Salary.sql`, `185-...sql`).
2. Build slug->id and id->kebab-slug maps from the id'd files.
3. Resolve id-less title files (`Reverse Integer.py`) by normalizing the title to a
   slug and looking it up in that map. Whatever stays unresolved -> _unresolved/, never guessed.
4. Group by id -> problems/<id>-<slug>/. First file per language -> solution.<ext>;
   extra same-language files -> solution.vN.<ext> (identical dups dropped), all reported.
5. Seed frontmatter `topics` from the old folder path so no topic info is lost.
"""
from __future__ import annotations

import argparse
import filecmp
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXTS = {".py": "py", ".cpp": "cpp", ".sql": "sql"}

# Folder-name segments that are grouping noise, not real topics.
TOPIC_STOP = {"algorithm", "data-structure", "basic", "templates", "advanced",
              "operations", "very-basic", "search", "linear-list"}
# Fix known misspellings / odd folder names when turning them into topic tags.
TOPIC_FIXUP = {"devide-and-conquer": "divide-and-conquer", "knapspack": "knapsack",
               "serilization-deserialization": "serialization-deserialization",
               "sequence-array": "array", "queue-deque": "queue"}

ID_RE = re.compile(r"^(\d+)[.\-]\s*(.+)$")  # applied to the stem (name без ext)


def kebab(text: str) -> str:
    """Lowercase kebab slug. Splits camelCase (TwoSum->two-sum) then non-alnum->dash."""
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)  # camel boundary
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.lower())
    return text.strip("-")


def looks_kebab(stem_rest: str) -> bool:
    """True for `merge-intervals` style, False for `Merge Intervals` / `Rotate Image`."""
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", stem_rest))


@dataclass
class Rec:
    src: Path
    ext: str
    stem_rest: str          # filename stem minus any leading "id." prefix — the slug/title text
    raw_id: int | None
    slug: str               # normalized kebab slug
    is_kebab_src: bool
    display_title: str      # human title if the source gave one, else ""
    topics: list[str] = field(default_factory=list)
    mtime: float = 0.0
    resolved_id: int | None = None


def topics_from_path(src: Path) -> list[str]:
    parts = src.relative_to(REPO).parts[1:-1]  # drop lang root and filename
    out = []
    for p in parts:
        t = kebab(p)
        t = TOPIC_FIXUP.get(t, t)
        if t and t not in TOPIC_STOP and t not in out:
            out.append(t)
    return out


def parse(src: Path) -> Rec:
    ext = EXTS[src.suffix.lower()]
    stem = src.stem.strip()
    m = ID_RE.match(stem)
    raw_id = None
    rest = stem
    display_title = ""
    if m:
        raw_id = int(m.group(1))
        rest = m.group(2).strip()
    is_kebab = looks_kebab(rest)
    if not is_kebab:
        display_title = rest  # already human-readable
    return Rec(
        src=src, ext=ext, stem_rest=rest, raw_id=raw_id, slug=kebab(rest),
        is_kebab_src=is_kebab, display_title=display_title,
        topics=topics_from_path(src), mtime=src.stat().st_mtime,
    )


def collect() -> list[Rec]:
    """Scan every .py/.cpp/.sql anywhere in the repo (some are misfiled across language
    roots, e.g. a .py under Cpp/ or a .sql under Python/), excluding non-solution dirs."""
    skip_tops = {"problems", "book", "scripts", "node_modules", ".vitepress", ".git"}
    recs: list[Rec] = []
    for f in REPO.rglob("*"):
        if f.suffix.lower() not in EXTS or not f.is_file():
            continue
        rel = f.relative_to(REPO)
        if rel.parts[0] in skip_tops or ".vscode" in rel.parts:
            continue
        recs.append(parse(f))
    return recs


def build_maps(recs: list[Rec]):
    slug_to_ids: dict[str, set[int]] = defaultdict(set)
    id_to_kebab: dict[int, str] = {}
    id_to_title: dict[int, str] = {}
    for r in recs:
        if r.raw_id is None:
            continue
        slug_to_ids[r.slug].add(r.raw_id)
        if r.is_kebab_src:
            id_to_kebab.setdefault(r.raw_id, r.slug)
        if r.display_title:
            id_to_title.setdefault(r.raw_id, r.display_title)
    return slug_to_ids, id_to_kebab, id_to_title


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="execute git mv (default: dry-run)")
    args = ap.parse_args()

    recs = collect()
    slug_to_ids, id_to_kebab, id_to_title = build_maps(recs)

    warnings: list[str] = []
    # Resolve ids.
    for r in recs:
        if r.raw_id is not None:
            r.resolved_id = r.raw_id
            continue
        ids = slug_to_ids.get(r.slug)
        if ids and len(ids) == 1:
            r.resolved_id = next(iter(ids))
        elif ids:
            warnings.append(f"AMBIGUOUS slug '{r.slug}' -> ids {sorted(ids)} : {r.src.relative_to(REPO)}")

    # Detect same-slug/different-id mislabels (e.g. SQL 185 vs 1185).
    for slug, ids in slug_to_ids.items():
        if len(ids) > 1:
            warnings.append(f"MISLABEL? slug '{slug}' carries multiple ids {sorted(ids)} (same problem, different id)")

    # Canonical slug + title per id.
    def canon_slug(pid: int, group: list[Rec]) -> str:
        if pid in id_to_kebab:
            return id_to_kebab[pid]
        return sorted((g.slug for g in group), key=len)[0] or f"id-{pid}"

    def canon_title(pid: int, slug: str) -> str:
        if pid in id_to_title:
            return id_to_title[pid]
        return slug.replace("-", " ").title()

    by_id: dict[int, list[Rec]] = defaultdict(list)
    unresolved: list[Rec] = []
    for r in recs:
        (by_id[r.resolved_id].append(r) if r.resolved_id is not None else unresolved.append(r))

    moves: list[tuple[Path, Path]] = []
    drops: list[tuple[Path, Path]] = []  # (identical duplicate, canonical it duplicates)
    readmes: dict[Path, str] = {}

    for pid, group in sorted(by_id.items()):
        slug = canon_slug(pid, group)
        title = canon_title(pid, slug)
        pdir = REPO / "problems" / f"{pid}-{slug}"
        topics = sorted({t for g in group for t in g.topics})
        # Per language: choose canonical (newest mtime, prefer kebab source), number the rest.
        for ext in ("py", "cpp", "sql"):
            langfiles = sorted((g for g in group if g.ext == ext),
                               key=lambda g: (not g.is_kebab_src, -g.mtime))
            n = 0
            for i, g in enumerate(langfiles):
                if i == 0:
                    dst = pdir / f"solution.{ext}"
                else:
                    # identical to the canonical? drop it, else keep as vN.
                    if filecmp.cmp(str(g.src), str(langfiles[0].src), shallow=False):
                        drops.append((g.src, langfiles[0].src))
                        continue
                    n += 1
                    dst = pdir / f"solution.v{n + 1}.{ext}"
                    warnings.append(f"DRIFTED dup id {pid} {ext}: kept {g.src.relative_to(REPO)} as {dst.name}")
                moves.append((g.src, dst))
        langs = sorted({g.ext for g in group})
        lc = f"https://leetcode.com/problems/{slug}/" if pid in id_to_kebab else ""
        readmes[pdir / "README.md"] = (
            "---\n"
            f"id: {pid}\n"
            f"title: {title}\n"
            f"slug: {slug}\n"
            "difficulty:\n"
            f"topics: [{', '.join(topics)}]\n"
            f"leetcode: {lc}\n"
            "---\n\n"
            f"# {pid}. {title}\n\n"
            "> Notes / intuition / complexity — TODO.\n\n"
            + "".join(f"<<< @/problems/{pid}-{slug}/solution.{e}\n" for e in langs)
        )

    for r in unresolved:
        dst = REPO / "problems" / "_unresolved" / f"{r.slug or r.src.stem}.{r.ext}"
        k = 2
        while dst in {m[1] for m in moves}:
            dst = REPO / "problems" / "_unresolved" / f"{r.slug}-{k}.{r.ext}"
            k += 1
        moves.append((r.src, dst))

    # ---- report ----
    report = [f"# Migration report (dry-run={'no' if args.apply else 'yes'})\n",
              f"- solution files scanned: {len(recs)}",
              f"- problems (unique ids): {len(by_id)}",
              f"- planned moves: {len(moves)}",
              f"- identical duplicates dropped: {len(drops)}",
              f"- unresolved (no derivable id): {len(unresolved)}",
              f"- warnings: {len(warnings)}\n",
              "## Warnings (review these)\n"]
    report += [f"- {w}" for w in sorted(set(warnings))] or ["- none"]
    report.append("\n## Unresolved -> problems/_unresolved/ (triage manually)\n")
    report += [f"- {r.src.relative_to(REPO)}  ->  {r.slug or r.src.stem}.{r.ext}"
               for r in sorted(unresolved, key=lambda r: str(r.src))] or ["- none"]
    report.append("\n## Identical duplicates dropped\n")
    report += [f"- {a.relative_to(REPO)}  (== {b.relative_to(REPO)})" for a, b in drops] or ["- none"]
    (REPO / "_migration_report.md").write_text("\n".join(report) + "\n")

    print("\n".join(report[:8]))
    print(f"\nWrote _migration_report.md  ({'APPLIED' if args.apply else 'dry-run, nothing moved'})")

    if not args.apply:
        return 0

    # ---- execute ----
    for src, dst in moves:
        dst.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "mv", str(src), str(dst)], cwd=REPO, check=True)
    for a, _ in drops:
        subprocess.run(["git", "rm", "-q", str(a)], cwd=REPO, check=True)
    for path, text in readmes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        subprocess.run(["git", "add", str(path)], cwd=REPO, check=True)
    print(f"Moved {len(moves)}, dropped {len(drops)}, wrote {len(readmes)} READMEs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
