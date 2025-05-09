"""
Name: The k-th Lexicographical String of All Happy Strings of Length n (#1415)
URL: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

Time Complexity: O(2^length)
Space Complexity: O(length)
"""

class Solution:
    def getHappyString(self, length: int, k: int) -> str:
        
        def backtrack(idx, path):
            if len(path) == length:
                nonlocal k

                if k == 1:
                    result = "".join(path)
                    return result

                k -= 1
                return None

            for ch in allowed_characters:
                if idx != 0 and ch == path[idx - 1]:
                    continue

                result = backtrack(idx + 1, path + [ch])

                if result: 
                    return result

        allowed_characters = ['a', 'b', 'c']
        result = backtrack(0, [])

        return result if result != None else ""