# Definition for a binary tree node.
# class TreeNode
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution
#     def isValidBST(self, root TreeNode) - bool
#         stack = []
#         cur = root
#         vals = []
        
#         while(stack or cur)
#             while(cur)
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             vals.append(cur.val)
#             cur = cur.right
                
#         print(vals)
#         return sorted(list(set(vals))) == vals    # use set for remove duplicated value
        
class Solution
    def isValidBST(self, root TreeNode) - bool
        return self.isValid(root, -sys.maxsize, sys.maxsize)
    
    def isValid(self, node, minval, maxval)
        if not node 
            return True
        if minval = node.val or maxval = node.val
            return False
        return self.isValid(node.left, minval, node.val) and self.isValid(node.right, node.val, maxval)
    
# Time O(logN)
# Space O(1)