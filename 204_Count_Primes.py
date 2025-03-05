"""
Name: Count Primes (#204)
URL: https://leetcode.com/problems/count-primes/

Time Complexity: O(N * Log Log N)
Space Complexity: O(N)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        nums = [1] * n
        nums[0] = nums[1] = 0

        for idx in range(2, len(nums)):
            if nums[idx] == 1:
                for idx2 in range(idx + idx, len(nums), idx):
                    nums[idx2] = 0

        return sum(nums)