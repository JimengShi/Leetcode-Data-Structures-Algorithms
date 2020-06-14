# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return root

        stack = [root]
        res = []
        flag = 1
        while stack:
            res.append([i.val for i in stack[::flag]])   # change direction when print, stack dosen't change
            flag *= -1
            
            temp = []
            for i in stack:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            stack = temp[:]

        return res
    
# Time: O(N) since each node is processed exactly once.
# Space: O(N) to keep the output structure which contains N node values.    