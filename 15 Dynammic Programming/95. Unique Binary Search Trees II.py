# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
    
class Solution:
    def generateTrees(self, n):
        return self.generate(1, n) if n else []
    
    def generate(self, start, end):
        # (0) ending condition
        if start > end:
            return [None]
        
        # (1) create data structure and recursively create subtrees
        res = []
        for i in range(start, end + 1):                 # pick i as a root
            left_trees = self.generate(start, i - 1)    # all possible left subtrees
            right_trees = self.generate(i + 1, end)     # all possible right subtrees
            for l in left_trees:                     # connect left, right subtrees to root i
                for r in right_trees:
                    curr_tree = TreeNode(i)
                    curr_tree.left = l
                    curr_tree.right = r
                    res.append(curr_tree)
        
        # (3) return result
        return res