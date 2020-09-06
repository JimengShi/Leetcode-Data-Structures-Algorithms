# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

# Example:
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.size = k
        
        # deal with the original nums to build a heap with size of k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)  
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)      
        return self.heap[0]


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