"""
Name: Count Square Submatrices with All Ones (#1277)
URL: https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        cache = {}

        def helper(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            if row < 0 or row >= len(matrix):
                return 0

            if col < 0 or col >= len(matrix[0]):
                return 0

            if matrix[row][col] == 0:
                return 0

            right = helper(row, col + 1)
            diagonal = helper(row + 1, col + 1)
            down = helper(row + 1, col)

            max_n = 1 + min(right, diagonal, down)
            cache[(row, col)] = max_n

            return max_n
        
        res = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    continue
                
                res += helper(row, col)

        return res