"""
Name: Course Schedule II (#210)
URL: https://leetcode.com/problems/course-schedule-ii/

DFS
Time Complexity: O(V + E) 
Space Complexity: O(V + E) 

Topological Sort
Time Complexity: O(V + E) 
Space Complexity: O(V + E) 
"""

class Solution:
    def dfsHelper(self, key, adjacency, nodeStates, orderStack):
        # If node is already being visited in DFS, there exists a cycle
        if nodeStates[key] == 1:
            return False
        
        # If node was already visited, then return True
        if nodeStates[key] == 2:
            return True
        
        # Mark node as being visited
        nodeStates[key] = 1

        for node in adjacency[key]:
            if self.dfsHelper(node, adjacency, nodeStates, orderStack) == False:
                return False
        
        # Mark node as visited
        nodeStates[key] = 2
        orderStack.append(key)
        return True

    def dfsOrder(self, numCourses, prerequisites):
        # For (a, b) one would need to complete B first, in order to complete A
        # Hence, we could make an edge like so : B => A

        # Prepare Adjacency List
        adjacency = { c: [] for c in range(numCourses) }
        for p in prerequisites:
            adjacency[p[1]].append(p[0])

        nodeStates = [0] * numCourses
        orderStack = []

        for key in adjacency:
            if self.dfsHelper(key, adjacency, nodeStates, orderStack) == False:
                return []
            
        return orderStack[::-1]
        
        
    def topologicalOrder(self, numCourses, prerequisites):
        # For (a, b) one would need to complete B first, in order to complete A
        # Hence, we could make an edge like so : B => A

        # Prepare Adjacency List
        adjacency = { c: [] for c in range(numCourses) }
        for p in prerequisites:
            adjacency[p[1]].append(p[0])
        
        # The objective is to return linear ordering, 
        # Hence we can employ topological sort

        # Prepare indegrees
        indegrees = { c: 0 for c in range(numCourses) }
        for key in adjacency:
            for node in adjacency[key]:
                indegrees[node] = indegrees.get(node, 0) + 1
        
        # Prepare queue with 0 indegrees
        nodeQueue = []
        for key in adjacency.keys():
            if indegrees[key] == 0:
                nodeQueue.append(key)
        
        # Prepare topological linear ordering
        topo = []
        while nodeQueue:
            node = nodeQueue.pop(0)
            topo.append(node)

            for neighbor in adjacency[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    nodeQueue.append(neighbor)
        
        # Topological sort generates a linear ordering of size N
        # IFF there are no cycles. (Draw this on a graph)
        if len(topo) != numCourses:
            return []
        
        return topo

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return self.topologicalOrder(numCourses, prerequisites)
        return self.dfsOrder(numCourses, prerequisites)