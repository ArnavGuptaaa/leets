"""
Name: Non-overlapping Intervals (#435)
URL: https://leetcode.com/problems/non-overlapping-intervals/

Time Complexity: O(N LogN)
Space Complexity: O(1)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        end = intervals[0][1]
        result = 0

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            # Non overlapping interval
            if s >= end:
                end = e
            
            # Overlapping interval
            else:
                # We choose the one with lower end 
                # Since we want to minimize the number of removals.
                # A bigger end could possible overlap with other intervals too.
                end = min(end, e)
                result += 1

        return result