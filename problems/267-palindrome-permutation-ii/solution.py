class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        canPalindrome, dic = self.canPermutePalindrome(s)
        if not canPalindrome:
            return []

        halfS = []
        for c in dic:
            for i in range(dic[c] // 2):
                halfS.append(c)

        results = []
        self.permuteUnique(results, halfS)

        if len(s) % 2 == 1:
            oddC = ""
            for c in dic:
                if dic[c] % 2 == 1:
                    oddC = c
            if not results:
                results = [oddC]
            else:
                for idx, result in enumerate(results):
                    results[idx] = result + oddC + result[::-1]
        else:
            for idx, result in enumerate(results):
                results[idx] = result + result[::-1]


        return results


    def canPermutePalindrome(self, s):
        if len(s) == 0:
            return True

        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        foundOdd = 0
        for key in dic:
            if dic[key] % 2 == 1:
                foundOdd += 1

        if len(s) % 2 == 0:
            if foundOdd != 0:
                return False, dic
            else:
                return True, dic
        else:
            if foundOdd == 1:
                return True, dic
            else:
                return False, dic

    def permuteUnique(self, results, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return results
        length = len(nums)
        nums.sort()
        used = [False for i in range(length)]
        self.permuteHelper(nums, used, results, [])
        return results

    def permuteHelper(self, nums, used, results, curList):
        if len(curList) == len(nums):
            tmpList = "".join(curList)
            results.append(tmpList)

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            if not used[i]:
                curList.append(nums[i])
                used[i] = True
                self.permuteHelper(nums, used, results, curList)
                curList.pop()
                used[i] = False