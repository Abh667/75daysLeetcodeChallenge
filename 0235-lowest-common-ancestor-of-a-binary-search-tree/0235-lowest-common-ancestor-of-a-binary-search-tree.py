class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            # दोनों left में हैं
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # दोनों right में हैं
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # split point → यही LCA है
            else:
                return root
        