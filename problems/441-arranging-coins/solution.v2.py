class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1: return n
        l, r = 1, n
        while l < r:
            mid = l +((r - l) >> 1)
            if mid * (mid + 1) // 2 <= n:
                l = mid + 1
            else:
                r = mid
        return l - 1