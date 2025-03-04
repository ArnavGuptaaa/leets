"""
Name: Kth Largest Element in an Array (#215)
URL: <Add question link here>

Time Complexity: O(N + (N - K) * LogN)
Space Complexity: O(1)
"""

from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min heap => O(N)
        heapify(nums)

        # Remove first N-K elements
        # O((N - K) * LogN)
        while len(nums) > k:
            heappop(nums)

        return nums[0]