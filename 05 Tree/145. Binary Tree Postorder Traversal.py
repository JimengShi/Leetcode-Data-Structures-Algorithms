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
        stack = [(root, False)]                     # (1) save root in stack
        
        while stack:
            cur, visited = stack.pop()              # (2) pop the last node in stack as cur
            if not cur:                             # (2.1) continue if cur is None
                continue
            if visited:                             # (2.2) res.append(cur) when visited is True
                res.append(cur.val)
            else:                                   # (2.3) save new status and children in stack
                stack.append((cur, True))           #       cur visited: False --> True after pop
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