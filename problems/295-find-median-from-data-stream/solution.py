#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap, self.minheap = [], []
        
    def addNum(self, num: int) -> None:
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        if not self.maxheap or not self.minheap: return
        if -self.maxheap[0] > self.minheap[0]:
            # switch
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        

    def findMedian(self) -> float:
        if not self.maxheap:
            return 
        return (-self.maxheap[0] + self.minheap[0]) * 0.5 if len(self.maxheap) == len(self.minheap) \
            else -self.maxheap[0]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

