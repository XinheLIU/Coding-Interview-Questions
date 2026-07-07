#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r:
            mid = (l + r) >> 1
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return l * l == num
# @lc code=end

'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = l + ((r-l) >> 1)
            val = mid * mid 
            if val == num:
                return True
            elif val > num:
                r = mid - 1
            else:
                l = mid + 1
'''
