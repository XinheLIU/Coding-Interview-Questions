#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findKth(nums1, nums2, i, j, k):
            # nums 1 should be shorter
            if len(nums1) - i > len(nums2) - j:
                return findKth(nums2, nums1, j, i, k)
            # if shorter is empty
            if len(nums1) == i:
                return nums2[j + k - 1]
            if k == 1:
                return (min(nums1[i], nums2[j]))
            # take steps
            pa = min(i + k // 2, len(nums1))
            pb = j + (k - (pa - i))
            if nums1[pa - 1] < nums2[pb - 1]:
                # i = pa
                return findKth(nums1, nums2, pa, j, k - (pa - i))
            elif nums1[pa - 1] > nums2[pb - 1]:
                # j = pb
                return findKth(nums1, nums2, i, pb, k - (pb - j))
            else:
                return nums1[pa - 1]
        
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return findKth(nums1, nums2, 0, 0, total // 2 + 1)
        else:
            return (findKth(nums1, nums2, 0, 0, total // 2) + findKth(nums1, nums2, 0, 0, total // 2 + 1)) / 2. 
# @lc code=end

