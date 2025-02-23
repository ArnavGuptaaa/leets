"""
Name: Validate Binary Search Tree (#98)
URL: <Add question link here>

# Iterative
Time Complexity: O(N)
Space Complexity: O(N)

# Recursive
Time Complexity: O(N)
Space Complexity: O(H) [H : height of the tree]
"""

class Solution:
    def isValidBSTRecursive(self, node, minVal, maxVal):
        if not node:
            return True
        
        if not (minVal < node.val < maxVal):
            return False
        
        return self.isValidBSTRecursive(node.left, minVal, node.val) and self.isValidBSTRecursive(node.right, node.val, maxVal)


    def getInorderTraversal(self, node, arrSoFar):
        if not node:
            return 
        
        self.getInorderTraversal(node.left, arrSoFar)
        arrSoFar.append(node.val)
        self.getInorderTraversal(node.right, arrSoFar)

        return arrSoFar
    

    def checkIfArrayIsSorted(self, arrayToTest):
        
        for idx in range(len(arrayToTest) - 1):
            # IMP: checking for ">=" rather than ">" since 
            # two nodes in a BST cannot be of the same value
            if arrayToTest[idx] >= arrayToTest[idx + 1]:
                return False
        
        return True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # Iterative Solution
        # # IMP: Inorder traversal of BST is always sorted.
        # if not root: return True
        # arrayToTest = self.getInorderTraversal(root, [])
        # return self.checkIfArrayIsSorted(arrayToTest)

        return self.isValidBSTRecursive(root, float('-inf'), float('inf'))