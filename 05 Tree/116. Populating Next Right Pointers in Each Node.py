"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # (0) edge case
        if not root:
            return root
        
        # (1) Initialize a queue data structure which contains just the root of the tree
        Q = collections.deque([root])
        
        # (2) Outer while loop which iterates over each level
        while Q:
            size = len(Q)
            for i in range(size):           # (2.0) Iterate over all the nodes on the current level
                node = Q.popleft()

                if i < size - 1:            # (2.1) connect node with node.next
                    node.next = Q[0]
                if node.left:               # (2.2) add left child of node into queue
                    Q.append(node.left)
                if node.right:              # (2.3) add right child of node into queue
                    Q.append(node.right)
                    
            # node.next = None
            
        # (3) return the root node, since the tree has now been modified
        return root
    
# Time: O(N) since we process each node exactly once. Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
# Space: O(N).    
    
    
    
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # (0) edge case
        if not root:
            return root
        
        # (1) Start with the root node. There are no next pointers that need to be set up on the first level
        leftmost = root
        
        # (2) Once we reach the final level, we are done
        while leftmost.left:
            
            # (2.1) connect the nodes on the current level
            head = leftmost
            while head:
                head.left.next = head.right             # (2.1.1) connect nodes with a same parent
                if head.next:                           # (2.1.2) connect nodes with differnet parent
                    head.right.next = head.next.left
                head = head.next                        # (2.1.3) move head to the next node on current level
            
            # (2.2) move onto the next level
            leftmost = leftmost.left                    
        
        # (3) return the root node, since the tree has now been modified
        return root
    
    
# Time: O(N) since we process each node exactly once.
# Space: O(1) since we don't make use of any additional data structure for traversing nodes on a particular level like the previous approach does.