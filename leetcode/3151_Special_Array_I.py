"""
Name: Special Array I (#3151)
URL: https://leetcode.com/problems/special-array-i/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True
        
        EVEN, ODD = 0, 1

        prev_parity = ODD if nums[0] % 2 else EVEN

        for idx in range(1, len(nums)):
            curr_parity = ODD if nums[idx] % 2 else EVEN

            if prev_parity == curr_parity:
                return False

            prev_parity = curr_parity

        return True