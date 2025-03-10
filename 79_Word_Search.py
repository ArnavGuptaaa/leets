"""
Name: Word Search (#79)
URL: https://leetcode.com/problems/word-search/

Time Complexity: O(?)
Space Complexity: O(N)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [
            [-1, 0],
            [0, -1],
            [0, 1],
            [1, 0],
        ]

        visited = set()

        def does_exist(node, index):
            (row_idx, col_idx) = node
            nonlocal directions
            nonlocal visited

            if index >= len(word):
                return True

            if row_idx < 0 or row_idx >= len(board):
                return False

            if col_idx < 0 or col_idx >= len(board[0]):
                return False

            if node in visited:
                return False

            if board[row_idx][col_idx] != word[index]:
                return False

            visited.add(node)

            for direction in directions:
                new_row = row_idx + direction[0]
                new_col = col_idx + direction[1]

                if does_exist((new_row, new_col), index + 1):
                    return True

            visited.discard(node)

            return False

        # ===
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]: 
                    if does_exist((row, col), 0):
                        return True

        return False