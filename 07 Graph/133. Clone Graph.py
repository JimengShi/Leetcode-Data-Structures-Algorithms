# Definition for a Node.
# class Node(object):
#     def __init__(self, val, neighbors):
#         self.val = val
#         self.neighbors = neighbors

# DFS with a stack
# Clone node + clone edge
# Time: O(N) since we process each node exactly once.
# Space: O(N). O(n) is occupied by the visited hash map and O(H) occupied by the recursion stack, where H is the height of the graph. Overall, the space complexity would be O(N).

class Solution(object):
    def cloneGraph(self, node):
        # (0) edge case
        if not node:
            return node

        # (1) Dictionary to save the visited node and its clone as key and value respectively. This helps to avoid cycles.
        visited = {}
        stack = [node]
        visited[node] = Node(node.val, [])                              # Clone the node and put it in visited dictionary, neighbor=empty.

        # (2) Start DFS traversal
        while stack:
            curr_node = stack.pop()                                     # Pop a node, say "curr_node" from the front of the queue.
            for neighbor in curr_node.neighbors:                        # Iterate through all the neighbors of the curr_node
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])          # Clone the neighbor and put in the visited if not present already
                    stack.append(neighbor)                              # Add the newly encountered node to the queue.
                visited[curr_node].neighbors.append(visited[neighbor])  # ***Add clone of the neighbor to the neighbors of curr_node.***

        # (3) Return the clone of the node from visited.
        return visited[node]
    
    
# BFS with a queue
# Clone node + clone edge  
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        # (0) edge case
        if not node:
            return node

        # (1) Dictionary to save the visited node and its clone as key and value respectively. This helps to avoid cycles.
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])                              # Clone the node and put it in visited dictionary, neighbor=empty.

        # (2) Start BFS traversal
        while queue:
            curr_node = queue.popleft()                                 # Pop a node, say "curr_node" from the front of the queue.
            for neighbor in curr_node.neighbors:                        # Iterate through all the neighbors of the curr_node
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])          # Clone the neighbor and put in the visited if not present already
                    queue.append(neighbor)                              # Add the newly encountered node to the queue.
                visited[curr_node].neighbors.append(visited[neighbor])  # Add clone of the neighbor to the neighbors of curr_node.

        # (3) Return the clone of the node from visited.
        return visited[node]