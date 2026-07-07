"""
Determine if there exists three elements in a given array that sum to the given target number. Return all the triple of values that sums to target.

Assumptions

The given array is not null and has length of at least 3
No duplicate triples should be returned, order of the values in the tuple does not matter
Examples

A = {1, 2, 2, 3, 2, 4}, target = 8, return [[1, 3, 4], [2, 2, 4]]

"""
class Solution(object):
  def allTriples(self, nums, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    nums.sort()
    ret = []
    n = len(nums)
    for i in range(n-2):
      if nums[i] > target:
        break
      # no duplicates
      if i and nums[i] == nums[i-1]:
        continue
      t = target - nums[i]
      l, r = i + 1, n - 1
      while l < r:
        if nums[l] + nums[r] == t:
          ret.append([nums[i], nums[l], nums[r]])
          r -= 1
          l += 1
          while l < r and nums[l] == nums[l-1]: l+= 1
          while l < r and nums[r] == nums[r+1]: r-=1
        elif nums[l] + nums[r] > t:
          r -= 1
        else:
          l += 1
    return ret