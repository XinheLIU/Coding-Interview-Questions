class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1  
        return i
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j, v in enumerate(nums):
            if v != val:
                nums[i] = nums[j]
                i += 1
        return i
"""