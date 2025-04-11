"""
Name: Equilibrium Point (#GFG)
URL: https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        curr_sum = 0
        
        for idx, num in enumerate(arr):
            curr_sum = curr_sum + num
            
            target = total_sum - curr_sum
            sum_until_before_index = curr_sum - num
            
            if target == sum_until_before_index:
                return idx
                
        return -1