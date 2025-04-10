"""
Name: Maximum Average Subarray I (#643)
URL: https://leetcode.com/problems/maximum-average-subarray-i/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k

        window_sum = sum(nums[:k])
        max_sum = window_sum

        while right < len(nums):
            window_sum += nums[right]
            window_sum -= nums[right - k]

            max_sum = max(max_sum, window_sum)
            right += 1

        return max_sum / k