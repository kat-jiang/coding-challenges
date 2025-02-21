"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the 
same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a 
node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.


"""

# Approach
# Recursive Traversal: We traverse root and check at every node whether the subtree rooted at that node matches subRoot.
# Tree Comparison: At each node of root, we use a helper function to check whether the subtree starting at that node is identical to subRoot.
# Steps
# If root is None, return False (base case).
# If the trees rooted at root and subRoot are identical, return True.
# Otherwise, recursively check the left and right subtrees of root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False  # Base case: root is None, so subRoot can't be a subtree
        
        if self.isSameTree(root, subRoot):
            return True  # Found a subtree match
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True  # Both trees are empty, so they match
        if not s or not t or s.val != t.val:
            return False  # One tree is empty or values do not match
        
        # Check both left and right subtrees
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)


# Time & Space Complexity
# Time Complexity: O(m * n)
# isSameTree takes O(m) in the worst case.
# We call isSameTree at every node in root (up to n nodes).
# Worst case: O(m * n) when subRoot is compared at every node in root.
# Space Complexity: O(h)
# Recursion depth depends on tree height h.
# Balanced tree: O(log n), Skewed tree: O(n).