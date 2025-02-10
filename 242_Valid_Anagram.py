"""
Name: Valid Anagram (#242)  
URL: https://leetcode.com/problems/valid-anagram/  

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = {}
        
        for ch in s:
            if not ch in seen:
                seen[ch] = 1
            else:
                seen[ch] += 1
            
        
        for ch in t:
            if ch in seen:
                seen[ch] -= 1
            
                if seen[ch] == 0:
                    del seen[ch]
            
            else:
                return False
        
        return False if seen else True