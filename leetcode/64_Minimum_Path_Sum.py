"""
Name: Minimum Path Sum (#64)
URL: https://leetcode.com/problems/minimum-path-sum/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}

        def dp (row, col):
            if (row, col) in cache:
                return cache[(row, col)]
                
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]

            sum_down = dp(row + 1, col)
            sum_right = dp(row, col + 1)
            
            cache[(row, col)] = grid[row][col] + min(sum_down, sum_right)

            return cache[(row, col)]

        return dp(0, 0)