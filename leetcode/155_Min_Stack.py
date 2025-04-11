"""
Name: Min Stack (#155)
URL: https://leetcode.com/problems/min-stack/

Time Complexity: O(1)
Space Complexity: O(N)
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minSoFar = float('inf')

    def push(self, val: int) -> None:
        if val < self.minSoFar:
            self.minSoFar = val
        
        self.stack.append((val, self.minSoFar))

    def pop(self) -> None:
        poppedNode = self.stack.pop()
        self.minSoFar = float('inf') if len(self.stack) == 0 else self.stack[-1][1]

        return poppedNode[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]