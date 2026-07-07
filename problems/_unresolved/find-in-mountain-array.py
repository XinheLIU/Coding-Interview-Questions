# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
		# find the index of the peak
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) >> 1
            a, b, c = mountain_arr.get(mid - 1), mountain_arr.get(mid), mountain_arr.get(mid + 1)
            if a < b and b < c:
                l = mid
            elif a > b and b > c:
                r = mid
            else:
                peak = mid
                break
        
        if target > mountain_arr.get(peak) or target < min(mountain_arr.get(0), mountain_arr.get(n - 1)):
            return -1
        
		# find whether target is in the left of the peak
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            tmp = mountain_arr.get(mid)
            if target < tmp:
                r = mid - 1
            elif target > tmp:
                l = mid + 1
            else:
                return mid
    
		# find whether target is in the right of the peak
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            tmp = mountain_arr.get(mid)
            if target < tmp:
                l = mid + 1
            elif target > tmp:
                r = mid - 1
            else:
                return mid
        return -1