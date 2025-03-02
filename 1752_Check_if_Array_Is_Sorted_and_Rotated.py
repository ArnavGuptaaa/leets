"""
Name: Check if Array Is Sorted and Rotated (#1752)
URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        doesPeakExist = False

        for idx in range(1, len(nums)):
            # Record a peak value with doesPeakExist
            if nums[idx - 1] > nums[idx] and not doesPeakExist:
                doesPeakExist = True

            # If peak already exists, and other peak is found,
            # Array is unsorted
            elif nums[idx - 1] > nums[idx]:
                return False

        # If one peak exists, check for last index peak
        # Else, no peak exists, then array is sorted => return True
        return nums[-1] <= nums[0] if doesPeakExist else True

"""
Cases:

- There might be unsorted input arrays
    - If its unsorted, then array may have multiple peaks
        - Peaks might be present on the last index
            - e.g. [2, 1, 3, 4] => Peak at 2=>1 and 4=>2 (In rotated fashion)
- There might be a sorted input array
    - i.e. there are no peaks in the array
"""