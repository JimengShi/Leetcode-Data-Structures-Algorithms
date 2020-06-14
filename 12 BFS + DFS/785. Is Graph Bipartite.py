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