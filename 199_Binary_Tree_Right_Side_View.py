"""
Name: Binary Tree Right Side View (#199)
URL: https://leetcode.com/problems/binary-tree-right-side-view/

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        
        if not root:
            return rightSideView

        dfsQueue = [root]

        while len(dfsQueue) != 0:
            rightSideView.append(dfsQueue[-1].val)

            for _ in range(len(dfsQueue)):
                node = dfsQueue.pop(0)

                if node.left:
                    dfsQueue.append(node.left)
                
                if node.right:
                    dfsQueue.append(node.right)
            
        return rightSideView