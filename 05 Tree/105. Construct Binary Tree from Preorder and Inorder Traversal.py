# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursively
# class Solution(object):
#     def buildTree(self, preorder, inorder): 
#         # (0) edge case
#         if not inorder or not preorder:
#             return None
        
#         # (1) Find index of root node within in-order traversal
#         val = preorder.pop(0)
#         index = inorder.index(val)
#         root = TreeNode(val)

#         # (2) Recursively build left and subtree
#         root.left = self.buildTree(preorder, inorder[:index])
#         root.right = self.buildTree(preorder, inorder[index+1:])
        
#         # (3) return output
#         return root

# Time: O(n), T(n) = 2T(n/2) + O(1)
# Space: O(n), record the entire tree node
    
    
# iteratively
class Solution:
    def buildTree(self, preorder, inorder):
    	# (1) construct hashmap to save inorder index
        idx = {}                            # idx = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        for i, val in enumerate(inorder):
            idx[val] = i 
			
	    # (2) Iterate over preorder and construct the tree 
        stack = []
        root = None
        for val in preorder:                # preorder = [3,9,20,15,7]
            # (2.1) determine root in preorder and save it in stack
            if not root:
                root = TreeNode(val)
                stack.append(root)
            
            # (2.2) determine node goes to left or right if it's not root
            else:
                cur_node = TreeNode(val)                            # (2.2.1) save cur_node as TreeNode
                if idx[val] < idx[stack[-1].val]:                   
                    stack[-1].left = cur_node                       # (2.2.2) go to left or right
                else:                                               
                    while stack and idx[val] > idx[stack[-1].val]:
                        temp = stack.pop()
                    temp.right = cur_node
                stack.append(cur_node)                              # (2.2.3) save cur_node in stack
                
        # (3) return output
        return root
    
# Time: O(n), traverse once
# Space: O(n), record the entire tree node   