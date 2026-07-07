#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            strs = []
            while stack and stack[-1] != '[':
                strs.append(stack.pop())
            # [
            stack.pop()
            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += int(stack.pop()) * base  
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)
        return ''.join(stack)
# @lc code=end
'''
class Solution:
    def decodeString(self, s: str) -> str:
        ret, num = "", 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                j = i
                cnt = 0
                while i < len(s):
                    if s[i] == '[': cnt += 1
                    elif s[i] == ']': cnt -= 1
                    if cnt == 0: break
                    i += 1
                ret += num * self.decodeString(s[j+1:i])
                num = 0
            elif s[i] == "]":
                return ret
            else:
                ret += s[i]
            i += 1
        return ret
'''
'''
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, temp = dfs(s, i + 1)
                    res += multi * temp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)
'''

