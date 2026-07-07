#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        cnt1, cnt2 = 0, 0 
        for v in nums:
            if v == candidate1:
                cnt1 += 1
            elif v == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = v
            elif cnt2 == 0:
                candidate2 = v
            else:
                cnt1 -= 1
                cnt -= 1
        ret = []
        if len(list(filter(lambda x: x == candidate1, nums))) > len(nums) / 3:
            ret.append(candidate1)
        if len(list(filter(lambda x: x == candidate2, nums))) > len(nums) / 3:
            ret.append(candidate2) 
        return ret
        
# @lc code=end

'''
# hash map
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dic = {}
    for x in nums:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    for key,value in dic.items():
        if value > len(nums) / 3:
            ret.append(key)
    return ret
'''