"""
Name: 3Sum (#15)
URL: https://leetcode.com/problems/3sum

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Time: O(N.LogN)
        nums.sort()

        for idx, num in enumerate(nums):
            if idx != 0 and num == nums[idx - 1]:
                continue

            target = -num

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                localSum = nums[left] + nums[right]

                if localSum < target:
                    left += 1
                elif localSum > target: 
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])    

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1

        return res