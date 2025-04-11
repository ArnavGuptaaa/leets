"""
Name: Subsets (#78)
URL: https://leetcode.com/problems/subsets/

Time Complexity: O(N*2^N)
Space Complexity: O(N + 2^N) 
"""

class Solution:
    def __init__(self):
        self.res = []
    
    def subsetsHelper(self, nums, n, subset):
        if n == len(nums):
            self.res.append(subset.copy())
            return 
    
        # Take
        subset.append(nums[n])
        self.subsetsHelper(nums, n+1, subset)
        
        # Leave
        subset.pop()
        self.subsetsHelper(nums, n+1, subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsetsHelper(nums, 0, [])

        return self.res