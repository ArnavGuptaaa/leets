"""
Name: Triangle (#120)
URL: https://leetcode.com/problems/triangle/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}

        def dp(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            if row >= len(triangle) or col >= len(triangle[row]):
                return float('inf')

            if row == len(triangle) - 1:
                return triangle[row][col]

            sum_down = dp(row + 1, col)
            sum_right = dp(row + 1, col + 1)

            cache[(row, col)] = triangle[row][col] + min(sum_down, sum_right)
             
            return cache[(row, col)]

        return dp(0, 0)