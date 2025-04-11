"""
Name: Maximal Square (#221)
URL: https://leetcode.com/problems/maximal-square/

Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])

        cache = {}

        def max_square(row, col):
            if (row, col) in cache:
                return cache[(row, col)]

            if row >= row_len or col >= col_len:
                return 0

            max_length = 0

            len_down = max_square(row + 1, col)
            len_right = max_square(row, col + 1)
            len_diag = max_square(row + 1, col + 1)

            if matrix[row][col] == '1':
                max_length = 1 + min(len_down, len_right, len_diag)

            matrix[row][col] = max_length
            cache[(row, col)] = max_length

            return max_length

        max_square(0, 0)
        max_side = max(cache.values())

        return max_side * max_side