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
            # result = []
            
            # def dfs(node):
            #     if not node:
            #         return
            #     dfs(node.left)      # Visit left subtree
            #     result.append(node.val)  # Visit node
            #     dfs(node.right)     # Visit right subtree

            # dfs(root)
            # return result
                
        #iterative solution
        
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr =  curr.left # Move to leftmost node
                
            curr = stack.pop() # Process the node
            res.append(curr.val)
            curr = curr.right # Move to right subtree
            
        return res