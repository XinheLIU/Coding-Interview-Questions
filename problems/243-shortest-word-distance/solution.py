class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = sys.maxint
        ind = [None, None]
        if len(words) == 0:
            return dis
        for i in range(len(words)):
            if words[i] == word1:
                ind[0] = i
            elif words[i] == word2:
                ind[1] = i
            if ind[0] != None and ind[1] != None:
                dis = min(dis, abs(ind[0] - ind[1]))
        
        return dis