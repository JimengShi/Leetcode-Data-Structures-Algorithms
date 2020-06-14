# Method 1: sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]

# Time: O(NlogN), where N is the length of points.
# Space: O(N).


# Method 2: min heap with size of k
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:     
        ans = []
        for point in points:
            x, y = point[0], point[1]
            distence = -(x**2 + y**2)
            
            if len(ans) >= K:
                heapq.heappushpop(ans, (distence, x, y))
            else:
                heapq.heappush(ans, (distence, x, y))
        
        return [(x, y) for (dist, x, y) in ans]
    
# Time: O(N) for building heap, O(Nlogk) for extracting K times, where N is length of points.
# Space: O(k).    
    
# Method 2: min heap
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # (1) build a heap to save all points
        heap = list()
        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)        # distance
            heapq.heappush(heap, (d, point))
        
        # (2) heapq.heappop(heap) k times to get k closest
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        
        # (3) return result
        return res

# Time: O(N) for building heap, O(KlogN) for extracting K times, where N is length of points.
# Space: O(N).


# Method 3: Divide and Conquer: quicksort
class Solution(object):
    def kClosest(self, points, K):
        results = []
        for i in range(len(points)):
            points[i] = (points[i][0]**2 + points[i][1]**2, points[i])  # (distance, point) tuple
            
        self.quickSelectHelper(points, 0, len(points)-1, K)
        print(points)
        for i in range(K):
            results.append(points[i][1])
        return results

    def quickSelectHelper(self, arr, start, end, K):
        if start >= end: 
            return
        
        i, j = start + 1, end
        while i <= j:
            while i <= j and arr[i][0] <= arr[start][0]:  # compare the first element in tuple (distance)
                i += 1
            while i <= j and arr[j][0] >= arr[start][0]:  # compare the first element in tuple (distance)
                j -= 1
            if i < j: 
                arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], arr[start]
        
        if K == j:
            return
        elif K < j:
            self.quickSelectHelper(arr, start, j-1, K)
        else:
            self.quickSelectHelper(arr, j+1, end, K)

               
# Time: O(N) in the average case, O(N^2) in the worst case.
# Space: O(1).