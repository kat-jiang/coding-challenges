# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #initialize inverted tree with same root
        #traverse through tree
        #recursion:
            #base case: when there is no more nodes to traverse, return
            #recurse into left, set node equal to root.right
            #recurse into right, see node equal to root.left
        #once whole tree is traversed, return root
        
        #base case
        if not root:
            return None
        
        #call recursion on left and right
        self.invertTree(root.left)
        self.invertTree(root.right)
            
        #set left as right and right as left
        root.left, root.right = root.right, root.left 
        
        return root