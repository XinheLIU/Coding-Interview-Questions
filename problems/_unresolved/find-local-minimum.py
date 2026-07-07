"""
Given an unsorted integer array, return any of the local minimum's index.

An element at index i is defined as local minimum when it is smaller than all its possible two neighbors a[i - 1] and a[i + 1]

(you can think a[-1] = +infinite, and a[a.length] = +infinite)

Assumptions:

The given array is not null or empty.
There are no duplicate elements in the array.
There is always one and only one result for each case.
"""
class Solution(object):
    def localMinimum(self, A):
        if len(A) == 1:
          return 0
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # compare with neighbor
            if A[mid] > A[mid - 1]:
                end = mid
            elif A[mid] > A[mid + 1]:
                start = mid
            else:
                end = mid
        return start if A[start] < A[end] else end