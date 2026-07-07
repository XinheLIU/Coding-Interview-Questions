#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        # dp[:i] can be split successfully or not
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
# @lc code=end
'''
# dfs
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(s, wordDict, start):
            print(memo, start)
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for end in range(start, len(s) + 1):
                if s[start: end] in wordDict and dfs(s, wordDict, end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return dfs(s, set(wordDict), 0)
'''
'''
# bfs
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        q = collections.deque()
        visited = set()
        q.append(0)
        while q:
            start = q.popleft()
            if start not in visited:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        q.append(end)
                        if end == len(s):
                            return True
                visited.add(start)
        return False
'''

