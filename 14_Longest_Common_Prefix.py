"""
Name: Longest Common Prefix (#14)
URL: https://leetcode.com/problems/longest-common-prefix/

Sorting 
Time Complexity: O(N*LogN)
Space Complexity: O(1)

Vertical Scanning
Time Complexity: O(M * N) [M : Length of strs; N: Length of shortest string in strs]
Space Complexity: O(1)
"""

class Solution:
    def verticalScanSolution(self, strs):
        if len(strs) == 0:
            return ""

        reference = strs[0]

        for idx in range(len(reference)):
            prefixSoFar = reference[idx]

            for word in strs[1:]:
                if idx >= len(word) or prefixSoFar != word[idx]:
                    return reference[:idx]
                
        return reference

    def sortSolution(self, strs):
        # Sorting => O(N*LogN)
        strs.sort()

        index = 0
        longestCommonPrefix = ''

        while index < len(strs[0]) and index < len(strs[-1]):
            if strs[0][index] != strs[-1][index]:
                break

            longestCommonPrefix += strs[0][index]
            index += 1

        return longestCommonPrefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return self.sortSolution(strs)
        return self.verticalScanSolution(strs)