#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # nums[i] - nums[j] <= t <=> nums[i] /t - nums[j]/t <= 1
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case, we only need to check the same bucket
            bucketKey, offset = (v // t, 1) if t != 0 else (v, 0)
            for key in range(bucketKey - offset, bucketKey + offset + 1):
                if key in buckets and abs(buckets[key] - v) <= t:
                    return True
            # keep the recent most nums[i] is ok
            buckets[bucketKey] = v
            # get rid of too far away buckets
            if len(buckets) > k:
                del buckets[nums[i-k] // t if t!= 0 else nums[i-k]]
        return False
# @lc code=end
'''
Other solutions
1. Directly Search
2. Maintain a balanced tree window set
'''

