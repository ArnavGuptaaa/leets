"""
Name: Pascal's Triangle (#118)
URL: https://leetcode.com/problems/pascals-triangle/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for idx in range(numRows):
            level = [1] * (idx + 1)
            triangle.append(level)

        for idx in range(2, numRows):
            for level_idx in range(1, len(triangle[idx]) - 1):

                triangle[idx][level_idx] = triangle[idx - 1][level_idx] + triangle[idx - 1][level_idx - 1]

        return triangle