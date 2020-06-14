# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: recursion
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n) The number of recursive calls is bound by the height of the tree. In the worst case, the tree height is in O(n). Therefore, space complexity due to recursive calls on the stack is O(n) in the worst case.


# Method 2: queue
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # (1) create data structure queue
        queue = [p, q]
        
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
            queue.append(right.left)
            queue.append(left.right)
            queue.append(right.right)
        
        # (3) otherwise return True
        return True
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)


# Method 3: stack
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        stack = [(p, q)]
        while stack:
            root1, root2 = stack.pop()
            if not root1 and not root2:
                continue   
            elif root1 and root2 and root1.val == root2.val:
                pass
            else:
                return False
                break        
            
            stack.append((root1.left, root2.left))
            stack.append((root1.right, root2.right))
            
        return True
    
# Time: O(n), because we traverse the entire input once, where n is total number of nodes in the tree.
# Space: O(n)