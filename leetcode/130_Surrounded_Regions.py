"""
Name: Surrounded Regions (#130)
URL: https://leetcode.com/problems/surrounded-regions/
"""

class Solution:
    # Traversing Board => O(N^2)
    def prepareBoard(self, board):
        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                # Save 'S' nodes by marking them 'O'
                if board[rowIdx][colIdx] == 'S':
                    board[rowIdx][colIdx] = 'O'
                    continue

                # All nodes except 'S' marked must be captured
                board[rowIdx][colIdx] = 'X'

    """
    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
    """
    # BFS Traversal => (M * N)
    def bfs(self, board, nodeQueue):
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        while nodeQueue:
            node = nodeQueue.popleft()

            for direction in directions:
                newRowIdx = node[0] + direction[0]
                newColIdx = node[1] + direction[1]

                if(
                    0 <= newRowIdx < len(board) and 
                    0 <= newColIdx < len(board[0]) and 
                    board[newRowIdx][newColIdx] == 'O'
                ):
                    # Mark every traversed node as 'S' (Save)
                    board[newRowIdx][newColIdx] = 'S'
                    nodeQueue.append((newRowIdx, newColIdx))


    """
    Time Complexity: O(M * N)
    Space Complexity: O(M * N)
    """
    def dfs(self, board, node):
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]
        
        for direction in directions:
            newRowIdx = node[0] + direction[0]
            newColIdx = node[1] + direction[1]

            if(
                0 <= newRowIdx < len(board) and 
                0 <= newColIdx < len(board[0]) and 
                board[newRowIdx][newColIdx] == 'O'
            ):
                # Mark every traversed node as 'S' (Save)
                board[newRowIdx][newColIdx] = 'S'
                self.dfs(board, (newRowIdx, newColIdx))


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)
        colLen = len(board[0])

        # visited set NOT required since we are marking all traversed node as 'S'
        nodeQueue = Deque()

        # Iterate over the edge of the matrix
        # Mark every node on the edge with 'S' (Save)
        for rowIdx in range(rowLen):
            if board[rowIdx][0] == 'O':
                board[rowIdx][0] = 'S'
                nodeQueue.append((rowIdx, 0))

            if board[rowIdx][colLen - 1] == 'O':
                board[rowIdx][colLen - 1] = 'S'
                nodeQueue.append((rowIdx, colLen - 1))

        for colIdx in range(colLen):
            if board[0][colIdx] == 'O':
                board[0][colIdx] = 'S'
                nodeQueue.append((0, colIdx))

            if board[rowLen - 1][colIdx] == 'O':
                board[rowLen - 1][colIdx] = 'S'
                nodeQueue.append((rowLen - 1, colIdx))

        # Solution 1 : Perform BFS on nodeQueue
        self.bfs(board, nodeQueue)

        # Solution 2 : Perform DFS on nodeQueue
        for node in nodeQueue:
            self.dfs(board, node)

        # Turn every node that is NOT in visited set to 'X'
        self.prepareBoard(board)