class Solution:
    # dynamic programming
    def isMatch(self, s, p):
        #dp[i][j] indicates if s[0,i) matches p[0,j)
        if s == p:
            return True
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if j > 1 and p[j - 1] == "*":
                    # zero occurance
                    dp[i][j] = (dp[i][j - 2] or  
                        (i > 0 and (s[i-1] == p[j-2] or p[j-2] == ".") and dp[i-1][j])) #one or more occurance
                else:
                    dp[i][j] =  (i > 0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")) #one or more occurance
        return dp[m][n]

    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ### solve by recursion
        ## stop condition
        if not p:
            return (not s)
        # handle *:
        if len(p) >= 2 and p[1] == "*":
        # can have 0 char before * or 1 or more char before *
            return (self.isMatch1(s, p[2:]) or  (len(s) > 0 and (s[0] == p[0] or p[0] == ".") and self.isMatch1(s[1:],p)))
        else:
            return len(s) > 0 and (s[0] == p[0] or p[0] == ".") and self.isMatch1(s[1:],p[1:])