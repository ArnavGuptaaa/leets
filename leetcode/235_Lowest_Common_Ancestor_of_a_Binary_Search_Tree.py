"""
Name: Lowest Common Ancestor of a Binary Search Tree (#235)
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Time Complexity: O(H)
Space Complexity: O(H)
"""

class Solution:
    def lcaHelper(self, node, p, q):
        if node == p:
            return p
        
        if node == q:
            return q
        
        if p.val < node.val < q.val:
            return node
        
        if p.val < q.val < node.val:
            return self.lcaHelper(node.left, p, q)

        if node.val < p.val < q.val:
            return self.lcaHelper(node.right, p, q)

        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = None

        if q.val < p.val:
            temp = p
            p = q
            q = temp
        
        return self.lcaHelper(root, p, q)