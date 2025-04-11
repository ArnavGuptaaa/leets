"""
Name: Course Schedule (#207)
URL: https://leetcode.com/problems/course-schedule/

DFS
Time Complexity: O(V + E) 
Space Complexity: O(V + E) 

Topological Sort
Time Complexity: O(V + E) 
Space Complexity: O(V + E) 
"""

class Solution:
    def dfsHelper(self, key, adjacency, nodeStates):
        if nodeStates[key] == 1:
            return False
        
        if nodeStates[key] == 2:
            return True

        nodeStates[key] = 1

        for node in adjacency[key]:
            if self.dfsHelper(node, adjacency, nodeStates) == False:
                return False

        nodeStates[key] = 2
        return True

    def canFinishDfs(self, numCourses, prerequisites):
        # Create Adjacency
        adjacency = { c: [] for c in range(numCourses) }
        for courses in prerequisites:
            adjacency[courses[1]].append(courses[0])

        nodeStates = [0] * numCourses

        for key in adjacency:
            if self.dfsHelper(key, adjacency, nodeStates) == False:
                return False

        return True

    def canFinishTopological(self, numCourses, prerequisites):
        # Create Adjacency
        adjacency = { c: [] for c in range(numCourses) }
        for courses in prerequisites:
            adjacency[courses[1]].append(courses[0])

        # Create indegrees
        indegrees = { c: 0 for c in range(numCourses) }
        for key in adjacency:
            for node in adjacency[key]:
                indegrees[node] += 1

        # Create nodeQueue with nodes with 0 indegrees
        nodeQueue = []
        for key in indegrees:
            if indegrees[key] == 0:
                nodeQueue.append(key)
        
        # count the courses
        count = 0
        while nodeQueue:
            node = nodeQueue.pop()
            count += 1

            for neighbor in adjacency[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    nodeQueue.append(neighbor)
        
        return count == numCourses
        

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.canFinishTopological(numCourses, prerequisites)
        return self.canFinishDfs(numCourses, prerequisites)