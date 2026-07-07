#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        # strip
        s = self.strip(s)
        reverse(s, 0, len(s) - 1)
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            reverse(s, start, i - 1)
            i += 1
        return "".join(s)
    
    def strip(self, s):
        processed = list()
        for i, c in enumerate(s):
            if c == ' ':
                if i == 0 or s[i-1].isspace():
                    continue
            processed.append(c)
        if processed and processed[-1].isspace():
            processed = processed[:-1]
        return processed

'''
    def reverseWords(self, s: str) -> str:
        word = ''
        ans = ''
        for c in s:
            if c == ' ':
                if word != "":
                    ans += word[::-1]
                word = ""
                ans += c
            else:
                word += c
        if word != "":
            ans += word[::-1]
        return ans
'''
# @lc code=end

