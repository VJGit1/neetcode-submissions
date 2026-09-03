# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightTree(self,root):
        if root is None:
            return 0
        left=self.heightTree(root.left)
        right=self.heightTree(root.right)
        return 1+max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftTree=self.heightTree(root.left)
        rightTree=self.heightTree(root.right)
        if abs(leftTree-rightTree)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)