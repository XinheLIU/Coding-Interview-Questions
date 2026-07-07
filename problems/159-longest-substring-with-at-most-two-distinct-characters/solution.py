class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        window = collections.defaultdict(int)
        ret = 2
        l, r = 0, 0
        while r < n:
            c1 = s[r]
            window[c1] += 1
            r += 1
            while len(window) > 2:
                c2 = s[l]
                window[c2] -= 1
                if window[c2] <= 0:
                    del window[c2]
                l += 1
            ret = max(ret, r - l)
        return ret