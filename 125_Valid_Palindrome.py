"""
Name: Valid Palindrome (#125)  
URL: https://leetcode.com/problems/valid-palindrome/  

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def generateAlphaNumericString(self, s): 
        s = s.lower()
        res = ''

        for ch in s:
            if(
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9')
            ):
                res += ch

        return res

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        alphaNumericString = self.generateAlphaNumericString(s)

        firstIndex = 0
        lastIndex = len(alphaNumericString) - 1

        while firstIndex < lastIndex:
            if alphaNumericString[firstIndex] != alphaNumericString[lastIndex]:
                return False

            firstIndex += 1
            lastIndex -= 1
        
        return True