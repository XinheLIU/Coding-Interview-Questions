class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return n
        window = collections.defaultdict(int)
        ret = k
        l, r = 0, 0
        while r < n:
            c1 = s[r]
            window[c1] += 1
            r += 1
            while len(window) > k:
                c2 = s[l]
                window[c2] -= 1
                if window[c2] <= 0:
                    del window[c2]
                l += 1
            ret = max(ret, r - l)
        return ret