# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_value = root.val
        # case 1: p and q > cur node, e.g., both 7 and 9 > 6, we search 6.right
        if p.val > cur_value and q.val > cur_value:
            return self.lowestCommonAncestor(root.right, p, q)
        # case 2: p and q < cur node, e.g., both 0 and 5 < 6, we search 6.left
        elif p.val < cur_value and q.val < cur_value:
            return self.lowestCommonAncestor(root.left, p, q)
        # case 3: Both p and q are not on the same side of cur node, then return cur node
        else:
            return root
        
# Time: O(N), the worst case we may visit N nodes of the BST.
# Space: O(N). recursion stack would be N since the height of a skewed BST could be N.

        
# iteratively
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            else:          
                return root 
            
# Time: O(N), In the worst case we may visit N nodes of the BST.
# Space: O(1).


# iteratively
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if max(p.val, q.val) < root.val: 
                root = root.left
            elif min(p.val, q.val) > root.val: 
                root = root.right
            else:
                return root
            
# Time: O(N), In the worst case we may visit N nodes of the BST.
# Space: O(1).