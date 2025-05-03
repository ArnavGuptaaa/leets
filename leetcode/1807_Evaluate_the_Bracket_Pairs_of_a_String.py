"""
Name: Evaluate the Bracket Pairs of a String (#1807)
URL: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

Time Complexity: O(N)
Space Complexity: O(N + K) [K : Space for knowledge_map]
"""

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map = {}

        for [key, value] in knowledge:
            knowledge_map[key] = value

        idx = 0
        stack = []

        while idx < len(s):
            if s[idx] == '(':
                key = ''
                idx += 1

                while s[idx] != ')':
                    key += s[idx]
                    
                    idx += 1

                if key in knowledge_map:
                    stack.append(knowledge_map[key])
                else:
                    stack.append('?')

                idx += 1
                continue

            stack.append(s[idx])
            idx += 1

        return "".join(stack)