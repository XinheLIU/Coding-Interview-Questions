class Solution(object):
  def solve(self, array):
    """
    input: int[] array
    return: int[]
    """
    # move the smallest to left most place
    for i in range(0, len(array)):
      min_ind = i
      for j in range(i + 1, len(array)):
           if array[j] < array[min_ind]:
               min_ind = j
      if min_ind != i:
          array[i], array[min_ind] = array[min_ind], array[i]
    return array