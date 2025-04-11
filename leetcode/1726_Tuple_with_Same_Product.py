"""
Name: Tuple with Same Product (#1726)
URL: https://leetcode.com/problems/tuple-with-same-product/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Stores product => count
        product_map = {}
        res = 0

        # Store every unique pair against product
        # O(N^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]

                if product not in product_map:
                    product_map[product] = 0

                product_map[product] += 1

        # Calculate the number of valid pairs
        # O(N)
        for product in product_map.keys():
            count = product_map[product]

            if count < 2:
                continue

            # combinations from count = C(count, 2)
            combinations = (count * (count - 1)) >> 1

            """
            Each unique combination can be arranged in 8 ways

            (a,b,c,d)
            (a,b,d,c)
            (b,a,c,d)
            (b,a,d,c)
            (c,d,a,b)
            (c,d,b,a)
            (d,c,a,b)
            (d,c,b,a)
            """
            res += combinations * 8

        return res