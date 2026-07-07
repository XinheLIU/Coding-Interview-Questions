# can also change array length at run time

class Solution(object):
    # i, j is the start pointers
    def findKth(self, nums1, nums2, i, j, k):
        # nums 1 should be shorter
        if len(nums1) - i > len(nums2) - j:
            return self.findKth(nums2, nums1, j, i, k)
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
            return self.findKth(nums1, nums2, pa, j, k - (pa - i))
        elif nums1[pa - 1] > nums2[pb - 1]:
            # j = pb
            return self.findKth(nums1, nums2, i, pb, k - (pb - j))
        else:
            return nums1[pa - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findKth(nums1, nums2, 0, 0, total // 2 + 1)
        else:
            return (self.findKth(nums1, nums2, 0, 0, total // 2) + self.findKth(nums1, nums2, 0, 0, total // 2 + 1)) / 2.0