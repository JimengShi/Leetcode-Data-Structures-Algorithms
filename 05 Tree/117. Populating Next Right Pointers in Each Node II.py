# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

# import collections 
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         # (0) edge case
#         if not root:
#             return root
        
#         # (1) Initialize a queue data structure which contains just the root of the tree
#         Q = collections.deque([root])
        
#         # (2) Outer while loop which iterates over each level
#         while Q:
#             size = len(Q)
#             for i in range(size):           # (2.0) Iterate over all the nodes on the current level
#                 node = Q.popleft()

#                 if i < size - 1:            # (2.1) connect node with node.next
#                     node.next = Q[0]
#                 if node.left:               # (2.2) add left child of node into queue
#                     Q.append(node.left)
#                 if node.right:              # (2.3) add right child of node into queue
#                     Q.append(node.right)
                    
#             # node.next = None
            
#         # (3) return the root node, since the tree has now been modified
#         return root
    
# Time: O(N) since we process each node exactly once. Note that processing a node in this context means popping the node from the queue and then establishing the next pointers.
# Space: O(N).

    
class Solution:
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            # If the "prev" pointer is already set, i.e. if we already found a one node on the next level
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node, we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
                
            prev = childNode
            
        return prev, leftmost
    
    
    def connect(self, root: 'Node') -> 'Node':
        # (0) edge case
        if not root:
            return root
        
        # (1) The root node is the only node on the first level, hence it's the leftmost node for that level
        leftmost = root
        
        # (2) keep going until we do find the last level, once we reach the final level, we are done
        while leftmost:
            
            # (2.1) initialize curr node on the current level and prev on the next level
            prev = None           # "prev" tracks latest node on the "next" level
            curr = leftmost       # "curr" tracks latest node on the current level
            leftmost = None       # reset this so that we can re-assign it to the leftmost node of the next level.
            
            # (2.2) Iterate on the nodes in the current level using the next pointers
            while curr:
                
                # (2.2.1) connect current level and update the prev and leftmost pointers
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # (2.2.2) Move onto the next node.
                curr = curr.next
        
        # (3) return the root node, since the tree has now been modified 
        return root
    
    
# Time: O(N) since we process each node exactly once.
# Space: O(1) since we don't make use of any additional data structure for traversing nodes on a particular level like the previous approach does.