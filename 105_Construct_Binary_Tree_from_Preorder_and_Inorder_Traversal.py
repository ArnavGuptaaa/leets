"""
Name: Construct Binary Tree from Preorder and Inorder Traversal (#105)
URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_node = TreeNode(preorder[0])
        inorder_mid = inorder.index(preorder[0])

        root_node.left = self.buildTree(preorder[1 : inorder_mid + 1], inorder[: inorder_mid])
        root_node.right = self.buildTree(preorder[inorder_mid + 1:], inorder[inorder_mid + 1 :])

        return root_node