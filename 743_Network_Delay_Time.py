"""
Name: Network Delay Time (#743)
URL: https://leetcode.com/problems/network-delay-time/

Time Complexity: O((V+E) LogV)
Space Complexity: O(V + E)
"""

from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        # since the graph is 1 based index
        adj_map = { node: set() for node in range(1, n + 1) }

        for u, v, wt in times:
            adj_map[u].add((v, wt))

        minHeap = []
        dist = [float('inf')] * (n + 1)

        # since the graph is 1 based index
        dist[0] = -1

        dist[src] = 0
        heappush(minHeap, (0, src)) # (distance, node)

        while minHeap:
            d, node = heappop(minHeap)

            # If we are not exploring the shortest path, then leave this path
            if d > dist[node]:
                continue

            for nei, w in adj_map[node]:

                if d + w < dist[nei]:
                    dist[nei] = d + w
                    heappush(minHeap, (dist[nei], nei))

        maxTime = max(dist)

        return -1 if maxTime == float('inf') else maxTime