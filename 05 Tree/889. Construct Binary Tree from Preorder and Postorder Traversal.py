# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursively    
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # (0) edge case
        if not pre or not post:
            return None
        
        # (1) find root and check the edge case
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        
        # (2) make sure the 1st element in pre which is the root of left subtree
        ind = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1 : ind+2], post[ : ind+1])
        root.right = self.constructFromPrePost(pre[ind+2 :], post[ind+1 : -1])
        
        # (3) return result
        return root
    
# Time: O(N^2) where N is the number of nodes.
# Space: O(N^2).
    
# idx  =  0  1  2  3  4  5  6
# pre  =  1 [2  4  5] 3  6  7
#            i
# post = [4  5  2] 6, 7, 3, 1]
#               j


# iterative
class Solution:
    def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

# Time: O(n)
# Space: O(n)