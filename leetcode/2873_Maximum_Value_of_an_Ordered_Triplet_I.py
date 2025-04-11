"""
Name: Maximum Value of an Ordered Triplet I (#2873)
URL: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_max = [-1] * len(nums)
        right_max = [-1] * len(nums)

        maxi = 0
        for idx in range(len(nums)):
            left_max[idx] = maxi
            maxi = max(maxi, nums[idx])

        maxi = 0
        for idx in range(len(nums)-1, -1, -1):
            right_max[idx] = maxi
            maxi = max(maxi, nums[idx])

        ans = 0
        for idx in range(len(nums)):
            ans = max(ans, (left_max[idx] - nums[idx]) * right_max[idx])

        return ans