"""
Name: Sum of Mutated Array Closest to Target (#1300)
URL: https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

Time Complexity: O(N*LogM) [M: Max(arr)]
Space Complexity: O(1)
"""

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def get_mutated_sum(value):
            total_sum = 0

            for num in arr:
                total_sum += value if num > value else num

            return total_sum
        
        left = 0
        right = max(arr)
        result = -1

        min_diff = float('inf')
        diff_val = float('inf')

        while left <= right:
            mid = (left + right) >> 1

            mutated_sum = get_mutated_sum(mid)
            diff = abs(mutated_sum - target)

            if diff < min_diff or (diff == min_diff and mid < diff_val):
                diff_val = mid
                min_diff = diff

            if mutated_sum < target:
                left = mid + 1

            else:
                right = mid - 1

        return diff_val