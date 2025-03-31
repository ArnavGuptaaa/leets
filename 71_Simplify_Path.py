"""
Name: Simplify Path (#71)
URL: https://leetcode.com/problems/simplify-path/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        ignore = ["", ".", ".."]
        stack = []

        for file_or_dir in split_path:
            if file_or_dir == ".." and len(stack) > 0:
                stack.pop()

            elif file_or_dir not in ignore:
                stack.append(file_or_dir)

        return '/' if len(stack) == 0 else "/" + "/".join(stack)