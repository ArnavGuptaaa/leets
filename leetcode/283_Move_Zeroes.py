"""
Name: Move Zeroes (#283)
URL: https://leetcode.com/problems/move-zeroes/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0

        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[ptr] = nums[idx]
                ptr += 1
        
        for _ in range(ptr, len(nums)):
            nums[ptr] = 0
            ptr += 1
            