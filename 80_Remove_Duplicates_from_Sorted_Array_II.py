"""
Name: Remove Duplicates from Sorted Array II (#80)
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        write_ptr = 0

        for idx in range(1, len(nums)):
            num = nums[idx]

            if num == nums[write_ptr]:
                count += 1
            else:
                count = 1

            if count < 3:
                write_ptr += 1
                nums[write_ptr] = num

        return write_ptr + 1