"""
Name: Combination Sum (#39)
URL: https://leetcode.com/problems/combination-sum/

Time Complexity: O(N^T/M) [T: target; M: min(candidates)]
Space Complexity: O(T/M) [T: target; M: min(candidates)]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidateLength = len(candidates)

        # === 
        def combinationSumHelper(idx, combination):
            # Summing => O(N)
            combinationSum = sum(combination)

            # Copying => O(N)
            if combinationSum == target:
                res.append(combination.copy())
                return
            
            if combinationSum > target:
                return 
            
            for idx in range(idx, candidateLength):
                combination.append(candidates[idx])

                combinationSumHelper(idx, combination)

                combination.pop()

        # === 
        combinationSumHelper(0, [])
        return res