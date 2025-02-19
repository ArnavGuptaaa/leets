"""
Name: Maximum Depth of Binary Tree (#104)
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time Complexity: O(N)
Space Complexity: O(N) (worst case for skewed tree) / O(log N) (best case for balanced tree)
"""

class Solution:
    def getMaxDepth(self, node):
        if not node: 
            return 0
        
        maxDepthSoFar = max(self.getMaxDepth(node.left), self.getMaxDepth(node.right)) + 1

        return maxDepthSoFar

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root)