"""
Name: Next Permutation (#31)
URL: https://leetcode.com/problems/next-permutation/

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse_nums(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        dip_idx = -1
        # Find the dip
        for idx in range(len(nums) - 2, -1 ,-1):
            if nums[idx] < nums[idx + 1]:
                dip_idx = idx
                break

        # If dip not found, then array is sorted, hence next permutation is reverse
        # Example => [3,2,1]
        if dip_idx == -1:
            reverse_nums(0, len(nums) - 1)
            return

        swap_idx = -1
        # Find element just greater than the dip
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] > nums[dip_idx]:
                swap_idx = idx
                break

        # Swap with the dip
        nums[dip_idx], nums[swap_idx] = nums[swap_idx], nums[dip_idx]

        # Sort the sub array
        reverse_nums(dip_idx + 1, len(nums) - 1)