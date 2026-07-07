'''
Find all pairs of elements in a given array that sum to the given target number. Return all the pairs of indices.

Assumptions

The given array is not null and has length of at least 2.

Examples

A = {1, 3, 2, 4}, target = 5, return [[0, 3], [1, 2]]

A = {1, 2, 2, 4}, target = 6, return [[1, 3], [2, 3]]

'''
class Solution(object):
  def allPairs(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    map = dict()
    ret = []
    for i, num in enumerate(array):
      # seen what happened
      if (target - num) in map:
        for j in map[target - num]:
          ret.append([j, i])
      # put in map
      if num not in map:
        map[num] = [i]
      else:
        map[num] = map[num] + [i]
    return ret