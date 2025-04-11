"""
Name: House Robber (#198)
URL: https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums) + 1)
        
        """
        Time Complexity: O(N)
        Space Complexity: O(N + N)
        """
        def memo_rob(idx):
            if idx >= len(nums):
                return 0

            if cache[idx] != -1:
                return cache[idx]

            rob = nums[idx] + memo_rob(idx + 2)
            spare = memo_rob(idx + 1)

            cache[idx] = max(rob, spare)
            return cache[idx]


        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        def tab_rob():
            cache[0] = nums[0]
            cache[1] = max(nums[0], nums[1]) if len(nums) > 1 else nums[0]

            for idx in range(2, len(nums)):
                cache[idx] = max(nums[idx] + cache[idx - 2], cache[idx - 1])

            return cache[len(nums) - 1]            

        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        def so_rob():
            prev2 = nums[0]
            prev = max(nums[0], nums[1]) if len(nums) > 1 else nums[0]

            for idx in range(2, len(nums)):
                result = max(nums[idx] + prev2, prev)

                prev2 = prev
                prev = result

            return prev

        # Memoized
        return memo_rob(0)

        # Tabulated
        return tab_rob()

        # Space optimized
        return so_rob()