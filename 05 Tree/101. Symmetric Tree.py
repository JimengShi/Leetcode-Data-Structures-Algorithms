# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, p, q) -> bool:
        if not p and not q:   # base case 1
            return True
        elif not p or not q:  # base case 2
            return False
        elif p.val != q.val:  # base case 3
            return False
        else:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)
        
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n) The number of recursive calls is bound by the height of the tree. In the worst case, the tree height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.


# Method 2: queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # (0) edge case
        if not root:
            return True
        
        # (1) create data structure queue
        queue = [root.left, root.right]
        
        # (2) traverse input
        while len(queue) > 0:
            # (2.1) pop 2 nodes from queue
            left = queue.pop(0)
            right = queue.pop(0)
            
            # (2.2) evalate the pair that is just popped
            if not left and not right:                      # case 1: both empty --> don't have to append
                continue
            elif left and right and left.val == right.val:  # case 2: both exist and equal --> do nothing
                pass
            else:                                           # case 3: otherwise
                return False
                break
            
            # (2.3) Enqueue children: must be by this order
            queue.append(left.left)                
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        # (3) otherwise return True
        return True
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)


# Method 3: stack
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         # (0) edge case
#         if not root:
#             return True
        
#         # (1) create data structure stack
#         stack = [(root, root)]

#         # (2) traverse input
#         while stack:
#             node1, node2 = stack.pop()
#             if node1 is None and node2 is None:                # node1 empty and node2 empty
#                 continue
#             elif node1 and node2 and node1.val == node2.val:   # node1 empty or node2 empty
#                 pass
#             else:                                              # otherwise: return False and break
#                 return False
#                 break
            
#             stack.append((node1.left, node2.right))
#             stack.append((node1.right, node2.left))
        
#         # (3) otherwise return True
#         return True
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)