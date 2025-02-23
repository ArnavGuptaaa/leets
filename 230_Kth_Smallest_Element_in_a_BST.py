"""
Name: Kth Smallest Element in a BST (#230)
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def getInorderTraversal(self, node, arrSoFar):
        if not node:
            return 
        
        self.getInorderTraversal(node.left, arrSoFar)
        arrSoFar.append(node.val)
        self.getInorderTraversal(node.right, arrSoFar)

        return arrSoFar

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
            
        inOrderTraversal = self.getInorderTraversal(root, [])
        return inOrderTraversal[k-1]