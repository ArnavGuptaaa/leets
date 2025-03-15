"""
Name: Largest Rectangle in Histogram (#84)
URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    # O(N)
    def previous_smaller(self, heights):
        out = [0] * len(heights) 
        stack = []

        for idx in range(0, len(heights)):
            height = heights[idx]

            while stack and height <= heights[stack[-1]]:
                stack.pop()

            out[idx] = stack[-1] if stack else -1

            stack.append(idx)
        
        return out
    
    # O(N)
    def next_smaller(self, heights):
        out = [0] * len(heights) 
        stack = []

        for idx in range(len(heights) - 1, -1, -1):
            height = heights[idx]

            while stack and height <= heights[stack[-1]]:
                stack.pop()

            out[idx] = stack[-1] if stack else len(heights)

            stack.append(idx)
        
        return out

    # O(N)
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        prev_smaller = self.previous_smaller(heights)
        next_smaller = self.next_smaller(heights)

        for idx, h in enumerate(heights):
            left = prev_smaller[idx]
            right = next_smaller[idx]

            width = right - left - 1

            max_area = max(max_area, h * width)

        return max_area