"""
Name: Balanced Binary Tree (#110)
URL: https://leetcode.com/problems/balanced-binary-tree/

Time Complexity: O(N)
Space Complexity: O(N) (worst case: skewed tree) / O(log N) (best case: balanced tree)
"""

class Solution:
    def __init__(self):
        self.res = True
    
    def isBalancedHelper(self, node): 
        if not node: 
            return 0
        
        leftHeight = self.isBalancedHelper(node.left)
        rightHeight = self.isBalancedHelper(node.right)

        self.res = self.res and abs(leftHeight - rightHeight) <= 1

        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalancedHelper(root)

        return self.res