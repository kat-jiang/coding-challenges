# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorder traversal: traverse left, root, right
        
        res = []
        
        def inorder(node, res):
            if not node:
                return
            inorder(node.left, res)
            
            res.append(node.val)
            
            inorder(node.right, res)
            
            return res
        
        return inorder(root, res)
            