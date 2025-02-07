# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []               # Final output list for right side view
        queue = deque([root])     # Initialize queue with the root node

        while queue:
            level_size = len(queue)   # Number of nodes at the current level

            for i in range(level_size):
                node = queue.popleft()    # Dequeue the node

                # If it's the last node in the current level, add it to the result
                if i == level_size - 1:
                    result.append(node.val)

                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

