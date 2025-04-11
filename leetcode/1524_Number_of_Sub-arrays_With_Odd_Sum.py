"""
Name: Number of Sub-arrays With Odd Sum (#1524)
URL: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        running_sum = 0
        even_sums = 1
        odd_sums = 0
        result = 0

        for idx in range(len(arr)):
            running_sum += arr[idx]

            # Odd
            if running_sum % 2:
                result += even_sums
                odd_sums += 1

            # Even
            else:
                result += odd_sums
                even_sums += 1

            result %= (10 ** 9) + 7
            
        return result