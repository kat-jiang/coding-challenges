# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # If both p and q are greater than root, LCA is in the right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both p and q are less than root, LCA is in the left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                # If p and q are on different sides (or one is root itself), root is the LCA
                return root