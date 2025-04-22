"""
Name: String Compression (#443)
URL: https://leetcode.com/problems/string-compression/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        start = right = 0

        while right < len(chars):

            while right < len(chars) and chars[right] == chars[start]:
                right += 1

            count = right - start
            chars[write_ptr] = chars[start]

            if count > 1:
                for ch in str(count):
                    write_ptr += 1
                    chars[write_ptr] = ch

            write_ptr += 1
            start = right

        return write_ptr