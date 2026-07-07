#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(s, p):
            if (s, p) not in memo:
                if p == s or p == "*":
                    ret = True
                elif p == "" or s == "":
                    ret = False
                elif p[0] == s[0] or p[0] == "?":
                    ret = dp(s[1:], p[1:])
                elif p[0] == '*':
                    ret = dp(s, p[1:]) or dp(s[1:], p)
                else:
                    ret = False
                memo[s,p] = ret
            return memo[s, p]
        
        p = self.remove_duplicate_stars(p)
        return dp(s, p)
     
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 
# @lc code=end

