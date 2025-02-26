# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        we need do dfs here 
        go through each node check sum = target sum or not 
        return sum 
        """
        def dfs(node,currentSum):
          if not node:
            return False 

          currentSum += node.val
          if not node.left and not node.right:
            return currentSum == targetSum
          
          return (dfs(node.left, currentSum) or 
                  dfs(node.right, currentSum))

        return dfs(root,0)