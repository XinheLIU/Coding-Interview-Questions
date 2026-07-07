import random
class Solution(object):
  def quickSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    self.helper(array, 0, len(array) - 1)
    return array

  def helper(self, array, l, r):
      if l < r:
        pivot = self.partition(array, l, r)
        self.helper(array, l, pivot - 1)
        self.helper(array, pivot + 1, r)

  def partition(self, array, l, r):
      # find a pivot
      rand = random.randint(l,r)
      # swap the pivot to the right
      array[rand], array[r] = array[r], array[rand]
      i, pivot = l-1, array[r]
      # i is at the left of pivot
      for j in range(l,r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
      # put the pivot in place
      array[i+1], array[r] = array[r], array[i+1]
      return i+1
'''
# More explicit method
class Solution(object):
  
  def quickSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    def partition(array, start, end, pivot_index):
      array[end], array[pivot_index] = array[pivot_index], array[end]
      pivot = array[end]
      store_index = start
      for i in range(start, end):
        if array[i] < pivot:
          array[i], array[store_index] = array[store_index], array[i]
          store_index += 1
      array[end], array[store_index] = array[store_index], array[end]
      return store_index

    def quick_sort(array, start, end):
      from random import randrange
      if start >= end:
        return
      pivot_index = randrange(start, end + 1)
      new_pivot_index = partition(array, start, end, pivot_index)
      quick_sort(array, start, new_pivot_index - 1)
      quick_sort(array, new_pivot_index + 1, end)

    quick_sort(array, 0, len(array) - 1)
    return array
'''