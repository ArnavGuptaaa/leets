"""
Name: Count Complete Subarrays in an Array (#2799)
URL: https://leetcode.com/problems/count-complete-subarrays-in-an-array/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_nums = len(set(nums))

        seen = {}
        left = right = 0
        result = 0

        while right < len(nums):
            seen[nums[right]] = seen.get(nums[right], 0) + 1

            while len(seen.keys()) == distinct_nums:
                result += len(nums) - right
                seen[nums[left]] -= 1

                if seen[nums[left]] == 0:
                    del seen[nums[left]]

                left += 1

            right += 1

        return result