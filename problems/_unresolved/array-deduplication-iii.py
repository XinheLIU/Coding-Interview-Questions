'''
Given a sorted integer array, remove duplicate elements. For each group of elements with the same value do not keep any of them. Do this in-place, using the left side of the original array and and maintain the relative order of the elements of the array. Return the array after deduplication.

Assumptions

The given array is not null
Examples

{1, 2, 2, 3, 3, 3} → {1}
'''
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    if not array or len(array) <= 2:
      return array
    i, j, cnt = 0, 0, 0
    while j < len(array):
      if array[i] == array[j]:
        j += 1
        cnt += 1
      else:
        if cnt == 1:
          i += 1
        array[i] = array[j]
        cnt = 0
    end = i + 1 if cnt == 1 else i
    return(array[:end])