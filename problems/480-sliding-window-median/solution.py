#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (34.20%)
# Likes:    586
# Dislikes: 60
# Total Accepted:    36.7K
# Total Submissions: 105.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples: 
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5 
# 
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position. Your
# job is to output the median array for each window in the original array.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# 
# 
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7       3
# ⁠1  3  -1  -3 [5  3  6] 7       5
# ⁠1  3  -1  -3  5 [3  6  7]      6
# 
# 
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
# 
# Note: 
# You may assume k is always valid, ie: k is always smaller than input array's
# size for non-empty array.
#

# @lc code=start
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
            max_heap, min_heap, ret = [], [], []

            for i, v in enumerate(nums[:k]):
                heapq.heappush(max_heap, (-v, i))
            
            for i in range(k - k // 2):
                popped = heapq.heappop(max_heap)
                heapq.heappush(min_heap, (-popped[0],
                                            popped[1]))
            # print(max_heap, min_heap)
            ret.append(min_heap[0][0] if k % 2 else
                                   (-max_heap[0][0] + min_heap[0][0]) / 2)
            # now rolling update both heaps
            for i, v in enumerate(nums[k:], k):
                # update
                if v >= min_heap[0][0]:
                    heapq.heappush(min_heap, (v, i))
                    if nums[i - k] <= min_heap[0][0]:
                        heapq.heappush(max_heap, (-min_heap[0][0], min_heap[0][1]))
                        heapq.heappop(min_heap)
                else:
                    heapq.heappush(max_heap, (-v, i))
                    if nums[i - k] >= min_heap[0][0]:
                        heapq.heappush(min_heap, (-max_heap[0][0], max_heap[0][1]))
                        heapq.heappop(max_heap)
                # delete out of window keys in the last step
                while max_heap and max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                while min_heap and min_heap[0][1] <= i - k:
                    heapq.heappop(min_heap)
                ret.append(min_heap[0][0] if k % 2 else
                                       (-max_heap[0][0] + min_heap[0][0]) / 2)

            return ret
# @lc code=end
'''
# binary search approach
class Solution(object):
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        if n == 0:
            return []
        arr = []
        [arr.insert(bisect.bisect_left(arr, v), v) for v in nums[:k]]
        res = [self.getMedian(arr)]
        i = 0
        for v in nums[k:]:
            index = bisect.bisect_left(arr, nums[i])
            arr = arr[:index] + arr[index+1:]
            index = bisect.bisect_left(arr, v)
            arr.insert(index, v)
            i += 1
            res.append(self.getMedian(arr))
        return res

    def getMedian(self, arr):
        n = len(arr)
        return (arr[n//2]+arr[n//2-1]) / 2.0 if n % 2 == 0 else arr[n//2] * 1.0

'''