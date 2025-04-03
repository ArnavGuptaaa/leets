"""
Name: Maximum Value of an Ordered Triplet II (#2874)
URL: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)

        l_maxi = 0
        r_maxi = 0
        for idx in range(len(nums)):
            end_idx = -1 - idx

            left_max[idx] = l_maxi
            right_max[end_idx] = r_maxi

            l_maxi = max(l_maxi, nums[idx])
            r_maxi = max(r_maxi, nums[end_idx])

        result = 0
        for idx in range(len(nums) - 1, -1, -1):
            diff = (left_max[idx] - nums[idx]) * right_max[idx]

            result = max(result, diff)

        return result