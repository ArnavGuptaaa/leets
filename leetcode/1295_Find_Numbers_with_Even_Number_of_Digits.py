"""
Name: Find Numbers with Even Number of Digits (#1295)
URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            str_num = str(num)

            if not len(str_num) % 2:
                result += 1

        return result