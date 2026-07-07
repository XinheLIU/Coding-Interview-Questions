class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not len(matrix):
            return matrix
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ret = []
        direct = 0 # 0: right, 1: down, 2: left, 3: up
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    ret.append(matrix[up][i])
                up += 1
            elif direct == 1:
                for i in range(up, down + 1):
                    ret.append(matrix[i][right])
                right -= 1
            elif direct == 2:
                for i in range(right, left - 1, -1):
                    ret.append(matrix[down][i])
                down -= 1
            elif direct == 3:
                for i in range(down, up - 1, -1):
                    ret.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return ret
            direct = (direct + 1) % 4
            