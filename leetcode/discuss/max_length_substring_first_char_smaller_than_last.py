"""
Link : https://leetcode.com/discuss/post/6381275/google-l4-phone-screen-by-anonymous_user-ript/

Question: 
Find maximum length of a substring of a string with first charachter of the substring is lexicographically smaller than the last charachter of the substring.
assume string length 10^5 char long, assume 26 small case english letters in string
solve it in linear time.
"""

class Solution:
    def __init__(self):
        pass

    def max_substring(self, s):
        max_right = [0] * len(s)
        max_so_far = 0

        for idx, ch in enumerate(reversed(s)):
            end_idx = -1 - idx

            max_so_far = max(max_so_far, ord(ch))
            max_right[end_idx] = max_so_far

        left = right = 0
        result = 0

        while right < len(s):
            while left < right and ord(s[left]) >= max_right[right]:
                left += 1

            result = max(result, right - left + 1)  

            right += 1
        
        return result