"""
Name: Pacific Atlantic Water Flow (#417)
URL: https://leetcode.com/problems/pacific-atlantic-water-flow/

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    def bfs(self, heights, heightQueue, visited):
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        while heightQueue:
            heightCoords = heightQueue.pop(0)

            for direction in directions:
                newRowIdx = heightCoords[0] + direction[0]
                newColIdx = heightCoords[1] + direction[1]

                if (
                    0 <= newRowIdx < len(heights) and
                    0 <= newColIdx < len(heights[0]) and
                    (newRowIdx, newColIdx) not in visited and
                    heights[newRowIdx][newColIdx] >= heights[heightCoords[0]][heightCoords[1]]
                ):
                    visited.add((newRowIdx, newColIdx))
                    heightQueue.append((newRowIdx, newColIdx))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])

        pacificSeen = set()
        atlanticSeen = set() 
        pacificQueue = []
        atlanticQueue = []
        
        # Prepare visited set and coordinate queues for both atlantic and pacific candidates
        for rowIdx in range(rowLen):
            pacificSeen.add((rowIdx, 0))
            pacificQueue.append((rowIdx, 0))

            atlanticSeen.add((rowIdx, colLen - 1))
            atlanticQueue.append((rowIdx, colLen - 1))

        for colIdx in range(colLen):
            pacificSeen.add((0, colIdx))
            pacificQueue.append((0, colIdx))

            atlanticSeen.add((rowLen - 1, colIdx))
            atlanticQueue.append((rowLen - 1, colIdx))
        
        self.bfs(heights, pacificQueue, pacificSeen)
        self.bfs(heights, atlanticQueue, atlanticSeen)

        return list(pacificSeen.intersection(atlanticSeen))