"""
Name: Peak element (#GFG)
URL: https://www.geeksforgeeks.org/problems/peak-element/

Time Complexity: O(LogN)
Space Complexity: O(1)
"""

class Solution:   
    def peakElement(self,arr):
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start + end) >> 1
            
            if mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
                start = mid + 1
            elif mid - 1 >= 0 and arr[mid] < arr[mid - 1]:
                end = mid - 1
            else:
                return mid
                
        return -1