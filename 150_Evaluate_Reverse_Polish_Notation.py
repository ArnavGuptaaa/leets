"""
Name: Evaluate Reverse Polish Notation (#150)
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def handleOperation(self, num1, num2, op):
        match op:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                return int(num1 / num2)
            case default:
                raise Exception("Invalid operation " + op)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = '+-*/'
        stack = []

        for token in tokens:
            if token in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(self.handleOperation(num2, num1, token))

                continue
            
            stack.append(int(token))
        
        return stack.pop()