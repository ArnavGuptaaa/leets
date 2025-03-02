"""
Name: Maximum Subarray (#53)
URL: https://leetcode.com/problems/maximum-subarray/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = globalMax = nums[0]

        for num in nums[1:]:
            # At every point we only want to qualify the bigger sum
            currentMax = max(currentMax + num, num)

            # After every comparison, we need to update the result with max sub array sum
            globalMax = max(globalMax, currentMax)

        return globalMax


"""
Thought process + Intuition to use Kadane's Algorithm

Since the array consist of negative numbers,
There might be cases where the those might be a part of the result array
    - [2, -1, 10]
    Here initially, it might feel that we want to eliminate -1,
    However including it will result in 11 as total sum

To tackle this, we need to track if a sub array can produce a net positive / larger value
Which can be used later on

Hence, at a certain point, we might need to check if current number is greater than the sum
with previously tracked elements.
    - [2, -1, 10]
    Here, when at -1, 2 and -1 create a net +ve / larger value
    - [-2, -1, 10]
    Here, when at -1, -2 and -1 create a net -ve / lower value hence, we choose to qualify only -1

As we proceed, we need to update the max value of each comparison to a result variable
"""