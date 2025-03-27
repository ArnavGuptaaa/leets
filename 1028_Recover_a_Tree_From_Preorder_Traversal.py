"""
Name: Recover a Tree From Preorder Traversal (#1028)
URL: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

Time Complexity: O(N)
Space Complexity: O(nodes) 
"""

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        idx = curr = prev = 0

        while idx < len(traversal) and traversal[idx].isdigit():
            idx += 1

        root = TreeNode(int(traversal[:idx]))
        stack = [root]

        while idx < len(traversal):
            while idx < len(traversal) and traversal[idx] == '-':
                curr += 1
                idx += 1

            start = idx

            while idx < len(traversal) and traversal[idx].isdigit():
                idx += 1

            node_val = int("".join(traversal[start:idx]))
            
            idx -= 1

            new_node = TreeNode(node_val)
            if curr > prev: 
                node = stack[-1]
                node.left = new_node
            
            elif curr == prev:
                stack.pop()
                node = stack[-1]
                node.right = new_node

            else:
                for _ in range(prev - curr + 1):
                    stack.pop()

                node = stack[-1]
                node.right = new_node

            stack.append(new_node)
            prev = curr
            curr = 0

            idx += 1

        return root