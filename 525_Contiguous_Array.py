"""
Name: Contiguous Array (#525)
URL: https://leetcode.com/problems/contiguous-array/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        currSum = 0
        res = 0

        sumToIndexMap = {0: -1}

        for idx, num in enumerate(nums):
            currSum = currSum + 1 if num == 1 else currSum -1
            # diff = currSum - 0

            # If diff has occoured before, we could subtract indexes to yield max length
            if currSum in sumToIndexMap:
                # Update res if its max
                res = max(res, idx - sumToIndexMap[currSum])
            else:
                # Update the current sum in map
                sumToIndexMap[currSum] = idx 

        return res

"""
The trick here is to understand that we are aiming to balance the frequencies of 0s and 1s.
Hence, if we replace 0 with -1 then the problem gets transformed to a sum tracking problem.

Balanced Case:
[1, 0] => [1, -1] (Sum = 0)

Imbalanced Case:
[1, 1, 0] => [1, 1, -1] (Sum = 1)

Here we can see that we have a subarray that had produced 1 (Index = 0).
If that were removed then the resulting sub array would meet our requirement.
Hence, the answer would be CurrentIndex - RequiredDiffIndex (2 - 0 = 2).
"""