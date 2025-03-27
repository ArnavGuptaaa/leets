"""
Name: Cheapest Flights Within K Stops (#787)
URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Time Complexity: O(KLogV)
Space Complexity: O(V + E)
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = { node: set() for node in range(n)}
        
        for s, d, wt in flights:
            adj[s].add((d, wt))

        # (stop, distance, node)
        min_heap = [(0, 0, src)]
        dist = [float('inf')] * n

        dist[src] = 0

        while min_heap:
            s, d, node = heapq.heappop(min_heap)

            if s > k:
                continue

            for v, wt in adj[node]:
                if d + wt < dist[v]:
                    dist[v] = d + wt
                    heapq.heappush(min_heap, (s + 1, dist[v], v))

        return dist[dst] if dist[dst] != float('inf') else -1