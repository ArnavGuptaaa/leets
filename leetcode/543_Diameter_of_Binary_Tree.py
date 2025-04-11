"""
Name: Diameter of Binary Tree (#543)
URL: https://leetcode.com/problems/diameter-of-binary-tree/

Time Complexity: O(N)
Space Complexity: O(N) (worst case: skewed tree) / O(log N) (best case: balanced tree)
"""

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterHelper(self, node):
        if not node:
            return 0

        maxLeftTreeEdges = self.diameterHelper(node.left)
        maxRightTreeEdges = self.diameterHelper(node.right)

        diameter = maxLeftTreeEdges + maxRightTreeEdges
        self.maxDiameter = diameter if diameter > self.maxDiameter else self.maxDiameter

        return max(maxLeftTreeEdges, maxRightTreeEdges) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterHelper(root)
        
        return self.maxDiameter