"""
Name: Top K Frequent Elements (#347)  
URL: https://leetcode.com/problems/top-k-frequent-elements/  

Time Complexity: O(N log N)  
Space Complexity: O(N)  
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freqArray = []
        res = []

        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else: 
                freq[num] = 1

        for key in freq.keys():
            freqArray.append((key, freq[key]))

        reverseSortedFreqArr = sorted(freqArray, key=lambda x: x[1], reverse=True)

        for n in range(k):
            res.append(reverseSortedFreqArr[n][0])

        return res