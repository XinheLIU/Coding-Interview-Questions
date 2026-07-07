#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        nrow, ncol = len(matrix), len(matrix[0])
        row, col = 0, ncol - 1
        while row < nrow and col >= 0:
            val = matrix[row][col]
            if  val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False 
# @lc code=end

