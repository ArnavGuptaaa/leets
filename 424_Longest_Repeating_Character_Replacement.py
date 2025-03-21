"""
Name: Longest Repeating Character Replacement (#424)
URL: https://leetcode.com/problems/longest-repeating-character-replacement/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = res = 0
        seen = {}

        for right in range(len(s)):
            letter = s[right]

            seen[letter] = seen.get(letter, 0) + 1
            window_size = right - left + 1

            if window_size - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res