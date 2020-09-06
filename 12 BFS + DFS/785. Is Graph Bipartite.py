# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B 
# such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i 
# and j exists. Each node is an integer between 0 and graph.length - 1.  
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.


# Method 1: BFS with a queue
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                queue = deque([node])
                colors[node] = 1               # 1 is just starting color
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in colors:
                            nei.append(nei)
                            colors[nei] = colors[node] * -1    
                        elif colors[nei] == colors[node]:
                            return False

        return True

# Time: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.
# Space: O(N), the space used to store the color.


# Method 2: DFS with a stack
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                stack = [node]
                colors[node] = 1               # 1 is just starting color
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in colors:
                            nei.append(nei)
                            colors[nei] = colors[node] * -1
                        elif colors[nei] == colors[node]:
                            return False

        return True
    
# Time: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.
# Space: O(N), the space used to store the color.


# Method 3: DFS with recursion
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i):
            for nb in graph[i]:
                if nb in color:
                    if color[nb] == color[i]:
                        return False
                else:
                    color[nb] = color[i] * -1
                    if not dfs(nb):
                        return False
            return True
        
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 1
                if not dfs(i):
                    return False
        return True 
    
# Time: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.
# Space: O(N), the space used to store the color.
    
# Time: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.
# Space: O(N), the space used to store the color.