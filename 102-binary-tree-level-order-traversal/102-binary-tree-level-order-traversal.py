# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize return list
        #base case: when no more nodes, return
        #create a list for each level to append nodes
        #recurse into left and right, append nodes to list
        #return levels list
        
        levels = []

        def dfs(root, level=0):
        
            if len(levels) <= level:
                levels.append([])
                
            levels[level].append(root.val)
            
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
        
        if root:
            dfs(root)
        
        return levels