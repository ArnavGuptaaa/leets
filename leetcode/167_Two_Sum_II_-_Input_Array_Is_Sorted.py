"""
Name: Two Sum II - Input Array Is Sorted (#167)
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            currSum = numbers[start] + numbers[end]

            if currSum < target:
                start += 1
            elif currSum > target:
                end -= 1
            else:
                return [start + 1, end + 1]

        return [-1, -1]