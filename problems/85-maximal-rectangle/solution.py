#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (37.84%)
# Likes:    3066
# Dislikes: 71
# Total Accepted:    186.5K
# Total Submissions: 492K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        l, r, h = [0] * n, [n] * n, [0] * n # maximum left bound, right bound, height from each point
        maxarea = 0
        
        for i in range(m):
            cur_l, cur_r = 0, n
            
            # update r
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], cur_r)
                else:
                    cur_r = j
                    r[j] = n

            # update h, l
            for j in range(n):
                if matrix[i][j] == '1':
                    h[j] += 1
                    l[j] = max(l[j], cur_l)
                else:
                    h[j] = 0
                    l[j] = 0
                    cur_l = j + 1
                # update maxarea
                maxarea = max(maxarea, h[j] * (r[j]-l[j]))
                
        return maxarea
# @lc code=end

'''
# histogram solution

    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, res = [-1], 0
        for i in range(len(heights)):
            # an increasing stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        # look at rectangles rowwise
        heights, res = [0] * n , 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            res = max(res, self.largestRectangleArea(heights))
        return res
’''  