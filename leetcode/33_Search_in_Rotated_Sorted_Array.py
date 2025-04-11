"""
Name: Search in Rotated Sorted Array (#33)
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Time Complexity: O(LogN)
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Check if left array is sorted
            if nums[start] <= nums[mid]:
                # If target lies in sorted array, restrict to left
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1

                # Else search right
                else:
                    start = mid + 1

            # Else, right array is sorted
            else:
                # If target lies in sorted array, restrict to right
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1

                # Else search left
                else:
                    end = mid - 1

        # Not found
        return -1