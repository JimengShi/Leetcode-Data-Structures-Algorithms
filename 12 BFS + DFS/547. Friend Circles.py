# Method 1: DFS with recursion              
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # (2) dfs
        def dfs(i):
            visited.add(i)
            for j in range(len(M)):
                if M[i][j] == 1 and j not in visited:
                    dfs(j)
        
        # (1) initialize data structure         
        circle = 0
        visited = set()                    
        
        # (2) use dfs for each person who haven't been visited
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                circle += 1
        
        # (3) return result
        return circle
    
# Time: O(n^2) since two for loops
# Space: O(1)


# Method 2: DFS with stack
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # (1) initialize data structure
        circle = 0
        visited = set()
        
        # (2) use dfs for each person who haven't been visited
        for i in range(len(M)):
            if i not in visited:    
                friends = [i]                 # friends is a stack            
                while friends:
                    f = friends.pop()
                    visited.add(f)
                    for j in range(len(M)):
                        if M[f][j] == 1 and M[j][j] == 1 and j not in visited:
                            friends.append(j)
                circle += 1
                
        # (3) return result
        return circle