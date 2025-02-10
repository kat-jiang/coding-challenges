from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()  # Remove the front node
                level.append(node.val)  # Store its value
                
                if node.left:
                    queue.append(node.left)  # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue
            
            result.append(level)  # Store the level results

        return result