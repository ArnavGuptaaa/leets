"""
Name: Word Subsets (#916)
URL: https://leetcode.com/problems/word-subsets/

Time Complexity: O(N + M), [N : Number of characters in words1; M : Number of characters in words2]
Space Complexity: O(1)
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        freqArr = [0] * 26

        # Get frequency array of letters from words2
        for word in words2:
            wordFreqArr = [0] * 26

            # Update word frequency in a temp frequency array
            for ch in word:
                wordFreqArr[ord(ch) - ord('a')] += 1
            
            # Persist only the maximum frequency
            for idx in range(26):
                freqArr[idx] = max(freqArr[idx], wordFreqArr[idx])
        
        for word in words1:
            wordFreqArr = [0] * 26
            isUniversal = True

            # Update word frequency in a temp frequency array
            for ch in word:
                wordFreqArr[ord(ch) - ord('a')] += 1
            
            # If character frequency in a word is less then required frequency
            # Mark it unfit for being universal
            for idx in range(26):
                if wordFreqArr[idx] < freqArr[idx]:
                    isUniversal = False
            
            if isUniversal:
                res.append(word)

        return res