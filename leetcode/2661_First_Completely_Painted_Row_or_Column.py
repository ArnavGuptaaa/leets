"""
Name: First Completely Painted Row or Column (#2661)
URL: https://leetcode.com/problems/first-completely-painted-row-or-column/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rowSum = [0] * len(mat)
        colSum = [0] * len(mat[0])
        
        valToIndex = {}

        for rowIdx in range(len(mat)):
            for colIdx in range(len(mat[0])):
                rowSum[rowIdx] += mat[rowIdx][colIdx]
                colSum[colIdx] += mat[rowIdx][colIdx]

                valToIndex[mat[rowIdx][colIdx]] = (rowIdx, colIdx)

        for idx, elem in enumerate(arr):
            (rowIdx, colIdx) = valToIndex[elem]

            rowSum[rowIdx] -= elem
            colSum[colIdx] -= elem

            if rowSum[rowIdx] == 0 or colSum[colIdx] == 0:
                return idx