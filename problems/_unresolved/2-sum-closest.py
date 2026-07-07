'''
Find the pair of elements in a given array that sum to a value that is closest to the given target number. Return the values of the two numbers.

Assumptions

The given array is not null and has length of at least 2
Examples

A = {1, 4, 7, 13}, target = 7, closest pair is 1 + 7 = 8, return [1, 7].

'''
class Solution(object):
  def closest(self, nums, target):
    """
    input: int[] array, int target
    return: Integer[]
    """
    if not nums or len(nums) < 2:
      return []
    nums.sort()
    diff = float('inf')
    l, r = 0, len(nums) - 1
    while l < r:
      Sum = nums[l] + nums[r]
      new_diff = abs(Sum - target)
      if new_diff < diff:
        diff, ret = new_diff, [nums[l], nums[r]]
      if Sum < target:
        l += 1
      elif Sum > target:
        r -= 1
      else:
        return [nums[l], nums[r]]
    return ret