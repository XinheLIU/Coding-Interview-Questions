class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = 0
        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum < target:
                    ret += r - l
                    l += 1
                else:
                    r -= 1
        return ret