import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while(x != 0):
            if(abs(res) > (2 ** 31 - 1) / 10): return 0
            res *= 10
            if x > 0:
                res += x % 10
                x //= 10
            elif x < 0:   # no need for this for cpp
                res -= (-x) % 10
                x = - ((-x) // 10)
        return res
