from collections import Counter
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        count = Counter()
        for i, r in enumerate(A):
            for j, v in enumerate(r):
                if v == 1:
                    for i2, r2 in enumerate(B):
                        for j2, v2 in enumerate(r2):
                            if v2:
                                count[i-i2, j-j2] += 1
        return max(count.values() or [0]) 

"""
    def largestOverlap(self, A, B):
        N = len(A)
        A2 = [complex(r, c) for r, row in enumerate(A)
              for c, v in enumerate(row) if v]
        B2 = [complex(r, c) for r, row in enumerate(B)
              for c, v in enumerate(row) if v]
        Bset = set(B2)
        seen = set()
        ans = 0
        for a in A2:
            for b in B2:
                d = b-a
                if d not in seen:
                    seen.add(d)
                    ans = max(ans, sum(x+d in Bset for x in A2))
        return ans
"""