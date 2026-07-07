class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ret = []
        if not len(nums):
            ret.append(self.helper(lower, upper))
            return ret
        pre = lower - 1
        for n in nums:
            if pre != n and pre + 1 != n:
                ret.append(self.helper(pre + 1, n - 1))
            pre = n
        if nums[-1] < upper:
            ret.append(self.helper(nums[-1] + 1, upper))
        return ret
    
    def helper(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)