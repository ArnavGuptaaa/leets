"""
Name: Remove All Occurrences of a Substring (#1910)
URL: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

Time Complexity: O(M * N) [N: Length of string; M: Length of part]
Space Complexity: O(N)
"""

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_list = list(part)

        for idx in range(len(s)):
            ch = s[idx]

            stack.append(ch)

            if len(stack) >= len(part) and stack[-len(part):] == part_list:
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)