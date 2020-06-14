import heapq
class Solution:
    def nthUglyNumber(self, n):
        # (0) edge case
        if n < 1 or not n:
            return
        
        # (1) initialize a heap with 1st element 1
        heap = [1]
        n = n - 1
        
        # (2) traverse n-1 times since we already ensure the 1st element in heap is 1
        while n:
            tmp = heapq.heappop(heap)               # (2.1) get the 1st out of heap
            
            while heap and tmp == heap[0]:          # (2.2) keep popping if 1st element is same as next
                tmp = heapq.heappop(heap)
            
            primes = [2, 3, 5]                      # (2.3) add more elements to build heap
            for p in primes:
                heapq.heappush(heap, p * tmp)
            n -= 1                                  # (2.4) update n = n - 1

        # (3) return result
        return heapq.heappop(heap)

# 1
# heap: [2, 3, 5]
# --------------------
# 2
# heap: [3, 5, 4, 6, 10]
# --------------------
# 3
# heap: [4, 5, 9, 6, 6, 10, 15]
# --------------------
# 4
# heap: [5, 6, 8, 6, 15, 10, 9, 12, 20]
# --------------------
# 5
# heap: [6, 6, 8, 10, 15, 10, 9, 20, 12, 15, 25]
# --------------------
# 6
# tmp 6
# heap: [8, 10, 9, 12, 12, 10, 15, 20, 25, 15, 18, 30]
# --------------------
# 8
# heap: [9, 10, 10, 12, 12, 16, 15, 20, 25, 15, 18, 30, 24, 40]
# --------------------
# 9
# heap: [10, 10, 15, 12, 12, 16, 18, 20, 25, 15, 18, 30, 24, 40, 27, 45]
# --------------------
# 10
# tmp 10
# heap: [12, 12, 15, 20, 15, 16, 18, 27, 25, 45, 18, 30, 24, 40, 20, 30, 50]
# --------------------    