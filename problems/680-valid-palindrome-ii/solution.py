#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = self.twoPointers(s, 0, len(s) - 1)
        if l >= r:
            return True
        return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
    
    def isPalindrome(self, s, l, r):
        l, r = self.twoPointers(s, l, r)
        if l >= r:
            return True
    def twoPointers(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return l, r
            l += 1
            r -= 1
        return l, r
# @lc code=end

