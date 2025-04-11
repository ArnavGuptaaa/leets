"""
Name: Count Symmetric Integers (#2843)
URL: https://leetcode.com/problems/count-symmetric-integers/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for num in range(low, high + 1):
            if 10 <= num <= 99 and num % 11 == 0:
                result += 1
            
            elif 1000 <= num <= 9999:
                str_num = str(num)
                str_first_sum = sum([int(ch) for ch in str_num[:2]])
                str_last_sum = sum([int(ch) for ch in str_num[2:]])

                if str_first_sum == str_last_sum:
                    result += 1

        return result 