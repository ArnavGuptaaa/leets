"""
Name: Kth Smallest (#GFG)
URL: https://www.geeksforgeeks.org/problems/kth-smallest-element5635/

Time Complexity: O(NLogK)
Space Complexity: O(K)
"""

from heapq import heappush, heappop

class Solution:
    # N Log K
    def kthSmallest(self, arr,k):
        max_heap = []
        
        for num in arr:
            heappush(max_heap, -1 * num)
            
            while len(max_heap) > k:
                heappop(max_heap)
                
        return -1 * max_heap[0]