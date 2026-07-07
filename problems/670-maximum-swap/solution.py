#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(map(int, str(num)))
        last = {v: i for i, v in enumerate(A)}
        for i, v in enumerate(A):
            for d in range(9, v, -1):
                j = last.get(d, -1)
                if j > i:
                    A[i], A[j] = A[j], A[i]
                    return int("".join(map(str,A)))
        return num
# @lc code=end

