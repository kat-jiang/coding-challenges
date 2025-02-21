"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res[k-1]
    
# BST means inorder traversal will give us sorted order
# So we can do an inorder traversal, save that to an array and return the kth - 1 element

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) for the result array