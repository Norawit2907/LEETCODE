class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        size1 = len(nums1)
        if(size1 % 2 == 0):
            middleL = nums1[size1 // 2]
            middleR = nums1[(size1 // 2) - 1]
            median1 = (middleL + middleR) / 2
        else:
            median1 = nums1[size1 // 2]

        size2 = len(nums2)
        if(size2 % 2 == 0):
            middleL = nums2[size2 // 2]
            middleR = nums2[(size2 // 2) - 1]
            median2 = (middleL + middleR) / 2
        else:
            median2 = nums1[size1 // 2]
        
        # print(median1, median2, (median1 + median2) / 2)
        return median1 + median2 / 2
