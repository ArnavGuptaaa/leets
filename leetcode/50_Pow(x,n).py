"""
Name: Pow(x, n) (#50)
URL: https://leetcode.com/problems/powx-n/description/

Time Complexity: O(Log N)
Space Complexity: O(Log N)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        
        else:
            return x * self.myPow(x * x, (n - 1) / 2)