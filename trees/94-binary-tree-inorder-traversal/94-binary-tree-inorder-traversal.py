# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorder traversal: traverse left, root, right
        #recursive solution
#         res = []
        
#         def inorder(node, res):
#             if not node:
#                 return
#             inorder(node.left, res)
            
#             res.append(node.val)
            
#             inorder(node.right, res)
            
#             return res
        
#         return inorder(root, res)
        
        #iterative solution
        
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr =  curr.left
                
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            
        return res