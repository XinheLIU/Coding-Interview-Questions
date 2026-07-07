class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return False
        # find one without changing the array
        start, end = 1, len(nums) - 1
        while end >= start:
            middle = start + ((end - start) >> 1)
            print(start, end, middle)
            count = self.countRange(nums, start, middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > middle - start + 1:  # one more in left region
                end = middle
            else:  # one more in right region
                start = middle + 1
        return -1

    def countRange(self, nums, start, end):
        if not nums:
            return 0
        count = 0
        for num in nums:
            if start <= num <= end:
                count += 1
        return count