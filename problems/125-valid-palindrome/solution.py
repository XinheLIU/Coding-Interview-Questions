#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and self.skip(s[l]):
                l += 1
            while l < r and self.skip(s[r]):
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def skip(self, c):
        return not c.isalpha() and not c.isdigit()
'''
class Solution:
  def isPalindrome(self, input: str) -> bool:
    """
    input: string input
    return: boolean
    """
    if not input:
      return True
    l, r = 0, len(input) - 1
    while l < r:
      if not input[l].isalnum():
        l += 1
      elif not input[r].isalnum():
        r -= 1
      else:
        if input[l].lower() != input[r].lower():
          return False
        l += 1
        r -= 1
    return True
'''
# @lc code=end

