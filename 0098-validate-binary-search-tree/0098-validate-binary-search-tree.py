# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, min_val: float, max_val: float) -> bool:
            if not node:
                return True  # Base case: An empty tree/subtree is always valid

            # If current node violates the BST property, return False
            if not (min_val < node.val < max_val):
                return False

            # Recursively validate left and right subtrees
            return (dfs(node.left, min_val, node.val) and  # Left subtree: max_val updated to current node's value
                    dfs(node.right, node.val, max_val))    # Right subtree: min_val updated to current node's value

        # Start DFS with initial min and max values as negative and positive infinity
        return dfs(root, float('-inf'), float('inf'))
