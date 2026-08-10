from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


class GeneratedCurriculumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = json.loads(
            (REPO / ".vitepress" / "problem-graph.json").read_text()
        )

    def test_every_problem_has_exactly_one_leaf_home(self) -> None:
        leaf_ids = set(self.graph["leaf_chapters"])
        self.assertEqual(len(self.graph["nodes"]), 403)
        self.assertTrue(all(node["chapter"] in leaf_ids for node in self.graph["nodes"]))

    def test_leaf_and_meta_counts_are_consistent(self) -> None:
        chapters = {chapter["id"]: chapter for chapter in self.graph["chapters"]}
        leaf_total = sum(
            chapter["count"]
            for chapter in chapters.values()
            if chapter["level"] == 2
        )
        self.assertEqual(leaf_total, len(self.graph["nodes"]))

        for meta in self.graph["meta_chapters"]:
            with self.subTest(meta=meta["id"]):
                child_total = sum(chapters[child]["count"] for child in meta["children"])
                self.assertEqual(meta["count"], child_total)

    def test_relationship_endpoints_still_exist(self) -> None:
        problem_ids = {node["id"] for node in self.graph["nodes"]}
        for edge in self.graph["edges"]:
            with self.subTest(edge=edge):
                self.assertIn(edge["source"], problem_ids)
                self.assertIn(edge["target"], problem_ids)


if __name__ == "__main__":
    unittest.main()
