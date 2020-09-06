# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.

# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursively
class Solution(object):
    def buildTree(self, preorder, inorder): 
        # (0) edge case
        if not inorder or not preorder:
            return None
        
        # (1) Find index of root node within in-order traversal
        val = preorder.pop(0)
        index = inorder.index(val)
        root = TreeNode(val)

        # (2) Recursively build left and subtree
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])
        
        # (3) return output
        return root

# Time: O(n), T(n) = 2T(n/2) + O(1)
# Space: O(n), record the entire tree node
    
    
# iteratively
class Solution:
    def buildTree(self, preorder, inorder):
        # (0) edge case
        if not preorder or not inorder:
            return None
        
        # (1) construct hashmap to save inorder index, idx = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4} control go L or R
        idx = {}                            
        for i, val in enumerate(inorder):
            idx[val] = i 
            
        # (2) make sure the root
        root = TreeNode(preorder[0])
        stack = [root]
        
        # (3) Iterate preorder from the 2nd number and construct the tree, preorder = [3,9,20,15,7]
        for j in range(1, len(preorder)):
            cur_node = TreeNode(preorder[j])              # (3.1) save cur_node as TreeNode

            if idx[cur_node.val] < idx[stack[-1].val]:    # (3.2) go left if curr.index < previous index in stack
                stack[-1].left = cur_node                 
            else:                                         # (3.3) go right when find the last index < curr.index
                while stack and idx[cur_node.val] > idx[stack[-1].val]:
                    temp = stack.pop()
                temp.right = cur_node

            stack.append(cur_node)                        # (3.3) save cur_node in stack
                
        # (4) return output
        return root
    
# Time: O(n), traverse once
# Space: O(n), record the entire tree node  