class Solution:
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans



"""
    def generateParenthesis(self, n):
        self.list = []
        self._gen(n, 0, 0, "")
        return self.list
    
    def _gen(self, n, left, right, result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(n, left + 1, right, result + "(")
        if right < n and right < left:
            self._gen(n, left, right + 1, result + ")")
"""