"""
Name: Trapping Rain Water (#42)
URL: https://leetcode.com/problems/trapping-rain-water/

Two Pointer
Time Complexity: O(N)
Space Complexity: O(1)

Max Arrays
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    # Time: O(N)
    # Space: O(1)
    def twoPointer(self, height):
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        trappedWater = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    trappedWater += leftMax - height[left]
                else:
                    leftMax = height[left]
                
                left += 1
            
            else:
                if height[right] < rightMax:
                    trappedWater += rightMax - height[right]
                else:
                    rightMax = height[right]
                
                right -= 1

        return trappedWater

    # Time: O(N)
    # Space: O(N)
    def maxArray(self,height):
        if len(height) == 0:
            return 0 

        leftMax = [0] * len(height)
        leftMax[0] = height[0]

        rightMax = [0] * len(height)
        rightMax[-1] = height[-1]

        trappedWater = 0
        
        for idx in range(1, len(height)):
            leftMax[idx] = max(height[idx], leftMax[idx - 1])

        for idx in range(len(height) - 2, -1, -1):
            rightMax[idx] = max(height[idx], rightMax[idx + 1])

        for (idx, h) in enumerate(height):
            if h < leftMax[idx] and h < rightMax[idx]:
                trappedWater += min(leftMax[idx], rightMax[idx]) - h

        return trappedWater

    def trap(self, height: List[int]) -> int:
        # return self.maxArray(height)
        return self.twoPointer(height)