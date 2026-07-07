class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first upside down, then swap symmetry
        # if anti-clockwise, first left to right reverse, then swap symmetry
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
'''  
  def rotate(self, matrix):
    """
    input: int[][] matrix
    return: No need to return
    """
    # many methods
    n = len(matrix)
    for i in range(n):
      for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
      matrix[i].reverse()
'''