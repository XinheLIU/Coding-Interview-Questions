class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ret, n = 0, len(nums)
        nums.sort()
        for i in range(n-1,1,-1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ret += (r - l)
                    r -= 1
                else:
                    l += 1
        return ret
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ret, n = 0, len(nums)
        nums.sort()
        for i in range(n-2):
            k = i + 2
            for j in range(i + 1, n-1):
                if nums[i] > 0:
                    while k < n and nums[i] + nums[j] > nums[k]:
                        k += 1
                    ret += k - j - 1
        return ret
'''