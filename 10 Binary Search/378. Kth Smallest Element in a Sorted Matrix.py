# Method 1: binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # (0) edge case
        if not matrix:
            return
        
        # (1) two pointers
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]
        
        # (2) while loop
        while lo < hi:
            mid = (lo + hi) // 2
            pos = sum(bisect.bisect_right(row, mid) for row in matrix)
            
            if pos < k:           # low  high  mid
                lo = mid + 1      #  13   14    13  since it's left mean, we set lo = mid + 1 so that we can update
            else:
                hi = mid
        
         # (3) return result
        return hi
    
# Time: O(nlogn) in the worst case
# Space: O(1)

    

# Method 2: min heap
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # (1) put first row into heap
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[0][i], 0, i))
        
        # (2) pop k time from heap
        while k > 0:                                     # be equivalent to for i in range(k)
            cur, row, col = heapq.heappop(heap)
            k -= 1
            if row + 1 < len(matrix):                    # there is still element below (row, col)
                heapq.heappush(heap, (matrix[row+1][col], row+1, col))
        
        # (3) return result
        return cur

# Time: O(nlogn + klogn)
# Space: O(N)