"""
Name: Longest Substring Without Repeating Characters (#3)
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time Complexity: O(N)
Space Complexity: O(1) [Since we arent storing any duplicates in the dictionary]
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringSeen = {}
        left = right = res = 0

        while right < len(s):
            while s[right] in substringSeen:
                del substringSeen[s[left]]
                left += 1

            substringSeen[s[right]] = 1
            res = max(res, right - left + 1)
            right += 1
        
        return res