"""
Name: Find Median from Data Stream (#295)
URL: https://leetcode.com/problems/find-median-from-data-stream/

Time Complexity: Refer Each Method
Space Complexity: O(N)
"""

from heapq import heappop, heappush

class MedianFinder:
    # O(1)
    def __init__(self):
        # Stores the greater half of elements
        self.minHeap = []

        # Stores the smaller half of elements
        self.maxHeap = []

    # O(LogN)
    def balance(self, lenMin, lenMax):
        if abs(lenMin - lenMax) <= 1:
            return

        if lenMin > lenMax:
            elem = heappop(self.minHeap)
            heappush(self.maxHeap, -elem)

        else:
            elem = -heappop(self.maxHeap)
            heappush(self.minHeap, elem)

    # O(LogN)
    def addNum(self, elem: int) -> None:
        lenMin = len(self.minHeap)
        lenMax = len(self.maxHeap)
        
        if lenMin == 0 and lenMax == 0:
            heappush(self.minHeap, elem)
            return

        if elem < self.minHeap[0]:
            heappush(self.maxHeap, -elem)
            self.balance(lenMin, lenMax + 1)

        else:
            heappush(self.minHeap, elem)
            self.balance(lenMin + 1, lenMax)        

    # O(1)
    def findMedian(self) -> float:
        lenMin = len(self.minHeap)
        lenMax = len(self.maxHeap)

        if lenMin == lenMax:
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        
        return self.minHeap[0] if lenMin > lenMax else -self.maxHeap[0]