# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order. The answer is guaranteed to be unique (except for order that it is in.)

# Example 1:
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]

# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10). The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]


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
        heap = []
        for point in points:
            x, y = point[0], point[1]
            dist = -(x**2 + y**2)
            if len(heap) < K:
                heapq.heappush(heap, (dist, x, y))
            else:
                if dist > heap[0][0]:
                    heapq.heappushpop(heap, (dist, x, y))
        
        return [(x, y) for (dist, x, y) in heap]
    
# Time: O(Nlogk) for extracting K times, where N is length of points.
# Space: O(k).


# Method 3: min heap with size of N
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points):
            return points
        
        heap = []
        for point in points:
            heapq.heappush(heap, (point[0]**2+point[1]**2, point))

        res = []
        for _ in range(K):
            curr_sum, curr_point = heapq.heappop(heap)
            res.append(curr_point)
        
        return res
    
# Time: O(N+KlogN)
# Space: O(k).


# Method 3: min heap with size of N
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [(point[0]**2+point[1]**2, point) for point in points]
        heapq.heapify(heap)
        
        res = []
        for _ in range(K):
            dist, point = heapq.heappop(heap)
            res.append(point)
        
        return res
    
# Time: O(N) for building heap, O(klogN) for extracting K times, where N is length of points.
# Space: O(k).


# Mthod 4: Divide and Conquer: quicksort
class Solution(object):
    def kClosest(self, points, K):
        # (1) [[3,3],[5,-1],[-2,4]]  -->  [(18,[3,3]), (26,[5,-1]), (20,[-2,4])]
        for i in range(len(points)):
            points[i] = (points[i][0]**2 + points[i][1]**2, points[i])
        
        # (2) [(18,[3,3]), (26,[5,-1]), (20,[-2,4])]  -->  [(18,[3,3]), (20,[-2,4]), (26,[5,-1])] 
        self.quicksort(points, 0, len(points)-1)

        # (3) save the Kth smallest result
        res = []
        for i in range(K):
            res.append(points[i][1])
        return res

    
    def quicksort(self, arr, l, r):
        if len(arr) <= 1:
            return arr
        if l < r:
            pos = self.partition(arr, l, r)
            self.quicksort(arr, l, pos-1)
            self.quicksort(arr, pos+1, r)
        return arr
        
    def partition(self, arr, l, r):
        pivot = arr[l]
        while l < r:
            while l < r and arr[r][0] >= pivot[0]:  # compare the first element in tuple (distance)
                r -= 1
            arr[l] = arr[r]
            
            while l < r and arr[l][0] <= pivot[0]:  # compare the first element in tuple (distance)
                l += 1
            arr[r] = arr[l]
        arr[l] = pivot
        return l
        
# Time: O(NlogN) in the average case, O(N^2) in the worst case.
# Space: O(1).