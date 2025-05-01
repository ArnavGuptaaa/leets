"""
Name: Maximum Width Ramp (#962)
URL: https://leetcode.com/problems/maximum-width-ramp/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = [0] * len(nums)
        max_so_far = 0

        for idx, num in enumerate(reversed(nums)):
            idx = -1 - idx

            max_so_far = max(max_so_far, num)
            max_right[idx] = max_so_far

        result = 0
        left = right = 0
        
        while right < len(nums):
            while nums[left] > max_right[right]:
                left += 1

            result = max(result, right - left)
            right += 1

        return result