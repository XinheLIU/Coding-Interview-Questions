class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    sum1, sum2 = sum(range(N+1)), sum(nums)
    return(sum1 - sum2)