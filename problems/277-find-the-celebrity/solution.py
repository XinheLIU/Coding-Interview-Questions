# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        ret = 0
        for i in range(n):
            if knows(ret, i): ret = i
        for i in range(ret):
            if not knows(i, ret) or knows(ret, i): 
                return -1
        for i in range(ret + 1, n):
            if not knows(i, ret):
                return -1
        return ret