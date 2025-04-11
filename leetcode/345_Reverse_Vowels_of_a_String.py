"""
Name: Reverse Vowels of a String (#345)
URL: https://leetcode.com/problems/reverse-vowels-of-a-string/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        char_list = list(s)
        vowels = 'aeiouAEIOU'

        left = 0
        right = len(char_list) - 1

        while left < right:
            if char_list[left] in vowels and char_list[right] in vowels:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
                continue

            if char_list[left] not in vowels:
                left += 1

            if char_list[right] not in vowels:
                right -= 1
        
        return "".join(char_list)
