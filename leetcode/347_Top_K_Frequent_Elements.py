"""
Name: Top K Frequent Elements (#347)  
URL: https://leetcode.com/problems/top-k-frequent-elements/  

Time Complexity: 

Sort: O(N * log N)  
Heap: O(N * log K)
Space Complexity: O(N)  
"""

class Solution:
    def heapSolution(self, nums, k):
        freqMap = {}
        minHeap = []

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0

            freqMap[num] += 1

        # O(N * LogK)
        for key in freqMap:
            heappush(minHeap, (freqMap[key], key))

            if len(minHeap) > k:
                heappop(minHeap)

        # O(K * LogK)
        return [value for (frequency, value) in minHeap]

    def sortSolution(self, nums, k):
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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.sortSolution(nums, k)
        return self.heapSolution(nums, k)