"""
Name: Longest Palindromic Substring (#5)
URL: https://leetcode.com/problems/longest-palindromic-substring/

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0

        def check_palindrome(left, right):
            nonlocal res_len
            nonlocal res

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res = s[left : right + 1]
                    res_len = right - left + 1

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