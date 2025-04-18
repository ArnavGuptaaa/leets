"""
Name: Count and Say (#38)
URL: https://leetcode.com/problems/count-and-say/

Time Complexity: O(N * M) [N : Number of terms to generate; M : Average length of the strings]
Space Complexity: O(M)
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        def get_rle_frequency(s):
            count = 0
            prev_ch = None
            output = []

            for idx in range(len(s)):
                ch = s[idx] 

                if not prev_ch:
                    count = 1

                elif prev_ch == ch:
                    count += 1

                else:
                    output.append((count, prev_ch))
                    count = 1

                
                prev_ch = s[idx]

            output.append((count, prev_ch))

            return output

        # ===
        def get_rle_string(freq_arr):
            output = ""

            for idx in range(len(freq_arr)):
                freq, ch = freq_arr[idx]

                output += f"{freq}{ch}"

            return output

        # ===
        result = "1"
        for _ in range(1, n):
            result = get_rle_string(get_rle_frequency(result))

        return result