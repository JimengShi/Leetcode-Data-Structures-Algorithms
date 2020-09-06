# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example: root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def pathSum(self, root, sum):
        # (1) edge case before helper function
        if not root:
            return 0
        
        # (2) process: helper function which is used to return the count from root to bottom
        def dfs(node, sum1):
            # (2.1) end condition 
            count = 0
            if not node:
                return 0

            # (2.2) process
            if node.val == sum1:
                count += 1

            # (2.3) recursion
            count += dfs(node.left, sum1-node.val) 
            count += dfs(node.right, sum1-node.val)

            return count
        
        # (3) recursion: dfs from root, dfs from root.left, dfs from root.right
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

# Time: O(N)
# Space: O(N)