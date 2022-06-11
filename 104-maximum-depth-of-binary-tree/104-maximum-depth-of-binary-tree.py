# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #need to use dfs to get longest depth
        #recursive function to go into all branches
            #base case: when we reach leaf node or no more nodes, return depth
            #start at root node, call recursive function on left and right
                # initialize depth as 0, add 1 for each node it traverses
            #return max depth using max function
            
        def dfs(root, depth):
            #base case: when there are no more nodes to traverse
            if not root:
                return depth
            #call recursive function on left and right children
            max_depth =  max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            
            return max_depth
        
        #call recursive function on root and initialize depth at 0
        return dfs(root, 0)