"""
Name: House Robber (#198)
URL: https://leetcode.com/problems/house-robber/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        
        # ===
        def tabulated_rob():
            if len(nums) == 1:
                return nums[0]

            cache[0] = nums[0]
            cache[1] = max(nums[1], nums[0])

            for idx in range(2, len(nums)):
                cache[idx] = max(cache[idx - 2] + nums[idx], cache[idx - 1])

            return cache[len(nums) - 1]

        # ===
        def memoized_rob(house):
            if house >= len(nums):
                return 0

            if cache[house] != -1:
                return cache[house]

            rob_house = memoized_rob(house + 2) + nums[house]
            spare_house = memoized_rob(house + 1)

            max_robbed = max(rob_house, spare_house)

            cache[house] = max_robbed
            return max_robbed
        
        # ===
        # return memoized_rob(0)
        return tabulated_rob()