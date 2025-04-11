"""
Name: Power of Two (#231)
URL: https://leetcode.com/problems/power-of-two/

Time Complexity: O(1)
Space Complexity: O(1)
"""

import math
class Solution:
    def bitwiseSolution(self, n):
        if n <= 0:
            return False

        # Power of 2 has exactly one bit set.
        # Subtracting 1 from it will result in a complement
        # ANDing those two must yield 0
        return n & (n-1) == 0

    def logSolution(self, n):
        if n <= 0:
            return False
        
        # 2^X = N
        # Log 2^X = Log N (Base 2)
        # X = Log N (Base 2)
        power = math.log2(n)
        return math.floor(power) == math.ceil(power) # ceil and floor to handle flating precision issue

    def isPowerOfTwo(self, n: int) -> bool:
        # return self.logSolution(n)
        return self.bitwiseSolution(n)