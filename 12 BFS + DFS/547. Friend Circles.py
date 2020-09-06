# There are N students in a class. Some of them are friends, while some are not. 
# Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, 
# then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

# Given a N*N matrix M representing the friend relationship between students in the class. 
# If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
# And you have to output the total number of friend circles among all the students.

# Example 1: Input: 
#                 [[1,1,0],
#                  [1,1,0],
#                  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.

# Example 2: Input: 
#                 [[1,1,0],
#                  [1,1,1],
#                  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

# Method 1: DFS with recursion              
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # (2) dfs
        def dfs(i):
            visited.add(i)
            for j in range(len(M)):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
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
                        if M[f][j] == 1 and j not in visited:
                            friends.append(j)
                            visited.add(j)
                circle += 1
                
        # (3) return result
        return circle

# Time: O(n^2) since two for loops
# Space: O(1)