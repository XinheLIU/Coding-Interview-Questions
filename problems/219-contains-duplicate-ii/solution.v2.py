class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i, v in enumerate(nums):
            if v in m:
                j = m[v]
                if i - j <= k:
                    return True
            m[v] = i
        return False 