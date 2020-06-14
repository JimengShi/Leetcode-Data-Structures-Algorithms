# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursively
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Edge/Condition
        if not root:
            return None
        if root == p or root == q:
            return root

        # Divide: recursion
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Conquer
        if left and right:        # e.g., 1 and 6, return 3
            return root
        if not left:              # e.g., 1 and 8, return 1
            return right
        if not right:             # e.g., 2 and 5, return 5
            return left

# Time:  O(n)
# Space: O(n)


# iteratively
class Solution:
    def lowestCommonAncestor(self, root, p, q):     
        # (1) Start from the root node and traverse the tree
        stack = [root]                                  
        parent = {root: None}  # Dictionary for parent pointers
        
        # (2) Iterate until we find both the nodes p and q, keep saving the parent pointers in a dictionary
        while p not in parent or q not in parent:       
            node = stack.pop()
            if node.left:                     
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        ancestors = set()       # Ancestors set() for node p.

        # (3) Once found both p and q, get all the ancestors for p using parent dictionary and add to a set
        while p:
            ancestors.add(p)
            p = parent[p]
            
        # (4) trying ancestors for q, if q's ancester appears in p's ancestor set(), that is lowest common ancestor
        while q not in ancestors:
            q = parent[q]
        return q

# Time: O(n)
# Space: O(n)