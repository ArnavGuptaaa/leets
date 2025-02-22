"""
Name: Binary Tree Level Order Traversal (#102)
URL: <Add question link here>

Time Complexity: O(?)
Space Complexity: O(?)
"""

class Solution:        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        bfsQueue = [root]

        while len(bfsQueue) != 0:
            level = []
            
            for _ in range(len(bfsQueue)):
                node = bfsQueue.pop(0)
                
                level.append(node.val)

                if node.left: bfsQueue.append(node.left)
                if node.right: bfsQueue.append(node.right)
                
            res.append(level)

        return res