class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(k):
            return sum((p - 1) // k + 1 for p in piles) <= H
    
        l, r = 1, max(piles)
        while l < r:
            mid = l + ((r - l) >> 1)
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l