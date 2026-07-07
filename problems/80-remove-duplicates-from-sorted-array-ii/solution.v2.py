class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)
        i, j, cnt = 0, 1, 1
        while j < len(nums):
            if nums[i] == nums[j] and cnt == 0:
                j += 1
            else:
                if nums[i] == nums[j]:
                    cnt -= 1
                else:
                    cnt = 1
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
        
'''
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    i, cnt = 0, 1
    for j in range(1, len(array)):
      if array[j] == array[i] and cnt == 0:
        continue
      else:
        if array[i] == array[j]:
          cnt -= 1
        else:
          cnt = 1
      i += 1
      array[i] = array[j]   
    return(array[:i+1])
'''