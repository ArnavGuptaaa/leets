"""
Name: Path with Maximum Probability (#1514)
URL: https://leetcode.com/problems/path-with-maximum-probability/

Time Complexity: O((V+E)LogV)
Space Complexity: O(V + E)
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = { node: set() for node in range(n) }

        for idx, edge in enumerate(edges):
            u, v = edge
            wt = -1 * succProb[idx]

            adj[u].add((v, wt))
            adj[v].add((u, wt))

        
        heap = []
        dist = [float('inf')] * n

        dist[start_node] = 0
        heapq.heappush(heap, (0, start_node))

        while heap:
            d, node = heapq.heappop(heap)

            d = -1 if d == 0 else d

            if d > dist[node]:
                continue

            if node == end_node:
                return -d

            for v, wt in adj[node]: 
                if -(d * wt) < dist[v]:
                    dist[v] = -(d * wt)
                    heapq.heappush(heap, (dist[v], v))

        return -1 * dist[end_node] if dist[end_node] != float('inf') else 0