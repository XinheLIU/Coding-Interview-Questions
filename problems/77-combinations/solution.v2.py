#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(ret, out, n, k, start):
            if len(out) == k:
                ret.append(out)
                return
            for i in range(start, n + 1):
                dfs(ret, out + [i], n, k, i + 1)
        ret = []
        dfs(ret, [], n, k, 1)
        return ret
# @lc code=end

