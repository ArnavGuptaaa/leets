"""
Name: Shortest Path in Undirected (#GFG)
URL: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/0

Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""

class Solution:
    def shortestPath(self, adj, src):
        # Step 1: Create an adj list
        adj_map = { node: set() for node in range(len(adj)) }
        
        for u in range(len(adj)):
            for v in adj[u]:
                adj_map[u].add(v)
                adj_map[v].add(u)
        
        # Step 2: Perform BFS. BFS because all the upcoming nodes would be somewhat in an order of distances

        # NOTE: visited set can be dropped since dist arr will handle the visited tracking part
        visited = set()
        node_queue = deque()
        dist = [float('inf')] * len(adj_map.keys())
        dist[src] = 0
        node_queue.append(src)
        
        while node_queue:
            v = node_queue.popleft()
            visited.add(v)
            
            for nei in adj_map[v]:
                if nei not in visited and dist[v] + 1 < dist[nei]:
                    dist[nei] = dist[v] + 1
                    node_queue.append(nei)
        
        # Step 3: Update Distances
        for idx in range(len(dist)):
            if dist[idx] == float('inf'):
                dist[idx] = -1
                
        return dist