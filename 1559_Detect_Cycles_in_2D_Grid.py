"""
Name: Detect Cycles in 2D Grid (#1559)
URL: https://leetcode.com/problems/detect-cycles-in-2d-grid/

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        def check_cycle(node, parent):
            row = node[0]
            col = node[1]

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (
                    0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[0]) and
                    grid[new_row][new_col] == grid[row][col]
                ):
                    new_node = (new_row, new_col)

                    if new_node not in visited:
                        visited.add(new_node)
                        
                        if check_cycle(new_node, node):
                            return True
                    
                    elif parent != new_node:
                        return True

            return False

        visited = set()

        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    node = (row, col)
                    parent = (-5, -5)

                    visited.add(node)

                    if check_cycle(node, parent):
                        return True

        return False