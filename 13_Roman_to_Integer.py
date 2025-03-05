"""
Name: Roman to Integer (#13)
URL: https://leetcode.com/problems/roman-to-integer/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": (1, 0),
            "V": (5, 1),
            "X": (10, 2),
            "L": (50, 3),
            "C": (100, 4),
            "D": (500, 5),
            "M": (1000, 6)
        }

        res = 0
        [valSoFar, prevRank] = symbols[s[0]]

        for ch in s[1:]:
            (value, rank) = symbols[ch]

            if prevRank == rank:
                valSoFar += value

            elif prevRank > rank:
                res += valSoFar
                valSoFar = value
            
            else:
                valSoFar = value - valSoFar

            prevRank = rank
        
        res += valSoFar
        return res