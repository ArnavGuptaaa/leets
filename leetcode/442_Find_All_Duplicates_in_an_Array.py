"""
Name: Find All Duplicates in an Array (#442)
URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findDuplicates(self, nums):
        result = []

        for (idx, num) in enumerate(nums):
            absoluteValue = abs(num) - 1

            if nums[absoluteValue] < 0:
                result.append(absoluteValue + 1)
            else:
                nums[absoluteValue] *= -1

        return result