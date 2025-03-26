"""
Name: Shortest path in Directed Acyclic Graph (#GFG)
URL: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/0

Time Complexity: O(V+ E)
Space Complexity: O(V+ E)
"""

class Solution:
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Perform topo sort and get linear ordering
        def topoSort(node):
            visited.add(node)
            
            for v, wt in adj[node]:
                if v not in visited:
                    topoSort(v)
            
            order_stack.append(node)
        
        # Prepare adj list
        adj = { n: set() for n in range(V)}
        
        for [u, v, weight] in edges:
            adj[u].add((v, weight))
        
        order_stack = []
        visited = set()
        
        for node in adj.keys():
            if node not in visited:
                topoSort(node)
        
        # Step 2 : use linear order and relax edges
        dist = [float('inf')] * V
        dist[0] = 0
        
        while order_stack:
            node = order_stack.pop()
            
            for v, wt in adj[node]:
                dist[v] = min(dist[v], dist[node] + wt)
        
        for idx in range(len(dist)):
            if dist[idx] == float('inf'):
                dist[idx] = -1
        
        return dist