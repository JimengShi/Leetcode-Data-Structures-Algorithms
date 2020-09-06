# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 3 cases:
# case 1: both p and q > cur node, e.g., both 7 and 9 > 6, search 6.right
# case 2: both p and q < cur node, e.g., both 0 and 5 < 6, search 6.left
# case 3: Both p and q are not on same side of cur node, return cur node


# Method 1: Recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root

# Time: O(N), the worst case we may visit N nodes of the BST.
# Space: O(N). recursion stack would be N since the height of a skewed BST could be N.

        
# Method 2: iteratively
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:          
                return root 
            
# Time: O(N), In the worst case we may visit N nodes of the BST.
# Space: O(1).