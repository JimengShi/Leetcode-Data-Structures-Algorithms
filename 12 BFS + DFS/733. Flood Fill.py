# Method 1: DFS with visited set
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        visited = set()
        
        # (2) dfs function
        def dfs(r, c):
            if image[r][c] == base_color:
                image[r][c] = newColor
                visited.add((r, c))
                
                directions = [(0,1), (0,-1), (-1,0), (1,0)]
                for dx, dy in directions:
                    x, y = r, c
                    if 0 <= x+dx < R and 0 <= y+dy < C and (x+dx, y+dy) not in visited:
                        new_r = x + dx
                        new_c = x + dy
                        dfs(new_r, new_c)
        
        # (3) call dfs function and return result
        dfs(sr, sc)
        return image
    
# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.


# Method 2: DFS without visited set
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        
        # (2) dfs function
        def dfs(r, c):
            if image[r][c] == base_color:
                image[r][c] = newColor
                
                directions = [(0,1), (0,-1), (-1,0), (1,0)]
                for dx, dy in directions:
                    x, y = r, c
                    if 0 <= x+dx < R and 0 <= y+dy < C:
                        new_r = x + dx
                        new_c = y + dy
                        dfs(new_r, new_c)
        
        # (3) call dfs function and return result
        dfs(sr, sc)
        return image
    
# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.


# Method 3: DFS with stack and visited set
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        visited = set()
        stack = [(sr, sc)]
        
        # (2) dfs
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            visited.add((r, c))
            
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                if 0 <= r+dr < R and 0 <= c+dc < C and (r+dr, c+dc) not in visited:
                    new_r = r + dr
                    new_c = c + dc
                    if image[new_r][new_c] == base_color:
                        stack.append((new_r, new_c))
                    
        # (3) return result            
        return image

# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.


# Method 4: DFS with only stack
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # (0) edge case
        base_color = image[sr][sc]
        if base_color == newColor:
            return image
        
        # (1) initialize data structure
        R, C = len(image), len(image[0])
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            image[r][c] = newColor
            
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                if 0 <= r+dr < R and 0 <= c+dc < C:
                    new_r = r + dr
                    new_c = c + dc
                    if image[new_r][new_c] == base_color:
                        stack.append((new_r, new_c))
                    
        # (3) return result            
        return image
    
# Time: O(N), where N is the number of pixels in the image. We might process every pixel.
# Space: O(N), the size of the implicit call stack when calling dfs.