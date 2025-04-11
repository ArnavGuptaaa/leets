"""
Name: Product of Array Except Self (#238)  
URL: https://leetcode.com/problems/product-of-array-except-self/  

Time Complexity: O(N)  
Space Complexity: O(N)
"""

class Solution:
    def getProductOfArrayElements(self, arr, indexToIgnore):
        product = 1

        for (idx, num) in enumerate(arr):
            if indexToIgnore != -1 and idx == indexToIgnore:
                continue
            
            product = product * num

        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeroIndex = -1

        for (idx, num) in enumerate(nums):
            if num == 0:
                if zeroIndex == -1:
                    zeroIndex = idx
                else:
                    return [0] * len(nums)
        
        numProduct = self.getProductOfArrayElements(nums, zeroIndex)
        
        for (idx, num) in enumerate(nums):
            if zeroIndex != -1:
                if zeroIndex != idx:
                    res.append(0)
                else:
                    res.append(numProduct)
            else:
                res.append(numProduct // num)

        return res