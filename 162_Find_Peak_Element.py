"""
Name: Find Peak Element (#162)
URL: https://leetcode.com/problems/find-peak-element

Time Complexity: O(Log N)
Space Complexity: O(1)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        numLength = len(nums)

        left = 0
        right = numLength - 1

        while left <= right:
            mid = (left + right) // 2

            if mid < numLength - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                return mid
        
        return -1