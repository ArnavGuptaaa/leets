"""
Name: Permutations (#46)
URL: https://leetcode.com/problems/permutations/

Time Complexity: O(N!)
Space Complexity: O(N*N!)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        inputLength = len(nums)
        permutations = []

        # =====
        def permuteHelper(permutation, choices):
            if len(permutation) == inputLength:
                permutations.append(permutation.copy())
                return
            
            for idx, choice in enumerate(choices):
                permutation.append(choice)

                permuteHelper(permutation, choices[:idx] + choices[idx+1:])

                permutation.pop()


        #  ====
        permuteHelper([], nums)
        return permutations