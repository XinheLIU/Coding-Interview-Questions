'''
Find all pairs of elements in a given array that sum to the pair the given target number. Return all the distinct pairs of values.

Assumptions

The given array is not null and has length of at least 2
The order of the values in the pair does not matter
Examples

A = {2, 1, 3, 2, 4, 3, 4, 2}, target = 6, return [[2, 4], [3, 3]]

'''
class Solution(object):
  def allPairs(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    ret = []
    if not array or len(array) < 2:
      return ret
    array.sort()
    l, r = 0, len(array) -1
    while l < r:
      if array[l] == array[l+1]:
        if array[l] + array[l+1] == target:
          ret.append([array[l],array[l+1]])
        while array[l] == array[l+1]:
          l += 1
      if array[r] == array[r-1]:
        if array[r-1] + array[r] == target:
           ret.append([array[r-1],array[r]])
        while array[r] == array[r-1]:
          r -= 1
      if array[l] + array[r] == target:
        ret.append([array[l], array[r]])
        l += 1
      elif array[l] + array[r] < target:
        l += 1
      else:
        r -= 1
    return ret