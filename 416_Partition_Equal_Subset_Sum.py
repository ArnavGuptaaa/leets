"""
Name: Partition Equal Subset Sum (#416)
URL: https://leetcode.com/problems/partition-equal-subset-sum/

Time Complexity: O(N * T) [N: Length of nums; T: Target]
Space Complexity: O(N * T) [N: Length of nums; T: Target]
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def backtrack(start_idx, path_sum, target):
            if start_idx >= len(nums):
                return False

            if path_sum > target:
                return False

            if path_sum == target:
                return True

            if cache[start_idx][path_sum] != -1:
                return cache[start_idx][path_sum] 

            choose = backtrack(start_idx + 1, path_sum + nums[start_idx], target)
            leave = backtrack(start_idx + 1, path_sum, target)

            cache[start_idx][path_sum] = choose or leave

            return cache[start_idx][path_sum] 
        
        # O(N)
        total_sum = sum(nums)

        if total_sum % 2:
            return False
        
        target = total_sum // 2
        cache = [[-1] * (target + 1) for _ in range(len(nums) + 1)]
        
        return backtrack(0, 0, target)