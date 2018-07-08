class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        m = len(nums1)
        n = len(nums2)
        nums1 = [float('-inf')] + nums1 + [float('inf')]
        nums2 = [float('-inf')] + nums2 + [float('inf')]
        left = (m + n) // 2 - n
        right = (m + n) // 2
        while left <= right:
            mid = (left + right) // 2 # left part : mid
            cut = (m + n) // 2 - mid  # right part :
            if nums1[mid + 1] >= nums2[cut] and nums2[cut + 1] >= nums1[mid]:
                if (m + n) % 2 == 0:
                    return (max(nums1[mid], nums2[cut]) + min(nums1[mid + 1], nums2[cut + 1])) / 2.0
                else:
                    return min(nums1[mid + 1], nums2[cut + 1])
            elif nums1[mid + 1] < nums2[cut]:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
print(s.findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], [0,6]))

