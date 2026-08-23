#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l, r = 0, x // 2
        while l <= r:
            mid = (l + r) >> 1
            if mid*mid == x: return mid
            elif mid*mid < x: l = mid + 1
            else: r = mid-1
        return r

# @lc code=end
