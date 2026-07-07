class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # one pass swap
        if not nums or len(nums) < 2: return nums
        for i in range(len(nums) - 1):
            if (i & 1 == 0 and nums[i] > nums[i + 1]) or (i & 1 == 1 and nums[i] < nums[i+ 1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]