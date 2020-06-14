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
        sum -= root.val                                
        if not root.left and not root.right:
            return sum == 0
        
        # (3) recursively call function for each child node
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
    
# Time: O(N): access N node
# Space: O(N) when the tree is unbalanced, O(h=logN) when the tree is balanced

    
# iteratively substraction
class Solution(object):
    def hasPathSum(self, root, sum):
        # (0) edge case
        if not root:
            return False
        
        # (1) save root and target in stack
        stack = [(root, sum-root.val)]
        
        # (2) pop and append elements
        while stack:
            node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == 0:   # (2.1) check when it's leaf node 
                return True
            if node.right:                                          # (2.2) keep append if it's not leaf
                stack.append((node.right, cur_sum-node.right.val))
            if node.left:
                stack.append((node.left, cur_sum-node.left.val))
                
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