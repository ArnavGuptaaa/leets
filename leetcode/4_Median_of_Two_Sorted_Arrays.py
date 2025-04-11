"""
Name: Median of Two Sorted Arrays (#4)
URL: <Add question link here>

Time Complexity: O(Log min(m, n)) [m: len(nums1); n: len(nums2)]
Space Complexity: O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We are intending to run this algorithm on the smaller array.
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2

        total_elements = len(nums1) + len(nums2)
        half = total_elements >> 1

        left = 0
        right = len(nums1) - 1

        while True:
            mid1 = (left + right) >> 1
            mid2 = half - mid1 - 2

            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            r1 = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('inf')

            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                # Odd
                if total_elements % 2:
                    return min(r1, r2)

                # Even
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2

            if l1 > r2:
                right = mid1 - 1
            
            else:
                left = mid1 + 1
