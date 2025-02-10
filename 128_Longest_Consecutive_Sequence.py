"""
Name: Longest Consecutive Sequence (#128)  
URL: https://leetcode.com/problems/longest-consecutive-sequence/  

Time Complexity: O(N)  
Space Complexity: O(N)  
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLength = 0
        tempLength = 0

        for num in numSet:
            # Start of consecutive number
            if num - 1 not in numSet:
                tempLength = 0
                tempNum = num

                while tempNum in numSet:
                    tempNum += 1
                    tempLength += 1
                
                if tempLength > maxLength:
                    maxLength = tempLength

        return maxLength