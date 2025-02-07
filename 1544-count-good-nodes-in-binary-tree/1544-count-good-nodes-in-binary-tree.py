# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> int:
      
            if not node:
                return 0  # Base case: If the node is None, return 0
            
            # Check if the current node is a good node
            good = 1 if node.val >= max_so_far else 0
            
            # Update the maximum value for the path
            new_max = max(max_so_far, node.val)
            
            # Recursively count good nodes in the left and right subtrees
            left_good = dfs(node.left, new_max)
            right_good = dfs(node.right, new_max)
            
            # Total good nodes = current node (if good) + left subtree + right subtree
            return good + left_good + right_good

        # Start DFS from the root with initial max value as root's value
        return dfs(root, root.val)