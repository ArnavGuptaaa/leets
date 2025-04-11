"""
Name: Merge Intervals (#56)
URL: https://leetcode.com/problems/merge-intervals/

Time Complexity: O(N*LogN)
Space Complexity: O(1) [O(N) for storing in output array]
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lenInterval = len(intervals)
        
        # For just one element, the result will be same
        if lenInterval == 1:
            return intervals

        res = []

        # Sort on the first index,
        # So that we have the intervals in growing order of index
        intervals.sort(key=lambda x: x[0])

        # Track the leftmost and rightmost interval value
        leftInterval = intervals[0][0]
        rightInterval = intervals[0][1]

        for idx in range(1, lenInterval):
            currentInterval = intervals[idx]

            # If current interval has same value as left most index,
            # Then the right index need to be changed
            if currentInterval[0] == leftInterval:
                rightInterval = max(rightInterval, currentInterval[1])

            # If current interval has less value than the right most index,
            # Then the right index need to be changed
            elif currentInterval[0] <= rightInterval:
                rightInterval = max(rightInterval, currentInterval[1])

            # If left interval does not overal with the current left most and right most index
            # Add them to result list
            elif currentInterval[0] > rightInterval:
                res.append([leftInterval, rightInterval])

                # Update the new left and right most indexes
                leftInterval = currentInterval[0]
                rightInterval = currentInterval[1]
        
        # Add remaining interval indexes
        res.append([leftInterval, rightInterval])

        return res