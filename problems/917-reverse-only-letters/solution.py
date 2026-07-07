#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        def noletter(c):
            return not (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'))

        l, r = 0, len(S) - 1
        while l < r:
            while noletter(S[l]) and l < r:
                l += 1
            while noletter(S[r]) and l < r:
                r -= 1
            else:
                temp = S[l]
                S = S[:l] + S[r] + S[l+1:]
                l += 1
                S = S[:r] + temp + S[r+1:]
                r -= 1
        return S
# @lc code=end

