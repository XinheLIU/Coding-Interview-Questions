class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def possible(D):
            return sum(int((stations[i + 1] - stations[i]) // D) for i in range(len(stations) - 1)) <= K
        
        l, r = 0, 10 ** 18
        while l + 1e-6 < r:
            mid = l + (r - l) / 2.0
            if possible(mid):
                r = mid
            else:
                l = mid
        return l