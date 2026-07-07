#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, ret, out, start):
            ret.append(out)
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i-1]: 
                    dfs(nums, ret, out + [nums[i]], i + 1)
        ret = []
        if not nums: return ret
        dfs(sorted(nums), ret, [], 0)
        return ret
# @lc code=end

