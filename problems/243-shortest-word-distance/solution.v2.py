class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = None, None
        ret = len(words)
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i
            if p1 is not None and p2 is not None:
                ret = min(ret, abs(p1 - p2))
        return ret