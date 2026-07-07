from collections import Counter
class Solution:
    def subarraySum(self, nums: 'List[int]', k: 'int') -> 'int':
        # key : sum , val: # of cumsum appearances from begining
        map, ret, sum = Counter({0:1}), 0, 0
        for num in nums:
            sum += num
            ret += map[sum - k]
            map[sum] += 1
        return ret