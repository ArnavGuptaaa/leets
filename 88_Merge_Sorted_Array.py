"""
Name: Merge Sorted Array (#88)
URL: https://leetcode.com/problems/merge-sorted-array

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1EndIndex = m - 1
        nums2EndIndex = n - 1
        resEndIndex = (m + n) - 1

        while nums1EndIndex >= 0 and nums2EndIndex >= 0:
            if nums1[nums1EndIndex] > nums2[nums2EndIndex]:
                nums1[resEndIndex] = nums1[nums1EndIndex]
                nums1EndIndex -= 1
            
            else:
                nums1[resEndIndex] = nums2[nums2EndIndex]
                nums2EndIndex -= 1
            
            resEndIndex -= 1
        
        while nums2EndIndex >= 0:
            nums1[resEndIndex] = nums2[nums2EndIndex]
            nums2EndIndex -= 1
            resEndIndex -= 1