class Solution:
    def longestLine(self, M):
        if not M or not len(M):
            return 0
        n, m = len(M), len(M[0])
        ret = 0
        dp = [[[0]*4 for i in range(0, m)] for j in range(0, n)]
        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                if i - 1 >= 0:
                    dp[i][j][0] += dp[i - 1][j][0]
                if j - 1 >= 0:
                    dp[i][j][1] += dp[i][j - 1][1]
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j][2] += dp[i - 1][j - 1][2]
                if i - 1 >= 0 and j + 1 < m:
                    dp[i][j][3] += dp[i - 1][j + 1][3]
                ret = max(ret, max(dp[i][j][0], dp[i][j][1]))
                ret = max(ret, max(dp[i][j][2], dp[i][j][3]))
        return ret

"""
class Solution:
    def longestLine(self, M):
        if not M or not len(M):
            return 0
        m, n = len(M), len(M[0])
        dirs = ((0, 1), (1, 0),(-1, 1), (1, 1))
        ret = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    for d in dirs:
                        x, y = i, j 
                        cnt = 0
                        while (x >= 0 and x < m and y >= 0 and y < n) and  M[x][y] == 1:
                            x = x + d[0]
                            y = y + d[1]
                            cnt += 1
                        ret = max(ret, cnt)
        return ret
"""