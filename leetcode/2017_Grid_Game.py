"""
Name: Grid Game (#2017)
URL: https://leetcode.com/problems/grid-game/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        for idx in range(1, len(grid[0])):
            grid[0][idx] += grid[0][idx - 1]
            grid[1][idx] += grid[1][idx - 1]

        min_sum = float('inf')

        for partition_idx in range(len(grid[0])):
            top_sum = grid[0][-1] - grid[0][partition_idx]
            bottom_sum = grid[1][partition_idx - 1] if partition_idx > 0 else 0

            min_sum = min(min_sum, max(top_sum, bottom_sum))
        
        return min_sum

"""
Hint:
The problem states that both players play optimally.
This means bot1 will try to maximize its outcome by minimizing the maximum points bot2 can collect.

Observations:
- Bot1 can only move right and make a single downward move, forming two partitions in the grid (draw this to visualize).
- Bot2 will always choose the path that gives the maximum remaining score from those two partitions.

Therefore:
Since bot1 plays optimally, it must choose the partition point that minimizes
the worst-case score bot2 can achieve.

Final Strategy:
Return the minimum of max(top_partition_sum, bottom_partition_sum)
over all possible partition points.
"""