"""
Name: Indexes of Subarray Sum (#GFG)
URL: https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def subarraySum(self, arr, target):
        left = right = 0
        window_sum = 0
        
        while right < len(arr):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                
                left += 1
            
            if window_sum == target:
                return [left + 1, right + 1]
            
            right += 1
        
        return [-1]