"""
Name: Valid Parentheses (#20)
URL: https://leetcode.com/problems/valid-parentheses/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []

        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            
            else:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else: 
                    return False
                
        return True if len(stack) == 0 else False