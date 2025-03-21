"""
Name: Jump Game (#55)
URL: https://leetcode.com/problems/jump-game/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far_idx = 0

        for idx, num in enumerate(nums):
            if idx > far_idx:
                return False

            far_idx = max(far_idx, idx + num)

            if far_idx >= len(nums) - 1:
                return True

        return False
