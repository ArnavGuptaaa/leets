"""
Name: Solving Questions With Brainpower (#2140)
URL: https://leetcode.com/problems/solving-questions-with-brainpower/

Time Complexity: O(N)
Space Complexity: O(N + N)
"""

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = [-1] * len(questions)

        def dp(index):
            if index >= len(questions):
                return 0

            if cache[index] != -1:
                return cache[index]
            
            choose = questions[index][0] + dp(index + questions[index][1] + 1)
            leave = dp(index + 1)

            cache[index] = max(choose, leave)

            return cache[index]

        return dp(0)