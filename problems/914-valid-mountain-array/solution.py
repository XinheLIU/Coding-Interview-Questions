class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, n = 0, len(A)
        while i < n + 1 and A[i] < A[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        # walk down 
        while i + 1 < n and A[i] > A[i+1]:
            i += 1
        return i  == n-1