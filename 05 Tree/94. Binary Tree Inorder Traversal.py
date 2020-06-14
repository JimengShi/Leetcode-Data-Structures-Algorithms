# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteratively
class Solution(object):
    def inorderTraversal(self, root):
        # (1) initialize the stack and traversal
        stack = []                          
        res = []
        
        # (2) start traversing
        if root is None:
            return
        while stack or root:
            if root:
                stack.append(root)          # (2.1) save leftmoset nodes in stack temporarily
                root = root.left            # (2.2) update the left child as new root
            else:                           #       root has no left child
                node = stack.pop()          # (2.3) pop the last node with no left child in stack
                res.append(node.val)        # (2.4) append it into traversal list
                root = node.right           # (2.5) update the right child as new root
                
        # (3) return the output
        return res
    
# Time: O(n) because the recursive function is T(n) = 2T(n/2) + 1.
# Space:O(n), in the average case it's O(logn) where n is number of nodes.

    
# recursively
class Solution(object):    
    def inorderTraversal(self, root):
        self.res = []
        self.helper(root)              # (4) call helper function
        return self.res
    
    def helper(self, node):
        if node is None:
            return
        if node:
            self.helper(node.left)     # (1) res.append(root.left)  -->  left part
            self.res.append(node.val)  # (2) res.append(root)       -->  root itself   
            self.helper(node.right)    # (3) res.append(root.right) -->  right part
            
# Time: O(n) because the recursive function is T(n) = 2T(n/2) + 1.
# Space:O(n), in the average case it's O(logn) where n is number of nodes.