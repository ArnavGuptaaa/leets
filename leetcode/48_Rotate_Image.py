"""
Name: Rotate Image (#48)
URL: https://leetcode.com/problems/rotate-image/

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for rowIdx in range(len(matrix)):
            for colIdx in range(rowIdx, len(matrix[0])):
                if rowIdx == colIdx :
                    continue

                matrix[rowIdx][colIdx], matrix[colIdx][rowIdx] = matrix[colIdx][rowIdx], matrix[rowIdx][colIdx]


        for idx in range(len(matrix)):
            start, end = 0, len(matrix[0]) - 1

            while start <= end:
                matrix[idx][start], matrix[idx][end] = matrix[idx][end], matrix[idx][start]

                start += 1
                end -= 1