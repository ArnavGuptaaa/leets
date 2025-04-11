"""
Name: Shortest Path in Binary Matrix (#1091)
URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Time Complexity: O(V + E)
Space Complexity: O(1)
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Invalid Matrix
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        # Singular Element
        if n == 1 and grid[0][0] == 0:
            return 1

        # dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        # dist[0][0] = 1

        dq = deque()
        dq.append((1, 0, 0))

        directions = [
            [-1, -1],
            [-1, 0],
            [0, -1],
            [-1, 1],
            [1, -1],
            [0, 1],
            [1, 0],
            [1, 1],
        ]

        while dq:
            d, row, col = dq.popleft()

            for direction in directions:
                d_row = row + direction[0]
                d_col = col + direction[1]

                if (
                    0 <= d_row < n and
                    0 <= d_col < n and
                    grid[d_row][d_col] == 0 # and
                    # d + 1 < dist[d_row][d_col]
                ):  
                    if d_row == n - 1 and d_col == n -1:
                        # dist[d_row][d_col] = d + 1
                        return d + 1

                    dq.append((d + 1, d_row, d_col))
                    grid[d_row][d_col] = 1
                    # dist[d_row][d_col] = d + 1

        return -1
        