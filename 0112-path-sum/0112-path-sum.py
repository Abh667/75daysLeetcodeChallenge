# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        # Base case: empty tree
        if root is None:
            return False

        # If it's a leaf node, check sum
        if root.left is None and root.right is None:
            return targetSum == root.val

        # Reduce targetSum and check subtrees
        targetSum -= root.val

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))