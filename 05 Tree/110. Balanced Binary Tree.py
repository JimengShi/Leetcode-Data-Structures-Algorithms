# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        # (0) edge case
        if not root:
            return True
        
        # (1) get the left_depth and right_depth
        l = self.depth(root.left)
        r = self.depth(root.right)
        
        # (2) return result
        return abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    

    def depth(self, node):
        if not node:     # necessary, which can not be deleted
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
# Time: O(N)
# Space: O(N)