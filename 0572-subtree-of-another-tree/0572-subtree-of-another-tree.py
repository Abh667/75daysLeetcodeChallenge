# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
        # Edge case: if subRoot is empty → always True
        if not subRoot:
            return True
        
        # If root becomes empty → cannot find subtree
        if not root:
            return False
        
        # Check if trees match from current node
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise check in left and right subtree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    
    def isSameTree(self, p, q):
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))




        