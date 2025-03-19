"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 

        visited = {}

        def dfs(old_node):
            if old_node in visited:
                return visited[old_node]

            # clone 
            new_node = Node(old_node.val)
            visited[old_node] = new_node

            for neighbor in old_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return new_node

        return dfs(node)
