# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: recursively
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # (0) edge case
        if not root:
            return 0
        
        # (1) get depth of root.left and root.right  
        dl = self.maxDepth(root.left)
        dr = self.maxDepth(root.right)
        
        # (2) return the final result
        return 1 + max(dl, dr)
        
# Time: O(N)
# Space: O(logN)
    

# Method 2: iteratively DFS
class Solution:
    def maxDepth(self, root):
        # (0) edge case
        if not root:
            return 0
        
        # (1) initialize
        depth = 1
        stack = [(1, root)]
        
        # (2) update depth
        while stack:
            curr_depth, root = stack.pop()
            depth = max(depth, curr_depth)
            if root.left:
                stack.append((curr_depth + 1, root.left))
            if root.right:
                stack.append((curr_depth + 1, root.right))
        
        # (3) return result
        return depth
    
# Time: O(N)
# Space: O(logN)



# Method 2: iteratively BFS
class Solution:
    def maxDepth(self, root):
        # (0) edge case
        if not root:
            return 0
        
        # (1) initialize
        depth = 0
        queue = [root]
        
        # (2) update depth
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # (3) return result
        return depth
    
# Time: O(N)
# Space: O(logN)