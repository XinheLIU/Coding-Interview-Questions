class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # sort it in place
    for i in range(1, len(array)):
      cur, k = array[i], i
      # before k (0 to k-1) all sorted
      while k > 0 and array[k-1] > cur:
        array[k] = array[k-1]
        k -= 1
      array[k] = cur
    return array
       
'''
import bisect
class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    new_array = []
    for i in range(len(array)):
      k = bisect.bisect_right(new_array, array[i])
      new_array.insert(k, array[i])
    return new_array
'''