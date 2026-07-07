class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not len(matrix):
            return
        # is the first col needs to be set to zero
        is_col = False
        r,c = len(matrix), len(matrix[0])
        # loop by rows
        # If an element is zero, we set the first element of the corresponding row and column to 0
        for i in range(r):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, c):
                if matrix[i][j]  == 0:
                    matrix[0][j], matrix[i][0] = 0, 0
        # set to zeros
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(1, c):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(r):
                matrix[i][0] = 0