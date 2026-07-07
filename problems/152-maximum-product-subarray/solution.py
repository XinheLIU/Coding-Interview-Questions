class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = nums[0] if nums else 0
        dp_max, dp_min = [0] * 2, [0] * 2
        dp_max[0], dp_min[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp_max[x] = max(nums[i], dp_max[y] * nums[i], dp_min[y] * nums[i])
            dp_min[x] = min(nums[i], dp_max[y] * nums[i], dp_min[y] * nums[i])
            ret = max(ret, dp_max[x])
        return ret