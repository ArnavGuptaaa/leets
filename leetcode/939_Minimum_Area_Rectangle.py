"""
Name: Minimum Area Rectangle (#939)
URL: https://leetcode.com/problems/minimum-area-rectangle/

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set((x, y) for x, y in points)
        result = float('inf')

        for (x1, y1) in points:
            for (x2, y2) in points:
                # It cannot be a diagonal if x1 == x2 or y1 == y2
                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    # Rectangle found. Find area
                    area_rect = abs(y2 - y1) * abs(x2 - x1)

                    result = min(result, area_rect)

        return result if result != float('inf') else 0 