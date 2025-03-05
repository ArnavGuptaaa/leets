"""
Name: Delete Nodes And Return Forest (#1110)
URL: https://leetcode.com/problems/delete-nodes-and-return-forest/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        # ===
        def delNodesHelper(node):
            if not node:
                return None

            node.left = delNodesHelper(node.left)
            node.right = delNodesHelper(node.right)

            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                return None

            return node

        # ===
        if root and root.val not in to_delete:
            res.append(root)

        delNodesHelper(root)

        return res