"""
Name: Clone Graph (#133)
URL: https://leetcode.com/problems/clone-graph/

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        if not node:
            return None

        # ===
        def dfs(node):
            if node in clones:
                return clones[node]
            
            clonedNode = Node(node.val)
            clones[node] = clonedNode

            for neighbor in node.neighbors:
                clonedNode.neighbors.append(dfs(neighbor))
            
            return clonedNode
        
        # ===
        return dfs(node)