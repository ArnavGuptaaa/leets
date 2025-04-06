"""
Name: Find Eventual Safe States (#802)
URL: https://leetcode.com/problems/find-eventual-safe-states/

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def eventualSafeNodes(self, adjacency: List[List[int]]) -> List[int]:
        def check_cycle(node, node_states):
            if node_states[node] == VISITED:
                return False

            if node_states[node] == VISITING:
                return True

            node_states[node] = VISITING

            for nei in adjacency[node]:
                if check_cycle(nei, node_states):
                    return True

            node_states[node] = VISITED
            return False


        UNVISITED, VISITING, VISITED = 0, 1, 2
        node_states = [UNVISITED] * len(adjacency)
        result = []

        for node in range(len(adjacency)):
            if check_cycle(node, node_states) == False:
                result.append(node)

        return result