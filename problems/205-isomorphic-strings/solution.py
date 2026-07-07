class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, map1, map2 = len(s), [-1] * 256, [-1] * 256
        if len(t) != n:
            return False
        for i in range(n):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False
            # record last appearance
            map1[ord(s[i])], map2[ord(t[i])] = i, i
        return True