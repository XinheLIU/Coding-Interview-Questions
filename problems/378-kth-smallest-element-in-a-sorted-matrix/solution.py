class Solution:
    def kthSmallest(self, matrix, k):
        # write your code here
        l, r = matrix[0][0], matrix[-1][-1] 
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                l = mid 
            else:
                r = mid 
        if self.get_num_less_equal(matrix, l) >= k:
            return l
        return r         
            
    def get_num_less_equal(self, matrix, mid):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1 
                count += j + 1 
            else:
                j -= 1 
        return count