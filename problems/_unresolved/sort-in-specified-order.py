'''
Given two integer arrays A1 and A2, sort A1 in such a way that the relative order among the elements will be same as those are in A2.

For the elements that are not in A2, append them in the right end of the A1 in an ascending order.

Assumptions:

A1 and A2 are both not null.
There are no duplicate elements in A2.
Examples:

A1 = {2, 1, 2, 5, 7, 1, 9, 3}, A2 = {2, 1, 3}, A1 is sorted to {2, 2, 1, 1, 3, 5, 7, 9}

'''
import collections
class Solution(object):
  def sortSpecial(self, A1, A2):
    """
    input: int[] A1, int[] A2
    return: int[]
    """
    # bucket sort
    cnt = collections.Counter(A1)
    remain, res = [], []   
    print remain
    for i in A2:
      while cnt[i] > 0:
        res.append(i)
        cnt[i] -= 1
    for i in A1:
      if cnt[i] > 0:
        remain.append(i)
    remain.sort() 
    return(res + remain)