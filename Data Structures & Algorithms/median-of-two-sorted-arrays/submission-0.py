class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        newnums1 = sorted(nums1)
        size = len(newnums1)
        if size % 2 == 0:
            return (newnums1[int(size / 2)] + newnums1[int(size / 2) - 1]) / 2
        else:
            return newnums1[int(size/2)]