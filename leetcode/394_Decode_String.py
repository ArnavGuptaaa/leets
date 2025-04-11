"""
Name: Decode String (#394)
URL: https://leetcode.com/problems/decode-string/

Time Complexity: O(N * K) [K : Maximum nesting]
Space Complexity: O(N)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        multipliers = []
        characters = []
        multiplier = 0

        for ch in s:
            if ch.isnumeric():
                multiplier = (10 * multiplier) + int(ch)

            if ch.isalpha():
                characters.append(ch)

            if ch == '[':
                characters.append(ch)
                multipliers.append(multiplier)

                multiplier = 0

            if ch == ']':
                string = ''
                num = multipliers.pop()

                while characters[-1] != '[':
                    string = characters.pop() + string
                
                characters.pop()
                characters.append(string * num)
            
        return "".join(characters)


# Optimized for space
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue

            substring = ''

            while stack and stack[-1] != '[':
                substring = stack.pop() + substring

            stack.pop()

            multiplier = ''

            while stack and stack[-1].isnumeric():
                multiplier = stack.pop() + multiplier

            stack.append(int(multiplier) * substring)
        
        return "".join(stack)