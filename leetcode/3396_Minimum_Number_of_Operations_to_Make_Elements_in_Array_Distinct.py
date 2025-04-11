"""
Name: Minimum Number of Operations to Make Elements in Array Distinct (#3396)
URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
"""

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def operations_formula(self, nums):
        seen = set()

        for idx in range(len(nums) - 1,  -1, -1):
            if nums[idx] in seen:
                return idx // 3 + 1
                
            seen.add(nums[idx])

        return 0

    """
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    def set_length(self, nums):
        num_set = set(nums)
        operations = 0

        while len(nums) != len(num_set):
            nums = nums[3:]
            num_set = set(nums)

            operations += 1

        return operations

    def minimumOperations(self, nums: List[int]) -> int:
        return self.operations_formula(nums)
        # return self.set_length(nums)