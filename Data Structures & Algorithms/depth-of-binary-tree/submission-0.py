# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftChild=self.maxDepth(root.left)
        rightChild=self.maxDepth(root.right)
        h=max(leftChild,rightChild)

        return h+1
        