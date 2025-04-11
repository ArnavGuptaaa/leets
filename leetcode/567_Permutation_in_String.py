"""
Name: Permutation in String (#567)
URL: https://leetcode.com/problems/permutation-in-string/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)

        if s1Len > s2Len:
            return False

        freqArrS1 = [0] * 26
        freqArrS2 = [0] * 26

        for idx in range(s1Len):
            freqArrS1[ord(s1[idx]) - ord('a')] += 1
            freqArrS2[ord(s2[idx]) - ord('a')] += 1
        
        if freqArrS1 == freqArrS2:
            return True
        
        for idx in range(s1Len, s2Len):
            freqArrS2[ord(s2[idx]) - ord('a')] += 1
            freqArrS2[ord(s2[idx-s1Len]) - ord('a')] -= 1

            if freqArrS1 == freqArrS2:
                return True

        return False