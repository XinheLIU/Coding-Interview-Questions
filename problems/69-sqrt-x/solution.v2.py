#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        # binary search
        l, r = 1, x
        while l < r:
            mid = l + (r-l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                r = mid 
            else:
                l = mid 
# @lc code=end
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton's method
        # f(r) = r ^ 2 - x = 0, r_n+1 = r_n - f(r)/f`(r) = r_n - (r_n^2-x)/2r_n = r_n/2 + x/2_rn
        r = x
        while r * r > x:
            r = (r + x/r) / 2
        return r
'''
'''
class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l + 1 < r:
            mid = l + (r-l) // 2
            if mid * mid < x:
                l = mid
            else:
                r = mid
        if r * r <= x:
            return int(r)
        return int(l)
'''
'''
class Solution:
	def mySqrt(self, x):
        i, j = 0, x / 2 + 1
        while i <= j:
        mid = (i + j) / 2
        cur = mid ** 2
        if cur == x:
            return mid
        elif cur < x:
            i = mid + 1
        else:
            j = mid - 1
        return (i + j) / 2
'''
