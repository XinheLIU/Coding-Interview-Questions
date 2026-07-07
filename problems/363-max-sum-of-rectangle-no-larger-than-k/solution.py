class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        MIN = -9999999
        ret = MIN
        for i in range(n):
            Sum = [0 for _ in range(m)]
            for j in range(i, n):   # loop horizontally (by column)
                for r in range(m):
                    Sum[r] += matrix[r][j] # row sum for column i to j
                sumSet, curMax = [0], MIN
                cumSum = 0
                for r in range(m):
                    cumSum += Sum[r]
                    pos = bisect.bisect_left(sumSet, cumSum - k) # binary search vertically (by row)
                    if pos != len(sumSet):
                        curMax = max(curMax, cumSum - sumSet[pos])
                    bisect.insort_left(sumSet, cumSum)
                ret = max(ret, curMax)
        return ret