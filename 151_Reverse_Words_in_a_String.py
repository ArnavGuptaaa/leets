"""
Name: Reverse Words in a String (#151)
URL: https://leetcode.com/problems/reverse-words-in-a-string/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(
            [word.strip() for word in s.split(" ")[::-1] if word.strip() != ""]
        )