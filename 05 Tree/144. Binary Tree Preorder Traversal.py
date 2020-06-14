# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iteratively
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return res
    
# Time: O(n) because the recursive function is T(n) = 2T(n/2) + 1.
# Space:O(n), in the average case it's O(logn) where n is number of nodes.

        
# recursively
class Solution:       
    def preorderTraversal(self, root):
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node is None:
            return
        self.res.append(node.val)
        self.helper(node.left)
        self.helper(node.right) 
        
# Time: O(n) because the recursive function is T(n) = 2T(n/2) + 1.
# Space:O(n), in the average case it's O(logn) where n is number of nodes.