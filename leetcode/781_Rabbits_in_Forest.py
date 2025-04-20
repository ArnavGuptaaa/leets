"""
Name: Rabbits in Forest (#781)
URL: https://leetcode.com/problems/rabbits-in-forest

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        seen = {}

        for idx in range(len(answers)):
            ans = answers[idx]

            if ans not in seen:
                if ans != 0: 
                    seen[ans] = 1

                result += ans + 1

            else:
                seen[ans] += 1

                if seen[ans] == ans + 1:
                    del seen[ans]

        return result