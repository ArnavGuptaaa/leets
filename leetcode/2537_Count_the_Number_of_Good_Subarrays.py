"""
Name: Count the Number of Good Subarrays (#2537)
URL: https://leetcode.com/problems/count-the-number-of-good-subarrays

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = right = 0

        # Num => Occourances
        seen = {}

        good_pairs = 0
        result = 0

        while right < len(nums):
            if nums[right] not in seen:
                seen[nums[right]] = 1

            else:
                good_pairs += seen[nums[right]]
                seen[nums[right]] += 1

            while good_pairs >= k:
                result += len(nums) - right

                seen[nums[left]] -= 1
                good_pairs -= seen[nums[left]]

                if seen[nums[left]] == 0:
                    del seen[nums[left]]

                left += 1

            right += 1

        return result