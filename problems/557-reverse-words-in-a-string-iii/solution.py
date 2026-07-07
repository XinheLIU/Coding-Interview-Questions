#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        start = end = 0
        while start < n:
            # go to the end of the word
            while end < n and s[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(s, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
        return ''.join(s[:])
    
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
# @lc code=end
# return " ".join([word[::-1] for word in s.split(' ')])
