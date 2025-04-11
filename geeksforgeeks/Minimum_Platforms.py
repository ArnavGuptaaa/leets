"""
Name: Minimum Platforms (#GFG)
URL: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/

Time Complexity: O(N LogN)
Space Complexity: O(1)
"""

class Solution:    
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        start = end = 0
        platforms = 0
        result = 0
        
        while start < len(arr):
            # New train has arrived
            if arr[start] <= dep[end]:
                platforms += 1
                start += 1
            
            # Train has left
            else:
                platforms -= 1
                end += 1
                
            result = max(result, platforms)
            
        return result