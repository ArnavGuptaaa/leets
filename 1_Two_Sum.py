"""
Name: Two Sum (#1)
URL: https://leetcode.com/problems/two-sum/

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for (idx, num) in enumerate(nums):
            if (target - num) in seen:
                return [seen[target-num], idx]
            
            seen[num] = idx
        
        return [-1, -1]