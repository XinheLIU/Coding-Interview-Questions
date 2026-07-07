#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (45.92%)
# Likes:    597
# Dislikes: 21
# Total Accepted:    22K
# Total Submissions: 47.5K
# Testcase Example:  '3\n3\n5'
#
# 
# Nearly every one have used the Multiplication Table. But could you find out
# the k-th smallest number quickly from the multiplication table?
# 
# 
# 
# Given the height m and the length n of a m * n Multiplication Table, and a
# positive integer k, you need to return the k-th smallest number in this
# table.
# 
# 
# Example 1:
# 
# Input: m = 3, n = 3, k = 5
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 3    6    9
# 
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# 
# 
# 
# 
# Example 2:
# 
# Input: m = 2, n = 3, k = 6
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# 
# 
# 
# 
# Note:
# 
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]
# 
# 
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def enough(x):
            count = 0
        # the ith row looks like 
        # [i, 2*i, 3*i, ..., n*i]
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k
        
        l, r = 1, m * n
        while l < r:
            mid = l + ((r - l) >> 1)
            if not enough(mid):
                l = mid + 1
            else:
                r = mid
        return r 
# @lc code=end
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def count_lessq(mid):
            cnt = 0
            i, j = m, 1
            while i >= 1 and j <= n:
                t = j
                if mid > n * i:
                    j = n + 1
                else:
                    j = mid // i + 1
                cnt += (j - t) * i
                i = mid // j
            return cnt
        
        l, r = 1, m * n
        while l < r:
            mid = l + ((r - l) >> 1)
            cnt = count_lessq(mid)
            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return r 
'''

