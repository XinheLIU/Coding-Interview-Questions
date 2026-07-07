class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret, mx = 0, 0
        for i, n in enumerate(arr):
            mx = max(mx, n)
            if mx == i: ret += 1 #able to do a chunck
        return ret