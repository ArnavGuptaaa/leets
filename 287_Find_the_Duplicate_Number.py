"""
Name: Find the Duplicate Number (#287)
URL: https://leetcode.com/problems/find-the-duplicate-number/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums: 
            absoluteNumVal = abs(num)

            if nums[absoluteNumVal] < 0:
                return absoluteNumVal

            nums[absoluteNumVal] = -1 * nums[absoluteNumVal]
        
        return -1