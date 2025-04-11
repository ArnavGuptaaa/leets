"""
Name: 3Sum Closest (#16)
URL: https://leetcode.com/problems/3sum-closest/

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        result = -1

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                diff = abs(target - three_sum)

                if diff == 0:
                    return three_sum

                if diff < min_diff:
                    result = three_sum
                    min_diff = diff

                if three_sum < target:
                    j += 1
                else:
                    k -= 1

        return result