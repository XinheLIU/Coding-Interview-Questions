class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

 '''
 class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(); nums2.sort()
        i, j = 0, 0
        ret = []
        print(nums1, nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(ret) == 0 or ret[-1] != nums1[i]:
                    ret.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ret
  '''