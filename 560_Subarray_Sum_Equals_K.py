"""
Name: Subarray Sum Equals K (#560)
URL: https://leetcode.com/problems/subarray-sum-equals-k/description/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        res = 0
        currSum = 0

        # Add 0 in map so that first target hit gets registered
        diffFreq = {0: 1}

        for num in nums:
            # Calculate running sum
            currSum += num

            # Calculate the diff required to meet the target
            diff = currSum - target

            # If diff exists in diffFreq map, update result with its count
            freqOfDiff = diffFreq.get(diff, 0)
            res += freqOfDiff

            # Update running sum frequency in diffFreq map for future lookup
            diffFreq[currSum] = diffFreq.get(currSum, 0) + 1

        return res