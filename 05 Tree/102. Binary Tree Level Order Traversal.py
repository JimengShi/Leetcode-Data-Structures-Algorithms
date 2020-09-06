# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
# Method 1: iteratively
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # (0) edge case
        if not root:
            return root

        # (1) initialize
        queue = [root]
        res = []

        # (2) append
        while queue:
            res.append([i.val for i in queue])  # append the current entire level

            temp = []                           # temp used to save the next level and append it into queue
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp[:]

        # (3) return result
        return res   

# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.    


# Method 2: recursively
class Solution(object):
    def levelOrder(self, root):
        self.res = []                        
        self.helper(root, 0)                    
        return self.res
        
    def helper(self, node, depth):              # (2) helper function
        if node is None:                        # (2.1) edge case
            return

        if len(self.res) == depth:              # (2.2) process
            self.res.append([])
        self.res[depth].append(node.val)

        self.helper(node.left, depth + 1)       # (2.3) recursion
        self.helper(node.right, depth + 1)

# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.