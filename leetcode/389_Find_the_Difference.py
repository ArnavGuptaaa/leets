"""
Name: Find the Difference (#389)
URL: https://leetcode.com/problems/find-the-difference/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = sum([ord(ch) - ord('a') for ch in s])
        sum_t = sum([ord(ch) - ord('a') for ch in t])

        diff = sum_t - sum_s

        return chr(ord('a') + diff)