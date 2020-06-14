# BSF + Topologitcal
# Time: O(|E| + |V|) where |V| is the number of courses, and |E| is the number of dependencies.
# O(|E|) to build a graph in the first step. 
# we would visit each vertex and each edge once in the worst case, O(|E| + |V|) for BFS.
# As a result, the overall would be O(2*|E| + |V|).

# Space: O(∣E∣+∣V∣)
# We built a graph data structure, which would consume O(|E|) for pre and O(|V|) for count space.
# We use a container (queue) to keep track of the courses that have no prerequisite, and the size of the container would be bounded by ∣V∣. And for result would consume O(|V|).
# As a result, the overall space complexity of the algorithm would be O(2*∣E∣+2*∣V∣).

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # (0) edge case
        if not numCourses:
            return
        
        # (1) initialize pre to build graph) and count to record indgree of each node
        pre = defaultdict(list)
        count = defaultdict(int)
        for i in prerequisites:
            pre[i[1]].append(i[0])                  # pre = {0: [4], 1: [4, 3], 2: [3], 4: [5], 3: [5]})
            count[i[0]] += 1                        # count = {4: 2, 3: 2, 5: 2}
            #count[i[0]] = count.get(i[0], 0) + 1   # count = {4: 2, 3: 2, 5: 2} when count = {} firstly
            
        # (2) bfs to search
        queue = []
        for i in range(numCourses):
            if i not in count:                      # (2.1) at first enqueue those node without indegree
                queue.append(i)
                
        res = []                         # (2.2) record how many node we already visited
        while queue:
            cur_node = queue.pop(0)                 # (2.3) pop the first element in the queue
            res.append(cur_node)
            
            for neighbor in pre[cur_node]:          # (2.4) update count for neighbor in pre[cur_node]
                count[neighbor] -= 1
                if count[neighbor] == 0:
                    queue.append(neighbor)
        
        # (3) return results
        if len(res) == numCourses:
            return res