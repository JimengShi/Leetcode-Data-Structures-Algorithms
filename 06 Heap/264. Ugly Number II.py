# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Same Problem 313. Super Ugly Number

import heapq
class Solution:
    def nthUglyNumber(self, n):
        # (0) edge case
        if n < 1 or not n:
            return 0
        
        # (1) initialize a heap with 1st element 1
        heap = [1]
        
        # (2) traverse n-1 times since we already ensure the 1st element in heap is 1
        for i in range(n-1):
            tmp = heapq.heappop(heap)               # (2.1) get the 1st out of heap
            
            while heap and tmp == heap[0]:          # (2.2) keep popping if 1st element is same as next
                tmp = heapq.heappop(heap)
            
            primes = [2, 3, 5]                      # (2.3) add more elements to build heap
            for p in primes:
                heapq.heappush(heap, p * tmp)

        # (3) return result
        return heapq.heappop(heap)

# iteration: 0
# heap: [1]
# tmp: 1
# --------------------------
# iteration: 1
# heap: [2, 3, 5]
# tmp: 2
# --------------------------
# iteration: 2
# heap: [3, 5, 4, 6, 10]
# tmp: 3
# --------------------------
# iteration: 3
# heap: [4, 5, 9, 6, 6, 10, 15]
# tmp: 4
# --------------------------
# iteration: 4
# heap: [5, 6, 8, 6, 15, 10, 9, 12, 20]
# tmp: 5
# --------------------------
# iteration: 5
# heap: [6, 6, 8, 10, 15, 10, 9, 20, 12, 15, 25]
# tmp: 6
# --------------------------
# iteration: 6
# heap: [8, 10, 9, 12, 12, 10, 15, 20, 25, 15, 18, 30]
# tmp: 8
# --------------------------
# iteration: 7
# heap: [9, 10, 10, 12, 12, 16, 15, 20, 25, 15, 18, 30, 24, 40]
# tmp: 9
# --------------------------
# iteration: 8
# heap: [10, 10, 15, 12, 12, 16, 18, 20, 25, 15, 18, 30, 24, 40, 27, 45]
# tmp: 10
# --------------------------
# 12