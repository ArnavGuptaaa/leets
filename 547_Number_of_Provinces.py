"""
Name: Number of Provinces (#547)
URL: https://leetcode.com/problems/number-of-provinces/

Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class DisjointSetUnion:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [node for node in range(n)]

    def find_parent(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union(self, node_1, node_2):
        parent_1 = self.find_parent(node_1)
        parent_2 = self.find_parent(node_2)

        # Belongs to same component
        if parent_1 == parent_2:
            return

        # Merge smaller component into larger component
        rank_1 = self.rank[parent_1]
        rank_2 = self.rank[parent_2]

        if rank_1 > rank_2:
            self.parent[parent_2] = parent_1
        
        elif rank_2 > rank_1:
            self.parent[parent_1] = parent_2

        else:
            self.parent[parent_2] = parent_1
            self.rank[parent_1] += 1

    def get_disconnected_components(self):
        parent_set = set()

        for p in self.parent:
            parent_set.add(self.find_parent(p))

        return len(parent_set)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dsu = DisjointSetUnion(len(isConnected))

        # O(N^2)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    dsu.union(row, col)
        
        # O(N)
        return dsu.get_disconnected_components()


"""
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
        
        # === 
        adj = {node: set() for node in range(len(isConnected))}

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if row == col or isConnected[row][col] != 1:
                    continue

                adj.get(row).add(col)

        result = 0
        visited = set()

        for node in adj.keys():
            if node not in visited:
                dfs(node)
                result += 1

        return result
        