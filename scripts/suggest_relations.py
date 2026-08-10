#!/usr/bin/env python3
"""Report where the knowledge graph is still thin. Read-only — never writes.

Run this after filing new problems to find the next edges worth adding:

    python3 scripts/suggest_relations.py            # summary
    python3 scripts/suggest_relations.py --chapter dynamic-programming  # meta
    python3 scripts/suggest_relations.py --chapter core-dp              # leaf
    python3 scripts/suggest_relations.py --isolated # just the unconnected problems

It reports candidates, not conclusions. A shared topic tag is not evidence of a
relationship — read the two solutions and name the shared invariant before adding
an edge (see CLAUDE.md).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import taxonomy

REPO = Path(__file__).resolve().parent.parent
GRAPH = REPO / ".vitepress" / "problem-graph.json"

# "Two Sum II" / "Coin Change 2" / "Subsets II" all share a stem with their
# predecessor. Stripping the trailing ordinal finds the series.
ORDINAL = re.compile(r"\s+(?:I{1,3}|IV|VI{0,3}|IX|X|\d+)$", re.IGNORECASE)


def load_graph() -> dict:
    if not GRAPH.exists():
        sys.exit("problem-graph.json missing — run scripts/gen_index.py first.")
    return json.loads(GRAPH.read_text())


def stem(title: str) -> str:
    previous = None
    current = title.strip()
    while current != previous:  # "Path Sum IV" -> "Path Sum"
        previous = current
        current = ORDINAL.sub("", current).strip()
    return current.lower()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chapter", help="only report this chapter id")
    parser.add_argument("--isolated", action="store_true",
                        help="list every problem with no relations at all")
    args = parser.parse_args()

    graph = load_graph()
    nodes = {n["id"]: n for n in graph["nodes"]}

    connected: set[int] = set()
    edge_pairs: set[frozenset[int]] = set()
    for edge in graph["edges"]:
        connected.add(edge["source"])
        connected.add(edge["target"])
        edge_pairs.add(frozenset((edge["source"], edge["target"])))

    if args.chapter and args.chapter not in taxonomy.CHAPTERS_BY_ID:
        allowed = ", ".join(c.id for c in taxonomy.CHAPTERS)
        sys.exit(f"unknown chapter '{args.chapter}'. Try one of: {allowed}")

    if not args.chapter:
        selected_ids = set(taxonomy.LEAF_CHAPTERS_BY_ID)
    else:
        selected_ids = {chapter.id for chapter in taxonomy.descendants_of(args.chapter)}
    chapters = [c for c in graph["chapters"] if c["id"] in selected_ids]
    chapter_ids = {c["id"] for c in chapters}
    scoped = [n for n in graph["nodes"] if n["chapter"] in chapter_ids]

    # ── 1. Title series missing an internal edge ──────────────────────────────
    series: dict[str, list[dict]] = defaultdict(list)
    for node in scoped:
        series[stem(node["title"])].append(node)

    gaps = []
    for name, members in sorted(series.items()):
        if len(members) < 2:
            continue
        members.sort(key=lambda n: n["id"])
        missing = [
            (a, b) for a, b in zip(members, members[1:])
            if frozenset((a["id"], b["id"])) not in edge_pairs
        ]
        if missing:
            gaps.append((name, members, missing))

    if gaps:
        print(f"── {len(gaps)} title series missing an internal edge "
              f"─────────────────────")
        for name, members, missing in gaps:
            chain = " → ".join(f"#{m['id']}" for m in members)
            print(f"  {name!r}: {chain}")
            for a, b in missing:
                print(f"      no edge between #{a['id']} {a['title']}")
                print(f"                  and #{b['id']} {b['title']}")
        print()
    else:
        print("✓ every detected title series is connected\n")

    # ── 2. Isolated problems per chapter ─────────────────────────────────────
    print("── coverage by chapter ───────────────────────────────────────────")
    for chapter in chapters:
        members = [n for n in scoped if n["chapter"] == chapter["id"]]
        if not members:
            continue
        isolated = [n for n in members if n["id"] not in connected]
        linked = len(members) - len(isolated)
        pct = 100 * linked / len(members)
        print(f"  {chapter['title']:34s} {linked:3d}/{len(members):3d} linked "
              f"({pct:4.0f}%)")
        if args.isolated and isolated:
            for node in sorted(isolated, key=lambda n: n["id"]):
                topics = ", ".join(node["topics"])
                print(f"      #{node['id']:<5d} {node['title'][:44]:46s} [{topics}]")
    print()

    # ── 3. Sections where nothing is linked yet ──────────────────────────────
    section_totals: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for node in scoped:
        section_totals[(node["chapter"], node["section"])].append(node)

    dead_sections = [
        (chapter, section, members)
        for (chapter, section), members in sorted(section_totals.items())
        if not any(n["id"] in connected for n in members)
    ]
    if dead_sections:
        print("── sections with zero relations — best place to add the next edge ─")
        for chapter, section, members in dead_sections:
            title = taxonomy.CHAPTERS_BY_ID[chapter].title
            print(f"  {title} › {section} ({len(members)} problems)")
        print()

    total_linked = len([n for n in scoped if n["id"] in connected])
    print(f"{len(graph['edges'])} edges · {total_linked}/{len(scoped)} problems "
          f"linked · {len(scoped) - total_linked} isolated")
    if not args.isolated:
        print("Re-run with --isolated to list the unconnected problems.")


if __name__ == "__main__":
    main()
