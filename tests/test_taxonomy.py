from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import taxonomy


class TaxonomyTests(unittest.TestCase):
    def test_every_topic_maps_to_a_leaf(self) -> None:
        for topic, spec in taxonomy.TOPICS.items():
            with self.subTest(topic=topic):
                self.assertIn(spec.chapter, taxonomy.LEAF_CHAPTERS_BY_ID)

    def test_every_leaf_has_a_meta_parent(self) -> None:
        for leaf in taxonomy.LEAF_CHAPTERS:
            with self.subTest(chapter=leaf.id):
                self.assertIn(leaf.parent, taxonomy.META_CHAPTERS_BY_ID)

    def test_mixed_topic_precedence(self) -> None:
        cases = {
            ("array", "sliding-window"): "arrays",
            ("string", "sliding-window"): "strings",
            ("binary-tree", "dfs"): "binary-trees",
            ("graph", "bfs"): "graphs-and-traversal",
            ("dynamic-programming", "knapsack"): "knapsack-dp",
            ("divide-and-conquer", "sorting"): "divide-and-conquer",
        }
        for topics, expected in cases.items():
            with self.subTest(topics=topics):
                chapter, _ = taxonomy.classify(list(topics))
                self.assertEqual(chapter, expected)

    def test_meta_chapters_aggregate_only_their_children(self) -> None:
        leaf_ids = {leaf.id for leaf in taxonomy.LEAF_CHAPTERS}
        children = {
            child.id
            for meta in taxonomy.META_CHAPTERS
            for child in taxonomy.children_of(meta.id)
        }
        self.assertEqual(children, leaf_ids)


if __name__ == "__main__":
    unittest.main()
