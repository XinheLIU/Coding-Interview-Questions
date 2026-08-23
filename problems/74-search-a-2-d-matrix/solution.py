#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) >> 1
            # Map 1D index to 2D matrix coordinates
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
        
# @lc code=end