class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Moore Voting
        num,count = nums[0],0
        for x in nums:
            if count == 0:
                num,count = x, 1
            elif x == num:
                count += 1
            else:
                count -= 1
        return num
'''
def majorityElement(self, nums):
    counts = collections.Counter(nums)
     return max(counts.keys(), key=counts.get)
'''
'''
def majorityElement(self, nums):   
	dic = {}
	for x in nums:
    	if x in dic:
        	dic[x] += 1
    	else:
        	dic[x] = 1
	for key,value in dic.items():
    	if value > len(nums)/2:
        	return key
'''