class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + ((r-l) >> 1)
            # left is sorted
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target: return l
        elif nums[r] == target: return r
        return -1