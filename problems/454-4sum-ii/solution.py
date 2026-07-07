from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt1, cnt2 = Counter(), Counter()
        n = len(A) # size is the same
        for i in range(n):
            for j in range(n):
                cnt1[A[i] + B[j]] += 1
                cnt2[C[i] + D[j]] += 1
        ret = 0
        for ele in cnt1:
            ret += cnt1[ele] * cnt2[-ele]
        return ret