class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def count(mid):
            cnt = 0
            start = 0
            for i in range(n):
                while start < n and nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start # i - start pairs distance less and equal to mid
            return cnt
        l, r = 0, nums[n-1] - nums[0]
        while l < r:
            mid = l + ((r - l) >> 1)
            cnt = count(mid)
            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return r