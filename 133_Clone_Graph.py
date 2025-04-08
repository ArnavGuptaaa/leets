"""
Name: Clone Graph (#133)
URL: https://leetcode.com/problems/clone-graph/

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

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

        def bfs(node):
            dq = deque()
            dq.append(node)

            cloned_nodes = {}
            cloned_nodes[node.val] = Node(node.val)

            while dq:
                n = dq.popleft()

                for nei in n.neighbors:

                    if nei.val not in cloned_nodes:
                        cloned_nodes[nei.val] = Node(nei.val)
                        dq.append(nei)

                    cloned_nodes[nei.val].neighbors.append(cloned_nodes[n.val])

            return cloned_nodes[node.val]
        
        # ===
        return bfs(node)
        # return dfs(node)