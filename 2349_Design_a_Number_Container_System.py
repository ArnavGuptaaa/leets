"""
Name: Design a Number Container System (#2349)
URL: https://leetcode.com/problems/design-a-number-container-system/

Time Complexity

__init__ : O(1)
change : O(LogN)
find : O(KLogN) [K: Number of Stale Indices]

Space Complexity: O(N)
"""

class NumberContainers:
    def __init__(self):
        # Index => Number
        self.index_to_number = {}

        # Number => Heap of indexes
        self.number_to_indexes = {}

    def change(self, index: int, number: int) -> None:
        # Update the index=>number mapping
        self.index_to_number[index] = number

        """
        We will directly add the index in index heap.
        This will create stale indexes. However, we plan to resolve that in find

        WHY? 
        If we removed it here, we would need to heapify the array again.
        hence adding O(N) complexity
        """

        # Insert index in number=>indexes map
        if number not in self.number_to_indexes:
            self.number_to_indexes[number] = []

        heapq.heappush(self.number_to_indexes[number], index) 

    def find(self, number: int) -> int:
        if number not in self.number_to_indexes:
            return -1

        """
        We know that 
        The min index retrieved from number_to_indexes WOULD ALWAYS point to the number

        If thats not the case (stale index), we pop it
        """
        while(
            len(self.number_to_indexes[number]) > 0 and
            number != self.index_to_number[self.number_to_indexes[number][0]]
        ):
            heapq.heappop(self.number_to_indexes[number])

        if len(self.number_to_indexes[number]) == 0:
            del self.number_to_indexes[number]
            return -1

        return self.number_to_indexes[number][0]