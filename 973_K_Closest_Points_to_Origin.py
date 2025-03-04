"""
Name: K Closest Points to Origin (#973)
URL: https://leetcode.com/problems/k-closest-points-to-origin/

Time Complexity: O(N * LogN)
Space Complexity: O(N)
"""

from heapq import heapify, heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min Heap stores (distance, (x, y))
        distances = []

        # Stores (x, y)
        result = []

        # O(N * Log N)
        for point in points:
            distanceFromOrigin = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5

            heappush(distances, (distanceFromOrigin, point))

        # O(K * LogN)
        for idx in range(k):
            result.append(heappop(distances)[1])

        return result


"""
Space optimization:

Instead of maintaining a min heap of size N, use a max heap and trim the first (N-K) elements
This would result in the k min elements in construction of heap in O(N * LogK) and result creation in O(K * LogK)
"""