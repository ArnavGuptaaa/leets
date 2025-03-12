"""
Name: Online Stock Span (#901)
URL: https://leetcode.com/problems/online-stock-span/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        element = [price, 1]

        while self.stack and element[0] >= self.stack[-1][0]:
            popped_element = self.stack.pop()
            element[1] += popped_element[1]

        self.stack.append(element)

        return element[1]