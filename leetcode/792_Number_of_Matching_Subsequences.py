"""
Name: Number of Matching Subsequences (#792)
URL: https://leetcode.com/problems/number-of-matching-subsequences/

Time Complexity: O(W * L) [W : Length of words; L : Average length of words]
Space Complexity: O(W) [W : Length of words]
"""

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = {}
        result = 0

        for idx, word in enumerate(words):
            if word == "":
                result += 1
                continue

            if word[0] not in waiting:
                waiting[word[0]] = []

            # (Word, CurrentIndex)
            waiting[word[0]].append((word, 0))
        
        for ch in s:
            if ch in waiting:
                copy = waiting[ch]
                del waiting[ch]

                for w, idx in copy:
                    if idx == len(w) - 1:
                        result += 1
                    else:
                        if w[idx + 1] not in waiting:
                            waiting[w[idx + 1]] = []

                        waiting[w[idx + 1]].append((w, idx + 1))

        return result

"""
Each word is grouped by the next character it needs to match. (Word, CurrentIndex)

As we iterate through s, we process all words waiting for the current character and move their pointer forward. 
If a word's pointer reaches the end, it's a valid subsequence.
"""