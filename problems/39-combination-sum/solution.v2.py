class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(res, candidates, target, start, out):
            if sum(out) == target:
                res.append(out[:])
                return
            if sum(out) > target:
                return
            for i in range(start, len(candidates)):
                out.append(candidates[i])
                dfs(res, candidates, target, i, out)
                out.pop()
        res = []
        dfs(res, candidates, target, 0, [])
        return res
"""
class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        self.res = []
        if not candidates or len(candidates) < 0: return self.res
        self.helper([], candidates, target, 0)
        return self.res
    
    def helper(self, temp, candidates, target, start):
        if target == 0:
            self.res.append(temp[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.helper(temp, candidates, target - candidates[i], i)
            temp.pop()
"""