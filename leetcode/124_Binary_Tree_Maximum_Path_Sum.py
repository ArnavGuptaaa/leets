"""
Name: Binary Tree Maximum Path Sum (#124)
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Time Complexity: O(N)
Space Complexity: O(H) [H: Height of tree]
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001

        #===
        def dfs(node):
            if not node:
                return 0

            nonlocal res

            leftMaxPathSum = dfs(node.left)
            rightMaxPathSum = dfs(node.right)

            res = max(
                res, 
                node.val,
                leftMaxPathSum + node.val,
                rightMaxPathSum + node.val,
                leftMaxPathSum + rightMaxPathSum + node.val
            )

            return max(
                node.val,
                leftMaxPathSum + node.val, 
                rightMaxPathSum + node.val
            ) 

        # ===
        dfs(root)
        return res

"""
IMP : A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.

This doesnt mean that we need to in
"""