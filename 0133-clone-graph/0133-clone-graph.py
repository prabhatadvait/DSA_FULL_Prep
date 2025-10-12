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

        def dfs(v):
            if v in visited:
                return visited[v]
            
            clone = Node(v.val)
            visited[v]=clone
            
            for neighbor in v.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
            
