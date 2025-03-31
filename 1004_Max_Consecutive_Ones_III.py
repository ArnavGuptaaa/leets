"""
Name: Max Consecutive Ones III (#1004)
URL: https://leetcode.com/problems/max-consecutive-ones-iii/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

        return right - left + 1  