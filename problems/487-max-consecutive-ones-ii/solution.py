class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        l = 0
        K = 1
        zeros = 0
        q = collections.deque() # record the index of 0s
        for r, v in enumerate(nums):
            if v == 0:
                q.append(r)
                zeros += 1
            while zeros > K:
                l = q.popleft() + 1
                zeros -= 1
            ret = max(ret, r - l + 1)
        return ret      
'''
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        can_still_flip, no_more_flips, max_ones = 0, 0, 0
        
        for num in nums:
            
            if num == 1:
                can_still_flip += 1 
                no_more_flips += 1
            else:
                can_still_flip += 1 
                no_more_flips, can_still_flip = can_still_flip, 0
                
            max_ones = max(max_ones, can_still_flip, no_more_flips)

        return max_ones
'''