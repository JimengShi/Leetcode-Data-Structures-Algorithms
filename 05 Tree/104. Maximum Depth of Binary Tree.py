# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # (0) edge case
        if not root:
            return 0
        
        # (1) get depth of root.left and root.right  
        dl = self.maxDepth(root.left)
        dr = self.maxDepth(root.right)
        
        # (2) return the final result
        return 1 + max(dl, dr)

        # if dl > dr:
        #     return dl + 1
        # else:
        #     return dr + 1
        # return 1 + dl if dl > dr else 1 + dr
        
# Time: O(logN)
# Space: O(1)