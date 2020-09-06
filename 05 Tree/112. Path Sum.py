# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up 
# all the values along the path equals the given sum. Note: A leaf is a node with no children.

# Example: Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursively
class Solution(object):
    def hasPathSum(self, root, sum):
        # (0) if it is not root
        if not root:                          
            return False
        
        # (1) sum = sum - root and check if reach leaf node                              
        if not root.left and not root.right and sum == root.val:
            return True
        
        # (3) recursively call function for each child node
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    
# Time: O(N): access N node
# Space: O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced

    
# iteratively substraction
class Solution(object):
    def hasPathSum(self, root, sum):
        # (0) edge case
        if not root:
            return False
        
        # (1) save root and target in stack
        stack = [(root, sum)]
        
        # (2) pop and append elements
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and node.val == curr_sum:   # (2.1) check when it's leaf node 
                return True
            if node.right:                                          # (2.2) keep append if it's not leaf
                stack.append((node.right, curr_sum-node.val))
            if node.left:
                stack.append((node.left, curr_sum-node.val))
                
        # (3) return False
        return False

# O(N): access N node
# O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced


# iteratively addtion    
class Solution(object):
    def hasPathSum(self, root, sum1):
        if not root:
            return False
        
        stack = [(root, [root.val])]                                    # (1) save root info in the stack
        while stack:
            node, temp = stack.pop()                                    # (2) pop the last node
            if not node.left and not node.right and sum(temp) == sum1:   
                return True
            if node.right:                                              # (2.2) keep append if if's not leaf
                stack.append((node.right, temp+[node.right.val]))
            if node.left:
                stack.append((node.left, temp+[node.left.val]))
        return False   
    
# O(N): access N node
# O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced