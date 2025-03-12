"""
Name: Daily Temperatures (#739)
URL: https://leetcode.com/problems/daily-temperatures/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        for idx in range(len(temperatures)):
            temp = temperatures[idx]

            while stack and temp > stack[-1][0]:
                [t, i] = stack.pop()

                temperatures[i] = idx - i
            
            stack.append([temp, idx])

        for elem in stack:
            temperatures[elem[1]] = 0

        temperatures[-1] = 0

        return temperatures