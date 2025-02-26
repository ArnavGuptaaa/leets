"""
Name: Generate Parentheses (#22)
URL: https://leetcode.com/problems/generate-parentheses

Time Complexity: O(2^N)
Space Complexity: O(N)
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        # ===
        def parenthesisHelper(openBrackets, closedBrackets):
            if openBrackets == n and closedBrackets == n:
                res.append(''.join(path))
                return 
            
            if openBrackets < n:
                path.append('(')
                parenthesisHelper(openBrackets + 1, closedBrackets)
                path.pop()
            
            if closedBrackets < openBrackets:
                path.append(')')
                parenthesisHelper(openBrackets, closedBrackets + 1)
                path.pop()

        # ===
        parenthesisHelper(0, 0)  
        return res   