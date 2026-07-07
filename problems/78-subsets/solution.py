#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, out, ret, start):
            ret.append(out)
            for i in range(start, len(nums)):
                dfs(nums, out + [nums[i]], ret, i + 1)
        if not nums:
            return []
        ret = []
        dfs(nums, [], ret, 0)
        return ret

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, 0, [])
        return self.res
      
    def helper(self, nums, start, out):
        self.res.append(out[:])
        for i in range(start, len(nums)):
            self.helper(nums, i + 1, out + [nums[i]])
'''
# @lc code=end

