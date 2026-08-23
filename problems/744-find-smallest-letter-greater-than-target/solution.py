#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) >> 1
            if letters[mid] > target:
                r = mid - 1
            else: # <= target
                l = mid + 1
        # if all elements <= target, l = len(letters)
        return letters[l % len(letters)]

# @lc code=end
