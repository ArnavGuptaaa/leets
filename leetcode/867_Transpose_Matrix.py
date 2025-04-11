"""
Name: Transpose Matrix (#867)
URL: https://leetcode.com/problems/transpose-matrix/
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_row = len(matrix)
        len_col = len(matrix[0])

        res = [[-1] * len_row for _ in range(len_col)]

        for row_idx in range(len_row):
            for col_idx in range(len_col):
                res[col_idx][row_idx] = matrix[row_idx][col_idx]

        return res