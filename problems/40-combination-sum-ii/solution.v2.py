class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        def dfs(start, out):
            if sum(out) == target:
                res.append(out[:])
                return
            elif sum(out) > target: return
            else:
                for i in range(start, n):
                    if i > start and candidates[i] == candidates[i-1]: continue
                    dfs(i+1, out + [candidates[i]])
        res = []
        dfs(0, [])
        return res