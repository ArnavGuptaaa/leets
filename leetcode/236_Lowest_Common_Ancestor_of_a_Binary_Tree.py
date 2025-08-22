"""
Name: Lowest Common Ancestor of a Binary Tree (#236)
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Time Complexity: O(N)
Space Complexity: O(H)
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            if not left_result:
                return right_result

            if not right_result:
                return left_result

            return node

        return dfs(root)