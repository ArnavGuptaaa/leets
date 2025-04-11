"""
Name: Maximum Product Subarray (#152)
URL: https://leetcode.com/problems/maximum-product-subarray/
"""

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def modified_kadane(self, nums):
        curr_min = curr_max = global_max = nums[0]

        for num in nums[1:]:
            possible_products = [num, curr_min * num, curr_max * num]

            curr_min = min(possible_products)
            curr_max = max(possible_products)

            global_max = max(global_max, curr_max)

        return global_max

    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def product_prefix_suffix(self, nums):
        left_product = right_product = 1
        result = float('-inf')

        for idx in range(len(nums)):
            end_idx = -1 - idx

            if left_product == 0:
                left_product = 1
            
            if right_product == 0:
                right_product = 1

            left_product *= nums[idx]
            right_product *= nums[end_idx]

            result = max(result, left_product, right_product)

        return result

    def maxProduct(self, nums: List[int]) -> int:
        # return self.modified_kadane(nums)
        return self.product_prefix_suffix(nums)