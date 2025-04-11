"""
Name: N-Queens (#51)
URL: https://leetcode.com/problems/n-queens/

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positive_diagonals = set()
        negative_diagonals = set()

        result = []
        board = [['.'] * n for _ in range(n)]
        
        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return 
            


            for col in range(n):
                if col in cols or (row - col) in negative_diagonals or (row + col) in positive_diagonals:
                    continue

                cols.add(col)
                negative_diagonals.add(row - col)
                positive_diagonals.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)
                
                cols.discard(col)
                negative_diagonals.discard(row - col)
                positive_diagonals.discard(row + col)
                board[row][col] = '.'

        backtrack(0)
        return result