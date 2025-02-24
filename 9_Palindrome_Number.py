"""
Name: Palindrome Number (#9)
URL: https://leetcode.com/problems/palindrome-number/

Integer Math:
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def stringPalindrome(self, x):
        if x < 0:
            return False

        numStr = str(x)

        if len(numStr) == 1:
            return True

        left = 0
        right = len(numStr) - 1

        while left < right:
            if numStr[left] != numStr[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
    
    def intPalindrome(self, x):
        if x < 0:
            return False
        
        if x == 0 :
            return True
        
        numCopy = x
        revNum = 0

        while numCopy > 0:
            revNum = (revNum * 10) + (numCopy % 10)
            numCopy = numCopy

        return revNum == x

    def isPalindrome(self, x: int) -> bool:
        # return self.stringPalindrome(x)
        return self.intPalindrome(x)