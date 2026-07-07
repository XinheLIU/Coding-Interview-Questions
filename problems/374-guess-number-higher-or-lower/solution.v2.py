# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = l + ((r - l) >> 1)
            x = guess(mid)
            if x == 0:
                return mid
            elif x == 1:
                l = mid + 1
            else:
                r = mid - 1