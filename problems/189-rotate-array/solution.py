#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n 
        i, count = 0, 0
        while count < n:
            pos = (i + k) % n
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1
# @lc code=end           

'''
class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, start = len(nums), 0
        while n and k % n:
            k %= n
            for i in range(k):
                nums[i + start], nums[n - k + i + start] = nums[n- k + i + start], nums[i + start]
            n -= k
            start += k
'''
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
'''
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        ret = [0] * n
        for i, v in enumerate(nums):
            ret[(i+k) % n] = v
        for i in range(n):
            nums[i] = ret[i]
'''