"""
Name: Count Number of Bad Pairs (#2364)
URL: https://leetcode.com/problems/count-number-of-bad-pairs/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        difference_to_count = {}
        good_pairs = 0

        for idx, val in enumerate(nums):
            difference = val - idx

            if difference in difference_to_count:
                good_pairs += difference_to_count[difference]
                difference_to_count[difference] += 1

            else:
                difference_to_count[difference] = 1
        
        len_nums = len(nums)
        total_pairs = len_nums * (len_nums - 1) // 2

        return total_pairs - good_pairs