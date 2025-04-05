"""
Name: Sum of All Subset XOR Totals (#1863)
URL: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
Time Complexity: O(N * 2^N)
Space Complexity: O(N)
"""

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def calculate_xor_sum(arr):
            if len(arr) == 0:
                return 0

            xor_sum = arr[0]

            for idx in range(1, len(arr)):
                num = arr[idx]

                xor_sum ^= num

            return xor_sum

        def backtrack(start_idx, path):
            nonlocal result
            result += calculate_xor_sum(path)

            for idx in range(start_idx, len(nums)):
                path.append(nums[idx])
                backtrack(idx + 1, path)

                path.pop()

        result = 0
        backtrack(0, [])

        return result