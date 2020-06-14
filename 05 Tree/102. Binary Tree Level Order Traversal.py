# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
# iteratively
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root

        stack = [root]
        res = []

        while stack:
            res.append([i.val for i in stack])
            
            temp = []
            for i in stack:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                    
            # res.append([i.val for i in stack])
            stack = temp[:]

        return res    

# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.    


# recursively
class Solution(object):
    def levelOrder(self, root):
        self.res = []                           # (1) initialize an empty list
        self.helper(root, 0)                    # (3) call helper function
        return self.res
        
    def helper(self, node, depth):           # (2) helper function
        if node is None:                     # (2.1) edge case
            return

        if len(self.res) == depth:          # (2.2) process
            self.res.append([])
            
        self.res[depth].append(node.val)
        self.helper(node.left, depth + 1)   # (2.3) recursion
        self.helper(node.right, depth + 1)

# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.