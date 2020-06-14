# Method: Sorting
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dis = []
        res = [0] * len(workers)
        
        # Compute the distance between each pair of bike and worker
        for b in range(len(bikes)):
            for w in range(len(workers)):
                dis.append( (abs(workers[w][0]-bikes[b][0]) + abs(workers[w][1]-bikes[b][1]), w, b) )
        
        # dis is sorted based on distance, then worker index, finally bike index
        dis = sorted(dis)
        for i in range(len(dis)):
            if workers[dis[i][1]] and bikes[dis[i][2]]:
                res[dis[i][1]] = dis[i][2]
                
                workers[dis[i][1]] = None       # worker assigned
                bikes[dis[i][2]] = None         # bike assigned
                
        return res
    
    
# [(3, 0, 0)]
# [(3, 0, 0), (2, 1, 0)]
# [(3, 0, 0), (2, 1, 0), (6, 0, 1)]
# [(3, 0, 0), (2, 1, 0), (6, 0, 1), (3, 1, 1)]

# [(2, 1, 0), (3, 0, 0), (3, 1, 1), (6, 0, 1)]

# Time: O(mn*logmn), m is the length of bikes array, n is the length of workers array.
# Space: O(mn)