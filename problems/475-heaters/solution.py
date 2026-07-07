class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ret = 0
        heaters.sort()
        n = len(heaters)
        for h in houses:
            pos = bisect.bisect_left(heaters, h)
            if pos == n:
                ret = max(ret, h - heaters[n-1])
            elif pos == 0:
                ret = max(ret, heaters[0] - h)
            else:
                ret = max(ret, min(heaters[pos] - h, h - heaters[pos-1]))
        return ret

'''
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ret = 0
        n = len(heaters)
        for h in houses:
            l, r = 0, n - 1
            if heaters[r] <= h: 
                ret = max(ret, h - heaters[r])
            elif heaters[l] >= h:
                ret = max(ret, heaters[l] - h)
            else:
                while l + 1 < r:
                    mid = (l+r) >> 1
                    if heaters[mid] >= h:
                        r = mid
                    else:
                        l = mid
                ret = max(ret, min(heaters[r] - h, h - heaters[l]))
        return ret
'''