class Solution(object):
  def bubble_sort(self, array):
    """
    array: list to sort
    return: array (list)
    """
    if not array:
      return array
    for i in range(1,len(array)):
      for j in range(len(array)-i):
        if array[j] > array[j+1]:
          array[j], array[j+1] = array[j+1], array[j]
    return array