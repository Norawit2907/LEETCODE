class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        numstotal = nums1 + nums2
        # print(numstotal)
        numstotal.sort()
        length = len(numstotal)
        if(length % 2 == 0):
            median = (numstotal[(length // 2) - 1] + numstotal[(length // 2)]) / 2
            # print(median)
            return median
        else:
            median = numstotal[(length // 2)]
            # print(median)
            return median

nums1 = [int(x) for x in input().split()]
nums2 = [int(x) for x in input().split()]
ans = Solution()
ans.findMedianSortedArrays(nums1, nums2)