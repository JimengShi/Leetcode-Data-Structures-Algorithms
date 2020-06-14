# Method 1: slicing
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for l in range(len(nums)):
            if (l+k) > len(nums):
                break 
            max_element = max(nums[l:(l+k)])
            res.append(max_element)
        return res
    
    
# Method 1: slicing
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        # (0) edge case
        if not nums:
            return
        
        # (1) initialize the left pointer and maintain empty list save max_element
        res = []
        l = 0
        
        # (2) traverse the nums list and update max_element
        while l+k <= len(nums):                        # available window position
            max_element = max(nums[l:(l+k)])           # (2.1) compute max_element of each window
            res.append(max_element)                    # (2.2) update res
            l += 1
        
        # (3) return res
        return res
    
# Time: O((N-k+1)·k), where N is number of elements in the array, O(k) for max in python.
# Space: O(N−k+1) for an output array, actually there are N-k+1 windows.



# Method 2:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:     
        # (0) edge case
        if len(nums) == 0:
            return []
        
        # (1) intialize the queue and find the max of the first 3 element
        queue = []
        for i in range(k):                             # [1 3 -1] -3 5 3 6 7
            while queue and queue[-1][0] <= nums[i]:   # (1.1) remove any elements that < current num
                queue.pop()
            queue.append((nums[i], i))                 # (1.2) else append it: queue = [3, -1]
        result = [queue[0][0]]                         # (1.3) the max of first 3 element
        
        # (2) traverse from the index k
        r = k                                          
        while r < len(nums):
            if r - queue[0][1] >= k:                   # (2.2) remove 1st ele if it's out of window
                queue.pop(0)

            while queue and queue[-1][0] <= nums[r]:   # (2.3) remove any elements that < current num
                queue.pop()
            queue.append((nums[r], r))                 # (2.4) else append it: queue = [3, -1, -3]

            result.append(queue[0][0])                 # (2.5) update res: queue[0][0] always is max
            r += 1

        # (3) return res
        return result

# Time: O(n) since each element is processed twice - it's index added and then removed from queue.
# Space: O(n) = O(n-k+1) for output + O(k) for deque