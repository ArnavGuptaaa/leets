"""
Name: Majority Element (#169)
URL: https://leetcode.com/problems/majority-element/
"""

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def map_solution(self, nums):
        seen = {}

        for idx in range(len(nums)):
            num = nums[idx]

            if num not in seen:
                seen[num] = 0

            seen[num] += 1

            if seen[num] > (len(nums) / 2):
                return num

        return -1 

    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def boyer_moore(self, nums):
        result = 0
        count = 0

        for num in nums:
            if result == num:
                count += 1

            elif count == 0:
                result = num 
                count += 1

            else:
                count -= 1

        return result

    def majorityElement(self, nums: List[int]) -> int:
        return self.boyer_moore(nums)
        # return self.map_solution(nums)