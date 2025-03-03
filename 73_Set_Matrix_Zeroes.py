"""
Name: Set Matrix Zeroes (#73)
URL: https://leetcode.com/problems/set-matrix-zeroes/

Time Complexity: O(M * N)
Space Complexity: O(1)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        doesFirstRowContainZero = False
        doesFirstColumnContainZero = False

        for colIdx in range(len(matrix[0])):
            if matrix[0][colIdx] == 0:
                doesFirstRowContainZero = True
                break
        
        for rowIdx in range(len(matrix)):
            if matrix[rowIdx][0] == 0:
                doesFirstColumnContainZero = True
                break

        for rowIdx in range(1, len(matrix)):
            for colIdx in range(1, len(matrix[0])):
                if matrix[rowIdx][colIdx] == 0:
                    matrix[0][colIdx] = 0
                    matrix[rowIdx][0] = 0

        for rowIdx in range(1, len(matrix)):
            for colIdx in range(1, len(matrix[0])):
                if matrix[0][colIdx] == 0 or matrix[rowIdx][0] == 0:
                    matrix[rowIdx][colIdx] = 0

        if doesFirstRowContainZero:
            matrix[0] = [0] * len(matrix[0])
        
        if doesFirstColumnContainZero:
            for rowIdx in range(len(matrix)):
                matrix[rowIdx][0] = 0