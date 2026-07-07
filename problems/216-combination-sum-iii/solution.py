class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(res, start, out):
            if sum(out) == target:
                res.append(out[:])
                return
            if sum(out) > target:
                return
            for i in range(start, len(candidates)):
                dfs(res, i, out + [candidates[i]])
        res = []
        dfs(res, 0, [])
        return res