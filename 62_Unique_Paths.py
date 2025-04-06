"""
Name: Unique Paths (#62)
URL: https://leetcode.com/problems/unique-paths

Time Complexity: O(MN)
Space Complexity: O(MN)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dp(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            if row >= m or col >= n:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            ways_down = dp(row + 1, col)
            ways_right = dp(row, col + 1)

            total_ways = ways_down + ways_right

            cache[(row, col)] = total_ways

            return total_ways

        return dp(0, 0)