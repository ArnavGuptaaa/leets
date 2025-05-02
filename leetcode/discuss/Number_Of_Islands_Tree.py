"""
Link : https://leetcode.com/discuss/post/6275124/google-phone-screen-number-of-islands-in-lan4/

Question:
Given a Binary tree having nodes with value 0 and 1. write a function to return the number of islands?

Follow Up Question:
Return the sizes of unique islands
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = []
    
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
            # count = 1
            self.result.append(self.dfs(root))

        islands_left = self.number_of_islands(root.left)
        islands_right = self.number_of_islands(root.right)

        # return count + islands_left + islands_right
        return self.result


# Test cases
test_cases = [
    # Test 1: A single island (connected)
    (TreeNode(1,
        TreeNode(1),
        TreeNode(1)), [3]),  # Expected: 1 island with size 3

    # Test 2: Two disconnected islands (1 -> 1)
    (TreeNode(0,
        TreeNode(1),
        TreeNode(1)), [1, 1]),  # Expected: Two islands with sizes 1 each

    # Test 3: Right-skewed tree with 1s (connected)
    (TreeNode(1,
        None,
        TreeNode(1,
            None,
            TreeNode(1))), [3]),  # Expected: 1 island with size 3

    # Test 4: One connected island (1 -> 1) + one isolated 1
    (TreeNode(1,
        TreeNode(0,
            TreeNode(1),
            TreeNode(0)),
        TreeNode(1)), [2, 1]),  # Expected: Two islands (size 2 and size 1)

    # Test 5: All 0s (no islands)
    (TreeNode(0,
        TreeNode(0),
        TreeNode(0)), []),  # Expected: No islands

    # Test 6: Alternating 1s and 0s down the left
    (TreeNode(1,
        TreeNode(0,
            TreeNode(1,
                TreeNode(0,
                    TreeNode(1))))), [1, 1, 1]),  # Expected: Three islands (each size 1)

    # Test 7: Single node, island with value 1
    (TreeNode(1), [1]),  # Expected: Single island of size 1

    # Test 8: Single node, value 0 (no island)
    (TreeNode(0), []),  # Expected: No islands
]

# Running the test cases
sol = Solution()

for i, (root, expected) in enumerate(test_cases, 1):
    sol.result = []
    actual = sol.number_of_islands(root)
    print(f"Test {i}: Expected = {expected}, Actual = {actual}, {'PASS' if expected == actual else 'FAIL'}")