# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            #both are empty
            if p is None and q is None:
                return True
            #either one is empty or the values dont match
            if p is None or q is None or p.val!=q.val:
                return False
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)

        #subroot is empty
        if not subRoot:
            return True
        #root is empty
        if not root:
            return False
        #check is root and subroot are same/equal
        if sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    
        