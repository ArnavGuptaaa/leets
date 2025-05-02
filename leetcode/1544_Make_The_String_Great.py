"""
Name: Make The String Great (#1544)
URL: https://leetcode.com/problems/make-the-string-great/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def makeGood(self, s: str) -> str:
        def is_same_letter(ch_1, ch_2):
            return (
                ord(ch_1) - ord('a') == ord(ch_2) - ord('A') or
                ord(ch_1) - ord('A') == ord(ch_2) - ord('a')
            )

        stack = []

        idx = 0
        while idx < len(s):
            ch = s[idx]

            if stack and is_same_letter(stack[-1], ch):
                stack.pop()
                idx += 1
                continue

            stack.append(ch)
            idx += 1

        return "".join(stack)
