"""
Name: Rotting Oranges (#994)
URL: https://leetcode.com/problems/rotting-oranges/

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    def bfs(self, grid, nodeQueue):
        directions = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1],
        ]

        timeToRot = 0

        while nodeQueue:
            didRot = False

            for _ in range(len(nodeQueue)):
                rottenNode = nodeQueue.pop(0)

                for direction in directions:
                    newRowIdx = rottenNode[0] + direction[0]
                    newColIdx = rottenNode[1] + direction[1]

                    if (
                        0 <= newRowIdx < len(grid) and
                        0 <= newColIdx < len(grid[0]) and
                        grid[newRowIdx][newColIdx] == 1
                    ):
                        grid[newRowIdx][newColIdx] = 2
                        didRot = True

                        nodeQueue.append((newRowIdx, newColIdx))
            if didRot:
                timeToRot += 1

        return timeToRot

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenNodes = []

        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                
                if grid[rowIdx][colIdx] == 2:
                    rottenNodes.append((rowIdx, colIdx))

        timeToRot = self.bfs(grid, rottenNodes)

        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx] == 1:
                    return -1

        return timeToRot