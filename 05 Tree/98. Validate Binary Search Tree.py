# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:
#     2
#    / \
#   1   3
# Input: [2,1,3]
# Output: true

# Example 2:
#     5
#    / \
#   1   4
#      / \
#     3   6
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: recursively
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -sys.maxsize, sys.maxsize)
    
    def isValid(self, node, minval, maxval):
        if not node: 
            return True
        
        if minval >= node.val or maxval <= node.val:
            return False
        
        return self.isValid(node.left, minval, node.val) and self.isValid(node.right, node.val, maxval)
    
# Time: O(N)
# Space: O(N)


# Method 2: iteratively
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            node, lower, upper = stack.pop()
            # if not node:
            #     continue

            if node.val <= lower or node.val >= upper:
                return False
            if node.right:
                stack.append((node.right, node.val, upper))
            if node.left:
                stack.append((node.left, lower, node.val))
        return True  
    
# Time: O(N)
# Space: O(N)