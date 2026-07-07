#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(ret, out, nums):
            if not nums:
                ret.append(out)
                return
            for i in range(len(nums)):
                dfs(ret, out + [nums[i]], nums[:i] + nums[i+1:])
        ret = []
        dfs(ret, [], nums)
        return ret
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, ret, out, visited):
            if len(out) == len(nums):
                ret.append(out)
                return
            for i, v in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                dfs(nums, ret, out + [v], visited)
                visited[i] = False
        ret = []
        dfs(nums, ret, [], [False for _ in nums])
        return ret
'''
# @lc code=end

