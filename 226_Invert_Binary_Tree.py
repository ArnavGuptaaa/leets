"""
Name: Invert Binary Tree (#226)
URL: https://leetcode.com/problems/invert-binary-tree/

Time Complexity: O(N)
Space Complexity: O(N) (worst case: skewed tree) / O(log N) (best case: balanced tree)
"""

class Solution:
    def invertTreeHelper(self, node):
        if not node:
            return
        
        tempNode = node.left
        node.left = node.right
        node.right = tempNode

        self.invertTreeHelper(node.left)
        self.invertTreeHelper(node.right)
        
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeHelper(root)