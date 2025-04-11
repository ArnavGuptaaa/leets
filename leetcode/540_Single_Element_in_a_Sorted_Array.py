"""
Name: Single Element in a Sorted Array (#540)
URL: https://leetcode.com/problems/single-element-in-a-sorted-array/

Time Complexity: O(LogN)
Space Complexity: O(1)
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            # Mid is even
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid + 2

                else:
                    end = mid
            
            # Mid is odd
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid + 1

                else:
                    end = mid
        
        return nums[end]

"""
Intuition behind this problem is that 

consider an ideal case where all elements are perfect pairs of 2

Arr = [0,0,1,1,2,2]
Idx = [0,1,2,3,4,5]

Here, the pairs happen on following indexes (even, odd)

Now in the given scenario, there will be a deviance from this behaviour.
Hence the mid COULD be off.

Pseudocode:
while start < end:
    if mid is even:
        If yes:
            check if elem[mid] == elem[mid + 1]:
                if yes:
                    move start to mid + 2
                else:
                    move end to mid
        
        Else:
            check if elem[mid] == elem[mid - 1]:
                if yes:
                    move start to mid + 1
                else:
                    move end to mid
        
answer will occour at start == end
"""