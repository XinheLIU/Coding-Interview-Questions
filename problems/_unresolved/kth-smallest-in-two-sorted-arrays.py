"""
Given two sorted arrays of integers, find the Kth smallest number.

Assumptions

The two given arrays are not null and at least one of them is not empty

K >= 1, K <= total lengths of the two sorted arrays

Examples

A = {1, 4, 6}, B = {2, 3}, the 3rd smallest number is 3.

A = {1, 2, 3, 4}, B = {}, the 2nd smallest number is 2.
"""
class Solution(object):
  def kth(self, a, b, k):
    """
    input: int[] a, int[] b, int k
    return: int
    """
    if not a:
      return b[k-1]
    if not b:
      return a[k-1]
    if k == 1:
      return min(a[0], b[0])
    i = min(k // 2, len(a))
    j =  min(k - i, len(b))
    if a[i-1] > b[j-1]:
      return self.kth(a, b[j:], k - j)
    else:
      return self.kth(a[i:], b, k - i)