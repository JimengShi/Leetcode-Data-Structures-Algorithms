# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, p, q) -> bool:
        if not p and not q:   # base case 1
            return True
        elif not p or not q:  # base case 2
            return False
        elif p.val != q.val:  # base case 3
            return False
        else:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)
        
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n) The number of recursive calls is bound by the height of the tree. In the worst case, the tree height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.


# Method 2: stack
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # (0) edge case
        if not root:
            return True
        
        # (1) create data structure stack
        stack = [(root, root)]

        # (2) traverse input
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:                # node1 empty and node2 empty
                continue
            elif node1 and node2 and node1.val == node2.val:   # node1 empty or node2 empty
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            else:                                              # otherwise: return False and break
                return False
                break
        
        # (3) otherwise return True
        return True
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)