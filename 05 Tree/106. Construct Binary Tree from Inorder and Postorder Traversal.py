# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.

# For example, given
# postorder = [9,15,7,20,3]
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
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # (0) edge case
        if not inorder or not postorder:
            return None
        
        # (1) Find index of root node within in-order traversal
        val = postorder.pop()
        index = inorder.index(val)
        root = TreeNode(val)
        
        # (2) Recursively build right and left subtree
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        
        # (3) return output
        return root

# O(n): T(n) = 2T(n/2) + O(1)
# O(n): record the entire tree node


# iteratively
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
                
        # (1) construct hashmap to save inorder index
        idx = {}                            # idx = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        for i, val in enumerate(inorder):
            idx[val] = i 
            
        # (2) Iterate over preorder and construct the tree
        root = TreeNode(postorder[-1])
        stack = [root]
        
        # (3) Iterate preorder from the last number to 1st and construct the tree
        for val in postorder[:-1][::-1]:                        # postorder = [9,15,7,20,3]
            curr_node = TreeNode(val)
            if idx[val] > idx[stack[-1].val]:                   
                stack[-1].right = curr_node
            else:                                               
                while stack and idx[val] < idx[stack[-1].val]:
                    temp = stack.pop()
                temp.left = curr_node
            stack.append(curr_node)
                
        # (4) return output
        return root
    
# Time: O(n), traverse once
# Space: O(n), record the entire tree node   