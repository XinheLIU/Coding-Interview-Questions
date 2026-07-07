class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(S, n, out, res):
            if n == len(S):
                res.append(out)
                return
            if S[n].isalpha():
                dfs(S, n + 1, out + S[n].upper(), res)
                dfs(S, n + 1, out + S[n].lower(), res)
            else:
                 dfs(S, n + 1, out + S[n].upper(), res)       
        res = []
        dfs(S, 0, '', res)
        return res