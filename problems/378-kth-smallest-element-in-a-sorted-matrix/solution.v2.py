class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        def count_less_equal(mid):
            i, j = 0, n - 1
            count = 0
            while i < m and j >= 0:
                if matrix[i][j] <= mid:
                    count += j + 1
                    i += 1
                else:
                    j -= 1
            return count
                
        l, r = matrix[0][0], matrix[m-1][n-1]
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            cnt = count_less_equal(mid) # note: mid may not exist
            if  cnt < k:
                l = mid
            else:
                r = mid
        if count_less_equal(l) >= k:
            return l
        else:
            return r