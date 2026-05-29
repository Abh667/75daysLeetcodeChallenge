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
        # Definition for a Node.
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # If graph is empty
        if not node:
            return None
        
        # Dictionary to store old node -> new cloned node
        visited = {}

        def dfs(curr):
            
            # If node already cloned
            if curr in visited:
                return visited[curr]
            
            # Create clone node
            clone = Node(curr.val)
            
            # Store in dictionary
            visited[curr] = clone
            
            # Clone all neighbors
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
        