"""
Name: Parenthesis Checker (#GFG)
URL: https://www.geeksforgeeks.org/problems/parenthesis-checker2744/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def isBalanced(self, s):
        reverse_mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack = []
        
        for ch in s:
            # Add opening brackets to stack
            if ch not in reverse_mapping:
                stack.append(ch)
            
            # Closing bracket 
            else:
                if stack and reverse_mapping[ch] == stack[-1]:
                    stack.pop()
                    
                else:
                    return False

        # [()
        return len(stack) == 0