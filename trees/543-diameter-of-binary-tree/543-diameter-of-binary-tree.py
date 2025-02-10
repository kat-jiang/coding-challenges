# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res # ints in python are immutable, so we need to use nonlocal to modify res
            if not root:
                return 0
            
            # Compute left and right subtree heights
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Update the maximum diameter
            res = max(res, left + right)
            
            # Return the height of the current node
            return max(left, right) + 1
        
        dfs(root)
        return res