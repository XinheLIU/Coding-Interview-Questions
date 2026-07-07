class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2^0 does not count
        return n != 0 and n & (n-1) == 0