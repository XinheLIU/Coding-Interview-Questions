class Solution:
    def countLetters(self, S: str) -> int:
        s = ' ' + S
        total = 0
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                cnt = 1
            else:
                cnt += 1
            total += cnt
        return total