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
    	# (1) construct hashmap to save inorder index
        idx = {}                            # idx = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        for i, val in enumerate(inorder):
            idx[val] = i 
			
	    # (2) Iterate over preorder and construct the tree 
        stack = []
        root = None
        for val in postorder[::-1]:                # postorder = [9,15,7,20,3]
            # (2.1) determine root in preorder and save it in stack
            if not root:
                root = TreeNode(val)
                stack.append(root)
            
            # (2.2) determine node goes to left or right if it's not root
            else:
                cur_node = TreeNode(val)                             # (2.2.1) save cur_node as TreeNode
                if idx[val] > idx[stack[-1].val]:                   
                    stack[-1].right = cur_node                       # (2.2.2) go to left or right
                else:                                               
                    while stack and idx[val] < idx[stack[-1].val]:
                        temp = stack.pop()
                    temp.left = cur_node
                stack.append(cur_node)                               # (2.2.3) save cur_node in stack
                
        # (3) return output
        return root
    
# Time: O(n), traverse once
# Space: O(n), record the entire tree node   