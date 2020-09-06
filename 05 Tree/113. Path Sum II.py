# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example: Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1

# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: recursively
class Solution:    
    def pathSum(self, root: TreeNode, summation: int) -> List[List[int]]:
        # (0) edge case
        if not root:
            return

        # (1) initialize
        res = []
        path = []             # use stack to track downward traversal
        
        # (2) dfs function
        def dfs(node):
            # (2.1) end condition
            if not node:
                return

            # (2.2) process
            path.append( node.val )                 
            if not node.left and not node.right and sum(path) == summation:
                res.append( list(path) )

            # (2.3) recursively call dfs function to try node.left and node.right
            dfs( node.left )                         
            dfs( node.right )        
            path.pop()
        
        # (3) call dfs function and return result    
        dfs(root)
        return res

# O(N): access N node
# O(N): when the tree is unbalanced, O(h=logN) when the tree is balanced
        

# Method 2: iteratively addtion
class Solution(object):
    def pathSum(self, root, summation):
        if not root:
            return []
        
        res = []
        stack = [(root, [root.val])]
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right and sum(temp) == summation:
                res.append(temp)
            if node.right:
                stack.append((node.right, temp+[node.right.val]))
            if node.left:
                stack.append((node.left, temp+[node.left.val]))
        return res
    
        
# O(N): access N node
# O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced