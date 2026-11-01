# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

    # #  Unlike Path Sum I and II, the path does NOT have to start at the root or end at a leaf.   
    #         20
    #       15    7
    #       we return 20+max(15,7) to the root
        self.res=float("-inf")
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            left=max(0,left)
            right=max(0,right)
            self.res = max(self.res, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return self.res