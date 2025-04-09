"""
Name: Majority Element (#GFG)
URL: https://www.geeksforgeeks.org/problems/majority-element-1587115620/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def majorityElement(self, arr):
        # Boyer-Moore Algo
        count = 0
        elem = 0
        
        for idx in range(len(arr)):
            num = arr[idx]
            
            if count == 0:
                elem = num
                count += 1
                
            elif num != elem:
                count -= 1
                
            else:
                count += 1
        
        count = 0
        for idx in range(len(arr)):
            num = arr[idx]
            
            if num == elem:
                count += 1
        
        return elem if count > len(arr) / 2 else -1