class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        def lis(nums):
            dp = []
            for i in range(len(nums)):
                pos = bisect.bisect_left(dp, nums[i])
                if pos == len(dp):
                    dp.append(nums[i])
                else:
                    dp[pos] = nums[i]
            return len(dp)
        
        return lis(list(e[1] for e in envelopes))