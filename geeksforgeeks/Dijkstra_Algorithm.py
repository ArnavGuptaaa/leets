"""
Name: Dijkstra Algorithm (#GFG)
URL: https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

Time Complexity: O((V+E)*LogV)
Space Complexity: O(V + E)
"""

class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Step 1: Create an adj list
        adj_map = { node: set() for node in range(len(adj)) }
        
        for u in range(len(adj)):
            for v, wt in adj[u]:
                adj_map[u].add((v, wt))
                adj_map[v].add((u, wt))
                
        # Step 2: initialize minHeap and dist arr
        minHeap = []
        dist = [float('inf')] * len(adj_map.keys())
        
        # Step 3: start push source on minHeap and set dist to 0
        heapq.heappush(minHeap, (0, src))
        dist[src] = 0
        
        # Keep popping the min distance 
        while minHeap:
            d, node = heapq.heappop(minHeap)
            
            for dst, wt in adj_map[node]:
                
                if d + wt < dist[dst]:
                    dist[dst] = d + wt
                    
                    # Every time a new shorter distance is found, push to heap
                    heapq.heappush(minHeap, (dist[dst], dst))
                    
        dist = [d if d != float('inf') else -1 for d in dist]
        
        # return distance
        return dist