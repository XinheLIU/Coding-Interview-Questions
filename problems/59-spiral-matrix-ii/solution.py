#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        count = 1
        direct = 0 # 0: right, 1 : down, 2: left 3: up
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    matrix[up][i] = count 
                    count += 1
                up += 1
            elif direct == 1:
                for i in range(up, down + 1):
                    matrix[i][right] = count
                    count += 1
                right -= 1
            elif direct == 2:
                for i in range(right, left - 1, -1):
                    matrix[down][i] = count
                    count += 1
                down -= 1
            elif direct == 3:
                for i in range(down, up - 1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
            if up > down or left > right:
                return matrix
            direct = (direct + 1) % 4
# @lc code=end

