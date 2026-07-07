class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(n, k, start, out, res, s):
            if len(out) == k and s == 0:
                res.append(out[:])
                return
            for i in range(start, 10):
                out.append(i)
                dfs(n, k,  i + 1, out, res, s - i)
                out.pop()
        res = []
        dfs(n, k, 1, [], res, n)
        return res