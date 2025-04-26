"""
Name: Word Break (#139)
URL: https://leetcode.com/problems/word-break/

Time Complexity: O(N * M * L) [N = length of the input string s; M = number of words in wordDict; L = average length of words in wordDict]
    
Space Complexity: O(N)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dp(idx):
            if idx in cache:
                return cache[idx]

            if idx == len(s):
                return True

            can_break = False

            for word in wordDict: 
                if idx + len(word) > len(s):
                    continue

                if s[idx: idx + len(word)] == word:
                    can_break = can_break or dp(idx + len(word))

            cache[idx] = can_break
            return cache[idx]

        return dp(0)