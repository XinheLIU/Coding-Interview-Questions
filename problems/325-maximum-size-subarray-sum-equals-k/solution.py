class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum, ret = 0, 0
        m = {0:-1}
        for i, v in enumerate(nums):
            sum += v
            if sum - k in m:
                ret = max(ret, i - m[sum - k])
            if sum not in m: # first occurance
                m[sum] = i
        return ret