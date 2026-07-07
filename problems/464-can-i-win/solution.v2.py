class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # total sum
        if (maxChoosableInteger + 1) * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        
        def dfs(nums, desiredTotal, memo):
            hash = str(nums)
            if hash in memo:
                return memo[hash]
            if nums[-1] >= desiredTotal:
                return True
            for i in range(len(nums)):
                if not dfs(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                    memo[hash] = True
                    return True
            memo[hash] = False
            return False
        
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

"""
class Solution:

    def canIWin(self, maxChoosableInteger, desiredTotal):
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

    def helper(self, nums, desiredTotal):

        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False
"""