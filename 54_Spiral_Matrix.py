"""
Name: Spiral Matrix (#54)
URL: https://leetcode.com/problems/spiral-matrix/

Time Complexity: O(M*N)
Space Complexity: O(1) [Excluding result storage]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        direction = 0

        topLeft = [0, 0]
        topRight = [0, len(matrix[0]) - 1]
        bottomLeft = [len(matrix) - 1, 0]
        bottomRight = [len(matrix) - 1, len(matrix[0]) - 1]

        while \
            topLeft[1] <= topRight[1] and \
            topRight[0] <= bottomRight[0] and \
            bottomRight[1] >= bottomLeft[1] and \
            bottomLeft[0] >= topLeft[0]:

            # L2R => Row fixed
            if direction == 0:
                for idx in range(topLeft[1], topRight[1] + 1):
                    res.append(matrix[topLeft[0]][idx])

                topLeft[0] += 1
                topRight[0] += 1

            # U2D => Column fixed
            elif direction == 1:
                for idx in range(topRight[0], bottomRight[0] + 1):
                    res.append(matrix[idx][topRight[1]])

                topRight[1] -= 1
                bottomRight[1] -= 1

            # R2L => Row fixed
            elif direction == 2:
                for idx in range(bottomRight[1], bottomLeft[1] - 1, -1):
                    res.append(matrix[bottomRight[0]][idx])

                bottomRight[0] -= 1
                bottomLeft[0] -= 1

            # D2U => Column fixed
            else:
                for idx in range(bottomLeft[0], topLeft[0] - 1, -1):
                    res.append(matrix[idx][bottomLeft[1]])

                bottomLeft[1] += 1
                topLeft[1] += 1

            # flip direction
            direction = (direction + 1) % 4

        return res