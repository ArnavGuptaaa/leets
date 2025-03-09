"""
Name: Palindrome Partitioning (#131)
URL: https://leetcode.com/problems/palindrome-partitioning/

Time Complexity: O(N*2^N)
Space Complexity: O(2^N)
"""

class Solution:
    def isPalindrome(self, string, start, end):
        if not string:
            return False

        strLen = len(string)

        if strLen == 0 or strLen == 1:
            return True

        while start <= end:
            if string[start] != string[end]:
                return False
            
            start += 1
            end -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        # ===
        def partitionHelper(startIndex):
            if startIndex == len(s):
                res.append(path.copy())
                return
            
            for idx in range(startIndex, len(s)):
                if not self.isPalindrome(s, startIndex, idx):
                    continue 
                
                path.append(s[startIndex:idx+1])
                partitionHelper(idx + 1)
                path.pop()
                
        # ===
        partitionHelper(0)

        return res