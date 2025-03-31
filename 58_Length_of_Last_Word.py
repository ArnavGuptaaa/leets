"""
Name: Length of Last Word (#58)
URL: https://leetcode.com/problems/length-of-last-word/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])