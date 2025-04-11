"""
Name: Palindromic Substrings (#647)
URL: https://leetcode.com/problems/palindromic-substrings/

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def check_palindrome(left, right):
            nonlocal res

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1

                left -= 1
                right += 1

        for idx in range(len(s)):
            # Consider idx to be middle of an odd length string
            left = idx
            right = idx

            check_palindrome(left, right)

            # Consider idx to be middle of an even length string
            left = idx
            right = idx + 1

            check_palindrome(left, right)

        return res