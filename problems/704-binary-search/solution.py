
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[r] == target:
            return r
        elif nums[l] == target: 
            return l
        else:
            return -1
'''