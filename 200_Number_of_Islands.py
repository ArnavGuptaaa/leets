"""
Name: Number of Islands (#200)
URL: https://leetcode.com/problems/number-of-islands/

Time Complexity: O(V + E)
Space Complexity: O(M * N)
"""

class Solution:
    def dfs(self, nodeTuple, visited, grid):
        visited.add(nodeTuple)

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]
        
        for direction in directions:
            newRowIdx = nodeTuple[0] + direction[0]
            newColIdx = nodeTuple[1] + direction[1]

            if (
                0 <= newRowIdx < len(grid) and
                0 <= newColIdx < len(grid[0]) and
                grid[newRowIdx][newColIdx] == '1' and
                (newRowIdx, newColIdx) not in visited
            ):
                visited.add((newRowIdx, newColIdx))

                self.dfs((newRowIdx, newColIdx), visited, grid)

    def bfs(self, nodeTuple, visited, grid):
        nodeQueue = [nodeTuple]
        visited.add(nodeTuple)

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        while len(nodeQueue) != 0:
            node = nodeQueue.pop(0)

            for direction in directions:
                newRowIdx = node[0] + direction[0]
                newColIdx = node[1] + direction[1]

                if (
                    0 <= newRowIdx < len(grid) and
                    0 <= newColIdx < len(grid[0]) and
                    grid[newRowIdx][newColIdx] == '1' and
                    (newRowIdx, newColIdx) not in visited
                ):
                    visited.add((newRowIdx, newColIdx))
                    grid[newRowIdx][newColIdx] == '0'
                    nodeQueue.append((newRowIdx, newColIdx))
        

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        islandCount = 0

        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[rowIdx])):
                if (
                    grid[rowIdx][colIdx] == '1' and 
                    (rowIdx, colIdx) not in visited
                ):
                    islandCount += 1

                    # self.bfs((rowIdx, colIdx), visited, grid)
                    self.dfs((rowIdx, colIdx), visited, grid)

        return islandCount