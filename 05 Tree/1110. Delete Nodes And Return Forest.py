# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        td = set(to_delete)
        def process(node):
            if not node:
                return None
            
            node.left = process(node.left)
            node.right = process(node.right)
            
            if node.val not in td:
                return node
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
                
            return None

        root = process(root)
        if root:
            forest.append(root)
        
        return forest
    
    
# reference: https://www.youtube.com/watch?v=SEW3Vofoj_k
# Time: O(N), N is the length of tree
# Space: O(H), H is the height of tree