class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = None, None
        pre = None
        ret = len(words)
        for i, w in enumerate(words):
            if w == word1:
                pre = p1
                p1 = i
            elif w == word2:
                p2 = i
            if p1 is not None:
                if word1 == word2 and pre is not None:
                    ret = min(ret, abs(p1 - pre))
                elif p2 is not None:
                    ret = min(ret, abs(p1 - p2))
        return ret