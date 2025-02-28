"""
Name: Max Area of Island (#695)
URL: https://leetcode.com/problems/max-area-of-island/

Time Complexity: O(V + E)
Space Complexity: O(M * N)
"""

class Solution:
    def dfs(self, nodeTuple, visited, grid):
        areaOfIsland = 1
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
                grid[newRowIdx][newColIdx] == 1 and
                (newRowIdx, newColIdx) not in visited
            ):
                visited.add((newRowIdx, newColIdx))

                areaOfIsland += self.dfs((newRowIdx, newColIdx), visited, grid)
        
        return areaOfIsland

    def bfs(self, nodeTuple, visited, grid):
        areaOfIsland = 0

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
            areaOfIsland += 1

            for direction in directions:
                newRowIdx = node[0] + direction[0]
                newColIdx = node[1] + direction[1]

                if (
                    0 <= newRowIdx < len(grid) and
                    0 <= newColIdx < len(grid[0]) and
                    grid[newRowIdx][newColIdx] == 1 and
                    (newRowIdx, newColIdx) not in visited
                ):
                    visited.add((newRowIdx, newColIdx))
                    nodeQueue.append((newRowIdx, newColIdx))

        return areaOfIsland

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        maxArea = 0

        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[rowIdx])):
                if (
                    grid[rowIdx][colIdx] == 1 and 
                    (rowIdx, colIdx) not in visited
                ):
                    maxArea = max(maxArea, self.bfs((rowIdx, colIdx), visited, grid))
                    # maxArea = max(maxArea, self.dfs((rowIdx, colIdx), visited, grid))

        return maxArea