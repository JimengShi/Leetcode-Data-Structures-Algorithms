# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# iteratively
class Solution: 
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        res = []        
        stack = [(root, False)]                 # (1) save root in stack
        
        while stack:
            cur, visited = stack.pop()          # (2) pop the last node in stack as cur
            # if not cur:
            #     continue
            if visited:                         # (2.1) condition: res.append(cur) when visited is True
                res.append(cur.val)
                
            stack.append((cur, True))           # (2.2) recursion: save new status of curr and its children in stack
            if curr.right:
                stack.append((cur.right, False))    
            if curr.left:
                stack.append((cur.left, False))
                
        return res

class Solution: 
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        res = []        
        stack = [(root, False)]                 # (1) save root in stack
        
        while stack:
            cur, visited = stack.pop()          # (2) pop the last node in stack as cur

            if not cur:                         # (2.1) condition: res.append(cur) when visited is True
                continue
            if visited:                             
                res.append(cur.val)

            stack.append((cur, True))           # (2.2) recursion: save new status of curr and its children in stack
            stack.append((cur.right, False))    
            stack.append((cur.left, False))
        return res


# Time: O(n)
# Space: O(n)

    
# recursively
class Solution:       
    def postorderTraversal(self, root):
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node is None:
            return
        self.helper(node.left)
        self.helper(node.right) 
        self.res.append(node.val)

# Time: O(n) because the recursive function is T(n) = 2T(n/2) + 1.
# Space:O(n), in the average case it's O(logn) where n is number of nodes.