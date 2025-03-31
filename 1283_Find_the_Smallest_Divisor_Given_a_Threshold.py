"""
Name: Find the Smallest Divisor Given a Threshold (#1283)
URL: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Time Complexity: O(N * Log M) [N : Number of elements in nums; M : Max of nums]
Space Complexity: O(1)
"""

from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum_of_division(n):
            return sum([ceil(num / n) for num in nums])

        left = 1
        right = max(nums)
        result = -1

        while left <= right:
            mid = (left + right) >> 1

            if get_sum_of_division(mid) <= threshold:
                result = mid
                right = mid - 1

            else:
                left = mid + 1

        return result