"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #we'll use graph traversal+hashmap(to avoid cloning multipl times)
        # Create new nodes with the same values.
        # Preserve all connections between nodes.
        # Do NOT reuse any original nodes
        if not node:
            return None
        visited={}
        def dfs(node):
            #if already cloned return its copy
            if node in visited:
                return visited[node]
            #if not cloned, create a clone
            clone=Node(node.val)
            #store it
            visited[node]=clone
            #clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)