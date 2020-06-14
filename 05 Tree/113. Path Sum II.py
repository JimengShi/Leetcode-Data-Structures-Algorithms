# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursively
class Solution:    
    def pathSum(self, root: TreeNode, summation: int) -> List[List[int]]:        
        res = []
        cur_path = []             # use stack to track downward traversal
        
        def dfs(node):
            if not node:
                return
            cur_path.append( node.val )                 
            if not node.left and not node.right and sum(cur_path) == summation:
                res.append( list(cur_path) )
            dfs( node.left )                         
            dfs( node.right )        
            cur_path.pop()                              # DFS of this subtree is completed
            
        dfs(root)
        return res

# O(N): access N node
# O(N): when the tree is unbalanced, O(h=logN) when the tree is balanced
        

# iteratively addtion
class Solution(object):
    def pathSum(self, root, summation):
        if not root:
            return []
        
        res = []
        stack = [(root, [root.val])]                                    # (1) save root info in the stack
        while stack:
            node, temp = stack.pop()                                    # (2) pop the last node
            if not node.left and not node.right and sum(temp) == summation:  # (2.1) check when it's leaf node 
                res.append(temp)
            if node.right:                                              # (2.2) keep append if if's not leaf
                stack.append((node.right, temp+[node.right.val]))
            if node.left:
                stack.append((node.left, temp+[node.left.val]))
        return res
    
        
# O(N): access N node
# O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced