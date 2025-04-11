"""
Name: Last Stone Weight (#1046)
URL: https://leetcode.com/problems/last-stone-weight

Time Complexity: O(N LogN)
Space Complexity: O(1)
"""

from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(N)
        stones = [-1 * stone for stone in stones]

        # O(N)
        heapify(stones)
        
        while len(stones) > 1:
            # 2 * O(LogN)
            stone1 = -1 * heappop(stones)
            stone2 = -1 * heappop(stones)

            # O(LogN)
            if stone1 != stone2:    
                heappush(stones, -1 * (stone1 - stone2))

        return 0 if len(stones) == 0 else -1 * stones[0]  