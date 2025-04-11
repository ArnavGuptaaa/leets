"""
Name: Insert Interval (#57)
URL: https://leetcode.com/problems/insert-interval/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        res = []

        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            start = min(intervals[index][0], newInterval[0])
            end = max(intervals[index][1], newInterval[1])

            newInterval = [start, end]
            index += 1

        res.append(newInterval)

        while index < len(intervals):
            res.append(intervals[index])
            index += 1

        return res