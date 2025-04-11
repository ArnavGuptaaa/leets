"""
Name: Kth Largest Element in a Stream (#703)
URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Time Complexity:
__init__ : O(N + (N-K)LogN)
add : O(LogK)

Space Complexity: O(K)
"""

from heapq import heapify, heappop, heappush

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        # O(N)
        heapify(self.minHeap)

        # O((N-K) * LogN)
        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        # O(LogK)
        heappush(self.minHeap, val)

        # O(LogK)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        
        return None if len(self.minHeap) < self.k else self.minHeap[0] 