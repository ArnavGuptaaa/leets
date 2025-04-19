"""
Name: Count the Number of Fair Pairs (#2563)
URL: https://leetcode.com/problems/count-the-number-of-fair-pairs/

Time Complexity: O(N*LogN)
Space Complexity: O(1)
"""

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_sum_at_most(at_most_total):
            start = 0
            end = len(nums) - 1
            output = 0

            while start < end:
                while start < end and nums[start] + nums[end] > at_most_total:
                    end -= 1

                if start < end:
                    output += end - start
                    start += 1

            return output

        # ===
        nums.sort()
        return count_sum_at_most(upper) - count_sum_at_most(lower - 1)
