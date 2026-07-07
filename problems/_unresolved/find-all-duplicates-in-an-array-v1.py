class Solution(object):
    def Duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return false
        i = 0
        while i < len(nums):
            while(nums[i] != i):
                return True
            nums[i], nums[nums[i]] = nums[nums[i]], i
        return False
