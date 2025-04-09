"""
Name: Kadane's Algorithm (#GFG)
URL: https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArraySum(self, arr):
        current_max = global_max = arr[0]
        
        for idx in range(1, len(arr)):
            num = arr[idx]
            
            current_max = max(current_max + num, num)
            global_max = max(global_max, current_max)
            
        return global_max