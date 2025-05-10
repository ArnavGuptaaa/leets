"""
Name: Unique Number of Occurrences (#1207)
URL: https://leetcode.com/problems/unique-number-of-occurrences/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num not in freq:
                freq[num] = 0

            freq[num] += 1

        return len(freq.values()) == len(set(freq.values()))