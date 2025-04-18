"""
Name: Letter Combinations of a Phone Number (#17)
URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Time Complexity: O(4^N)
Space Complexity: O(4^N)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(idx, path):
            if idx == len(digits):
                nonlocal result 
                if path: result.append(path[:])

                return 

            for ch in key_mapping[digits[idx]]:
                path += ch
                backtrack(idx + 1, path)

                path = path[:-1]

        backtrack(0, '')

        return result