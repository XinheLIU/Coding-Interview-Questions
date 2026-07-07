#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        if not nums: return ret
        window = deque()
        for i, v in enumerate(nums):
            if i >= k and window[0] <= (i-k):
                window.popleft()
            while window and nums[window[-1]] <= v:
                window.pop()
            window.append(i)
            if i >= k - 1:
                ret.append(nums[window[0]])
        return ret
# @lc code=end

'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列
        if k == 0:
            return None
        if k == 1:
            return nums
        deq = deque()
        deq.append(nums[0])
        output = []
        for i in range(1, k):
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
        output.append(deq[0])
        for i in range(k, len(nums)):
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(nums[i])
            if deq[0] == nums[i-k]:
                deq.popleft()
            output.append(deq[0])
        return output
'''