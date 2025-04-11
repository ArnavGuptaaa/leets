"""
Name: First Missing Positive (#41)
URL: https://leetcode.com/problems/first-missing-positive/


cycleSolution
Time Complexity: O(N)
Space Complexity: O(1)

setSolution 
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def setSolution(self, nums):
        numSet = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numSet:
                return i

        return len(nums) + 1

    def cycleSolution(self, nums):
        for idx in range(len(nums)):
            while (
                1 <= nums[idx] <= len(nums) and
                nums[idx] != nums[nums[idx] - 1]
            ):
                i = idx
                j = nums[idx] - 1

                nums[i], nums[j] = nums[j], nums[i]

        for idx in range(len(nums)):
            if idx + 1 != nums[idx]:
                return idx + 1

        return len(nums) + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        # return self.cycleSolution(nums)
        return self.setSolution(nums)