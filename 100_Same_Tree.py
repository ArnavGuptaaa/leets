"""
Name: Same Tree (#100)
URL: https://leetcode.com/problems/same-tree/

Time Complexity: O(N)
Space Complexity: O(N) (worst case: skewed tree) / O(log N) (best case: balanced tree)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        
        if not q and p:
            return False

        if not p and not q:
            return True

        isLeftSame = self.isSameTree(p.left, q.left)
        isNodeSame = p.val == q.val
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isNodeSame and isRightSame