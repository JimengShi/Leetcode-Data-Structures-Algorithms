# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

# BFS
import collections 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # (0) edge case
        if not root:
            return root
        
        # (1) Initialize a queue data structure which contains just the root of the tree
        queue = collections.deque([root])
        
        # (2) Outer while loop which iterates over each level
        while queue:
            size = len(queue)
            for i in range(size):              # (2.0) Iterate over all the nodes on current level
                node = queue.popleft()

                if i < size-1:                 # (2.1) connect node with node.next
                    node.next = queue[0]
                if node.left:                  # (2.2) add left child of node into queue
                    queue.append(node.left)
                if node.right:                 # (2.3) add right child of node into queue
                    queue.append(node.right)
                    
            node.next = None
            
        # (3) return the root node, since the tree has now been modified
        return root
    
# Time: O(N) since we process each node exactly once. Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
# Space: O(N). 



# DFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = {}
        
        def inorder(node, level):
            if not node:
                return

            if d.get(level):
                d[level].next = node
                
            d[level] = node
            inorder(node.left, level+1)
            inorder(node.right, level+1)
                
        inorder(root, 0)
        return root
    
# Time: O(N)
# Space: O(1)