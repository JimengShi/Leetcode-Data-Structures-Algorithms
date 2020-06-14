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
            count = 0
            if not node:
                return 0
            if node.val == sum1:
                count += 1
            count += dfs(node.left, sum1-node.val) 
            count += dfs(node.right, sum1-node.val)
            return count
        
        # (3) recursion: root, root.left, root.right
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

        # dfs(root, sum): return the count from root to bottom
        # self.pathSum(root.left, sum): return the count from root.left to bottom
        # self.pathSum(root.left, sum): return the count from root.left to bottom

# Time: O(N)
# Space: O(N)


import collections

class Solution:
    def pathSum(self, root, sum):  
        if not root:
            return 0
        
        target = sum
        count = 0   
        sum_d = collections.defaultdict(int)
        sum_d[0] = 1
        
        stack = [(root, 0, False)]
        while stack:
            node, cur_sum, backtrack = stack.pop()
            if backtrack:
                sum_d[cur_sum] -= 1
                continue
            
            cur_sum += node.val
            count += sum_d[cur_sum - target]
            
            sum_d[cur_sum] += 1
            stack.append((None, cur_sum, True))
            if node.left:
                stack.append((node.left, cur_sum, False))
                
            if node.right:
                stack.append((node.right, cur_sum, False))
                
        return count