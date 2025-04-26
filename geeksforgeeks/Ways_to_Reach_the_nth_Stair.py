"""
Name: Ways to Reach the nth Stair
URL: https://www.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair-1587115620/1

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def __init__(self):
        self.cache = {}
        
    def countWays(self, n):
        if n in self.cache:
            return self.cache[n]
            
        if n < 0:
            return 0
            
        if n <= 1:
            return 1
            
        prev_stair = self.countWays(n - 1)
        second_prev_stair = self.countWays(n - 2)
        
        self.cache[n] = prev_stair + second_prev_stair
        
        return prev_stair + second_prev_stair