"""
Name: Find First and Last Position of Element in Sorted Array (#34)
URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Time Complexity: O(LogN)
Space Complexity: O(1)
"""

class Solution:
    def search_position(self, nums, target, find_left):
        left = 0
        right = len(nums) - 1

        index = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                index = mid

                if find_left:
                    right = mid - 1

                else:
                    left = mid + 1

        return index
        

    def searchRange(self, nums, target):
        left_index = self.search_position(nums, target, True)
        right_index = self.search_position(nums, target, False)

        return [left_index, right_index]