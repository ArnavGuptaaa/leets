"""
Name: Lowest Common Ancestor of Deepest Leaves (#1123)
URL: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Time Complexity: O(N)
Space Complexity: O(H)
"""

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        lca = root

        def dfs(node, depth):
            nonlocal max_depth
            nonlocal lca

            if not node:
                max_depth = max(max_depth, depth)
                return depth

            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            if left_depth == right_depth and  right_depth >= max_depth:
                lca = node
            
            return max(left_depth, right_depth)

        dfs(root, 0)
        return lca