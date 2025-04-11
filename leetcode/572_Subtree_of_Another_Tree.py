"""
Name: Subtree of Another Tree (#572)
URL: https://leetcode.com/problems/subtree-of-another-tree/

Time Complexity: O(M * N) (M : number of nodes in root. N : number of nodes in subRoot)
Space Complexity: O(N) (worst case: skewed tree) / O(log N) (best case: balanced tree)
"""

class Solution:
    def isSameTree(self, node, subRoot):
        if not node and subRoot:
            return False
        
        if not subRoot and node:
            return False
        
        if not node and not subRoot:
            return True
        
        if node.val != subRoot.val: 
            return False

        return self.isSameTree(node.left, subRoot.left) and self.isSameTree(node.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)