"""
Link : https://leetcode.com/discuss/post/6275124/google-phone-screen-number-of-islands-in-lan4/

Given a Binary tree having nodes with value 0 and 1. write a function to return the number of islands?
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass
    
    def dfs(self, node):
        if not node:
            return 0
        
        if node.val != 1:
            return 0

        count = 1 + self.dfs(node.left) + self.dfs(node.right)
        node.val = 0

        return count

    def number_of_islands(self, root):
        if not root:
            return 0

        count = 0

        if root.val == 1:
            count = 1
            
            print(self.dfs(root))

        islands_left = self.number_of_islands(root.left)
        islands_right = self.number_of_islands(root.right)

        return count + islands_left + islands_right


# Tests
test_cases = [
    # Test 1
    (TreeNode(1,
        TreeNode(1),
        TreeNode(1)), 1),

    # Test 2
    (TreeNode(0,
        TreeNode(1),
        TreeNode(1)), 2),

    # Test 3
    (TreeNode(1,
        None,
        TreeNode(1,
            None,
            TreeNode(1))), 1),

    # Test 4
    (TreeNode(1,
        TreeNode(0,
            TreeNode(1),
            TreeNode(0)),
        TreeNode(1)), 2),

    # Test 5
    (TreeNode(0,
        TreeNode(0),
        TreeNode(0)), 0),

    # Test 6
    (TreeNode(1,
        TreeNode(0,
            TreeNode(1,
                TreeNode(0,
                    TreeNode(1))))), 3),
]

for i, (root, expected) in enumerate(test_cases, 1):
    sol = Solution()
    actual = sol.number_of_islands(root)
    print(f"Test {i}: Expected = {expected}, Actual = {actual}, {'PASS' if expected == actual else 'FAIL'}")