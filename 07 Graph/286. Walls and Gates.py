from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # (0) edge case
        if not rooms:
            return -1
        
        # (1) maintain a queue to save gate
        queue = deque()
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:        # gate
                    queue.append((x,y, 0))

        if len(queue) == 0:                     # no gates
            return rooms
        
        # (2) BFS while queue has gates
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue: 
            x, y, dist = q.popleft()
            for dir in dirs:
                new_x, new_y = x+dir[0], y+dir[-1]
                if 0 <= new_x <= len(rooms)-1 and 0 <= new_y <= len(rooms[0])-1 and rooms[new_x][new_y] == 2147483647:  # empty room
                    rooms[new_x][new_y] = dist + 1          # update distance - Once we set a room's distance, we mark it as visited
                    q.append((new_x, new_y, dist+1))        # push newly found room into queue
        
        # (3) return results
        return rooms
    
    
# Time: O(mn)
# Space: O(mn)