"""
Link : https://leetcode.com/discuss/post/6038274/google-phone-screen-l3-by-anonymous_user-1173/

Question:
Given an array of integers nums, return the length of the longest non-decreasing contiguous subarray.
A subarray is a contiguous part of the array, and a subarray [a₁, a₂, ..., aₖ] is non-decreasing if aᵢ ≤ aᵢ₊₁ for all valid i.
"""

class Solution:

    def longest_increasing_subarray(self, nums):
        left = right = 0
        result = 0

        while right < len(nums):
            if right != 0 and left < right and nums[right] <= nums[right - 1]:
                left = right

            if right - left + 1 > result:
                result = right - left + 1

            right += 1

        return result


    def longest_increasing_subarray_with_one_replacement(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        max_ending = [1] * n
        max_starting = [1] * n

        for idx in range(1, n):
            if nums[idx] >= nums[idx - 1]:
                max_ending[idx] = max_ending[idx - 1] + 1
        
        for idx in range(n - 2, -1 , -1):
            if nums[idx] <= nums[idx + 1]:
                max_starting[idx] = max_starting[idx + 1] + 1

        result = max(max_ending)
        for idx in range(1, n - 1):
            if nums[idx - 1] <= nums[idx + 1]:
                result = max(result, 1 + max_ending[idx - 1] + max_starting[idx + 1])

        return result