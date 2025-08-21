"""
Name: Reorganize String (#767)
URL: https://leetcode.com/problems/reorganize-string/

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:

        # Calculate frequency
        freq_map = {}

        for ch in s:
            if ch not in freq_map:
                freq_map[ch] = 0

            freq_map[ch] += 1

            if freq_map[ch] > (len(s) + 1) // 2:
                return ""


        # Create max heap
        max_heap = []

        for key, val in freq_map.items():
            heapq.heappush(max_heap, (-val, key))

        # Pop heap till its empty and keep concatting the top 2 most freq elements
        result = ''

        while max_heap:
            max_freq_node = heapq.heappop(max_heap)
            result += max_freq_node[1]

            second_max_freq_node = None
            if len(max_heap):
                second_max_freq_node = heapq.heappop(max_heap)
                result += second_max_freq_node[1]

            if (-max_freq_node[0] - 1 > 0):
                heapq.heappush(max_heap, (max_freq_node[0] + 1, max_freq_node[1]))

            if (second_max_freq_node and -second_max_freq_node[0] - 1 > 0):
                heapq.heappush(max_heap, (second_max_freq_node[0] + 1, second_max_freq_node[1]))
        
        return result