# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: DFS - stack
# Time: O(n)
# Space: O(n).
# Note:
# append(left) first and then append(right) to get the values of node when you stand right
# append(right) first and then append(left) to get the values of node when you stand left
# because this uses stack(FILO), we need to append(left) first if we want right

class Solution(object):
    def rightSideView(self, root):
        # (0) edge case
        if not root:
            return []

        # (1) initialize an empty result and empty stack and prelevel
        res = []
        stack = []
        stack.append([root, 1])                     # keep track of node and its level
        preLevel = 0
        
        # (2) dfs traversal with a stack
        while stack:
            curr_node, level = stack.pop(-1)
            if level == preLevel + 1:
                res.append(curr_node.val)
                preLevel += 1
            
            if curr_node.left:
                stack.append([curr_node.left, level+1])
            if curr_node.right:
                stack.append([curr_node.right, level+1])

        # (3) return reslut
        return res        

    
# Method 1: DFS - stack
# Time: O(n)
# Space: O(n).
# Note:
# append(right) first and then append(left) to get the values of node when you stand right
# append(left) first and then append(right) to get the values of node when you stand left
# because this uses queue(FIFO), we need to append(right) first if we want right

class Solution(object):
    def rightSideView(self, root):
        # (0) edge case
        if not root:
            return []

        # (1) initialize an empty result and empty queue and prelevel
        res = []
        queue = []
        queue.append([root, 1])
        lastLevel = 0

        # (2) bfs traversal with a queue
        while queue:
            curr_node, level = queue.pop(0)
            if level == lastLevel + 1:
                res.append(curr_node.val)
                lastLevel += 1
                
            if curr_node.right:
                queue.append([curr_node.right, level+1])
            if curr_node.left:
                queue.append([curr_node.left, level+1])

        return res