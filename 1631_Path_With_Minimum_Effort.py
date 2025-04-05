"""
Name: Path With Minimum Effort (#1631)
URL: https://leetcode.com/problems/path-with-minimum-effort/

Time Complexity: O(MN * log(MN))
Space Complexity: O(MN)
"""

from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        # Start is the same as destination
        if m - 1 == 0 and n - 1 == 0:
            return 0

        effort = [[float('inf') for _ in range(n)] for _ in range(m)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]

        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        while heap:
            d, row, col = heappop(heap)

            if row == m - 1 and col == n - 1:
                return d

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (
                    0 <= new_row < m and 
                    0 <= new_col < n  
                ):  
                    new_effort = max(abs(heights[row][col] - heights[new_row][new_col]), d)

                    if new_effort < effort[new_row][new_col]:
                        effort[new_row][new_col] = new_effort
                        heappush(heap, (new_effort, new_row, new_col))
                        
        return -1