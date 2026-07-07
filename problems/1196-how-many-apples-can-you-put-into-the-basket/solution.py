class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        total = 5000
        for i, v in enumerate(sorted(arr)):
            total -= v
            if total < 0: return i
        return len(arr)