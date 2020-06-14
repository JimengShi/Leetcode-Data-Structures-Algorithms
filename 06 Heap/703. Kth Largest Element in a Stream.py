class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        
        # deal with the original nums to build a heap with size of k
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heapq.heappushpop(self.heap, num)  
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)      
        return self.heap[0]
        
# heappushpop(): push item on the heap, then pop and return the smallest item from the heap
# O(N*logK), N is the number of the new coming data
# O(K)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)