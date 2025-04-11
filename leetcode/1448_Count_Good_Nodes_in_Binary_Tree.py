"""
Name: Count Good Nodes in Binary Tree (#1448)
URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Time Complexity: O(N)
Space Complexity: O(H) [H : height of the tree]
"""

class Solution:
    def goodNodeHelper(self, node, maxSoFar):
        if not node:
            return 0
        
        isNodeGood = False

        if node.val >= maxSoFar:
            maxSoFar = node.val
            isNodeGood = True

        leftGoodNodes = self.goodNodeHelper(node.left, maxSoFar)
        rightGoodNodes = self.goodNodeHelper(node.right, maxSoFar)

        return (leftGoodNodes + rightGoodNodes + 1) if isNodeGood else (leftGoodNodes + rightGoodNodes)
        

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodeHelper(root, root.val)