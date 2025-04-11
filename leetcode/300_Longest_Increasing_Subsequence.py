"""
Name: Longest Increasing Subsequence (#300)
URL: https://leetcode.com/problems/longest-increasing-subsequence/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dp(start_idx, prev_idx): 
            if (start_idx, prev_idx) in cache:
                return cache[(start_idx, prev_idx)]
                
            longest_subsequence = 0

            for idx in range(start_idx, len(nums)):
                if prev_idx != -1 and nums[idx] <= nums[prev_idx]:
                    continue

                # Take + Leave
                longest_subsequence = max(longest_subsequence, 1+ dp(idx + 1, idx))

            cache[(start_idx, prev_idx)] = longest_subsequence
            return longest_subsequence

        cache = {}
        return  dp(0, -1)