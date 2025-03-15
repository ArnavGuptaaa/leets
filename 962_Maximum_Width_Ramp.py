"""
Name: Maximum Width Ramp (#962)
URL: https://leetcode.com/problems/maximum-width-ramp/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0

        # Prepare stack with decreasing values
        for idx, num in enumerate(nums):
            if not stack:
                stack.append(idx)
                continue

            if num < nums[stack[-1]]:
                stack.append(idx)

        # Iterate from last to first index
        for idx in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[idx]:
                popped_idx = stack.pop()

                max_width = max(max_width, idx - popped_idx)

        return max_width
