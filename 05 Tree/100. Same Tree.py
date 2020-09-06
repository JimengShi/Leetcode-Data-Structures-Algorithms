# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: recursion
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # case 1: both empty
        if not p and not q:
            return True
        
        # case 2: one exists, the other one not
        elif not p or not q:
            return False
        
        # case 3: both exist and equal
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n) The number of recursive calls is bound by height of tree. In worst case, tree height is O(n). 


# Method 2: stack
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        stack = [(p, q)]
        while stack:
            root1, root2 = stack.pop()
            if not root1 and not root2:                         # case 1: both empty
                continue   
            elif root1 and root2 and root1.val == root2.val:    # case 3: both exist and equal
                stack.append((root1.left, root2.left))
                stack.append((root1.right, root2.right))
            else:                                               # case 2: other cases
                return False
                break
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)