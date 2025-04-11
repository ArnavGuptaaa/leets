"""
Name: House Robber II (#213)
URL: https://leetcode.com/problems/house-robber-ii/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        # ===
        def memoized_robbery(house, end):
            if house > end:
                return 0

            if cache[house] != -1:
                return cache[house]

           
            rob_house = nums[house] + memoized_robbery(house + 2, end)
            spare_house = memoized_robbery(house + 1, end)

            cache[house] = max(rob_house, spare_house)

            return cache[house]

        # ===
        def tabulated_robbery(house, end):
            if house == end:
                return nums[house]

            cache = [-1] * len(nums)

            cache[end] = nums[end]            
            cache[end - 1] = max(nums[end], nums[end - 1])

            for idx in range(end - 2, house - 1, -1):
                cache[idx] = max(cache[idx + 2] + nums[idx], cache[idx + 1])
            
            return cache[house]

        # ===
        if len(nums) == 1:
            return nums[0]

        # # Memoized
        # rob_first = memoized_robbery(0, len(nums) - 2)
        # cache = [-1] * len(nums) # Clear Cache
        # rob_second = memoized_robbery(1, len(nums) - 1)
        # return max(rob_first, rob_second)

        # Tabulated
        rob_first = tabulated_robbery(0, len(nums) - 2)
        rob_second = tabulated_robbery(1, len(nums) - 1)
        return max(rob_first, rob_second)