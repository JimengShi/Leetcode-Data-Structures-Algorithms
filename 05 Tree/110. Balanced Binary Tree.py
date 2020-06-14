# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        # (0) edge case
        if root == None:
            return True
        
        # (1) get the left_depth and right_depth
        l = self.depth(root.left)
        r = self.depth(root.right)
        
        # (2) return result
        return abs(l-r)<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    

    def depth(self, node):
        if node == None:     # necessary, which can not be deleted
            return 0
        return max( self.depth(node.left), self.depth(node.right) ) + 1
    
# Time: O(logN)
# Space: O(1)