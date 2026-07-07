class WordDistance:

    def __init__(self, words: List[str]):
        self.loc = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.loc[w].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        ret = float('inf')
        l1, l2 = self.loc[word1], self.loc[word2]
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            ret = min(ret, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return ret

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)