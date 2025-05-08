"""
Name: First Unique Character in a String (#387)
URL: https://leetcode.com/problems/first-unique-character-in-a-string/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 0

            seen[ch] += 1

        for idx, ch in enumerate(s):
            if seen[ch] == 1:
                return idx

        return -1