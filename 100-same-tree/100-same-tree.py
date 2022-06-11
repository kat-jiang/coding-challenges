# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #traverse tree p starting at root node, compare to tree q
        #call isSameTree recursive function
        #base case: when there are no more nodes in p and q to traverse and didn't return False, return True
        #if p is none OR q is none, return False as this means they aren't equal
        #if p does not equal q, return False
        #otherwise call recursive function on p.left with q.left and p.right with q.right

        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)