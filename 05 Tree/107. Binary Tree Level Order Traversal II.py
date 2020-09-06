# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Method 1: iteratively
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        queue = [root]
        res = []
        while queue:
            res.append([i.val for i in queue])

            tem = []
            for i in queue:
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            queue = tem[:]
            
        return res[::-1]

# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.

    
# Method 2: recursively
class Solution(object):
    def levelOrderBottom(self, root):
        res = []                           # (1) initialize an empty list
        
        def helper(root, depth):           # (2) helper function
            if root is None:               # (2.1) edge case
                return
            
            if len(res) == depth:          # (2.2) process
                res.append([])
            res[depth].append(root.val)
            
            helper(root.left, depth + 1)   # (2.3) recursion
            helper(root.right, depth + 1)
            
        helper(root, 0)                    # (3) call helper function
        return res[::-1]
    
# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.

