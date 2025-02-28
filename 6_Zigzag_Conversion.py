"""
Name: Zigzag Conversion (#6)
URL: https://leetcode.com/problems/zigzag-conversion/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        res = [''] * numRows

        index = 0
        isForward = False

        for letter in s:
            if index == 0 or index == numRows - 1:
                isForward = not isForward

            res[index] += letter

            index = index + 1 if isForward else index - 1
        
        return "".join(res)