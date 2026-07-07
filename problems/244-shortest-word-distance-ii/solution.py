class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = {}
        self.l = len(words)
        for index, value in enumerate(words):
            self.dic[value] = self.dic.get(value, []) + [index] # dictionary.get()，可以传入一个参数。如果传入两个参数，第二个参数就是default值，如果字典中找不到的话，就返回default值。

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.dic[word1], self.dic[word2]
        i = j = 0
        res = self.l
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j])) # loop all the l1 and l2 to find the shortest
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res