"""
Link: https://leetcode.com/discuss/post/6294044/google-phone-screen-by-anonymous_user-9egl/

Question:

You are given a string expression consisting of lowercase variables ('a' to 'z'), '+', '-', and parentheses '(' and ')'. 
Each variable appears as a standalone character. The expression may contain only one level of parentheses — no nesting.
Your task is to simplify the expression by combining like terms and removing any redundant parentheses, 
while keeping the result in lexicographical order of variables.
"""

class Solution:
    def __init__(self):
        pass

    def simplify_expression(self, expression):
        sign_stack = [1]
        current_sign = 1

        is_within_bracket = False
        outer_bracket_sign = True
        
        characters = [0] * 26

        for ch in expression:
            if ch == '-':
                current_sign = -1

            elif ch == '+':
                current_sign = 1

            elif ch == '(':
                sign_stack.append(sign_stack[-1] * current_sign)
                current_sign = 1

            elif ch == ')':
                sign_stack.pop()

            else:    
                characters[ord(ch) - ord('a')] += sign_stack[-1] * current_sign
                current_sign = 1


        result = ''
        for idx in range(len(characters)):
            ch = chr(idx + ord('a'))
            multiple = characters[idx]

            if multiple == 0:
                continue

            if abs(multiple) > 1:
                result += f'+{multiple}{ch}' if multiple > 0 else f'{multiple}{ch}'

            else:
                result += f'+{ch}' if multiple == 1 else f'-{ch}'

        
        if len(result) > 0 and result[0] == '+':
            return result[1:]

        return result

# Test
sol = Solution()

print(sol.simplify_expression("x-(y+z)+x"))



# Test cases
test_cases = [
    ("a+b+a", "2a+b"),
    ("-a-b-c", "-a-b-c"),
    ("a+(b+c+d)+e", "a+b+c+d+e"),
    ("a-(b+c-d)+e", "a-b-c+d+e"),
    ("a-b+a+b-c+c", "2a"),
    ("a", "a"),
    ("a-b-b-b", "a-3b"),
    ("z+y+x+a+b+c", "a+b+c+x+y+z"),
    ("a-(b+c)+(d-e)-f+g", "a-b-c+d-e-f+g"),
    ("a-b+(b-a)", ""),
    ("x-(y+z)+x", "2x-y-z"),
    ("a-b-(c+d-(a+b))", "2a-c-d") # Multi level
]

sol = Solution()

for expr, expected in test_cases:
    output = sol.simplify_expression(expr)
    print(f"===\nInput: {expr}\nOutput: {output}\nExpected: {expected}\nMatch: {output == expected}\n")