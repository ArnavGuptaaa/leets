"""
Name: Find the Number of Distinct Colors Among the Balls (#3160)
URL: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_to_balls = {}
        ball_to_color = {}

        result = []

        for ball, color in queries:
            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                color_to_balls[prev_color] -= 1

                if color_to_balls[prev_color] == 0:
                    del color_to_balls[prev_color]
            
            ball_to_color[ball] = color

            if color not in color_to_balls:
                color_to_balls[color] = 0

            color_to_balls[color] += 1

            result.append(len(color_to_balls.keys()))

        return result