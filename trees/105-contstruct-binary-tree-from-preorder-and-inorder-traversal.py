"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where 
preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""
# 1. Preorder Traversal (Root → Left → Right)
#       The first element in preorder is always the root of the tree.
# 2. Inorder Traversal (Left → Root → Right)
#       The position of the root in inorder splits the tree into left and right subtrees.
# 3. Recursive Construction
#       Recursively build the left and right subtrees using appropriate slices of preorder and inorder.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: empty tree
        if not preorder or not inorder:
            return

        root_val = preorder[0]  # First element of preorder is root
        root = TreeNode(root_val)

        # Find the root index in inorder
        root_index = inorder.index(root_val)
        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        # for in order, the root index splits the tree into left and right,
        # so we don't want to include root_index value when we splicing the inorder array

        return root
    

# Time complexity: 
# O(n²) due to use of index() method in inorder array.
# Note: This can be improved to O(n) by using a hashmap to store indices of inorder elements.\

# Space complexity:
# O(n) for creation of additional list
