# Method 1: brute force: sorting
# class Solution(object):
#     def medianSlidingWindow(self, nums, k):
#         # (0) edge case
#         if not nums:
#             return
        
#         # (1) initialize two pointers and result
#         res = []
#         l = 0
        
#         # (2) traverse the nums and get each sorted window
#         while l+k <= len(nums):
#             sort = sorted(nums[l:(l+k)])
            
#             if k % 2 == 1:                  # (2.1) k is odd
#                 median = sort[k//2]    
#             else:                           # (2.2) k is even
#                 median = (sort[(k-1)//2] + sort[k//2]) / 2
#             res.append(median)
            
#             l += 1
#         # (3) return result
#         return res
    
# Time: O((n-k+1)·k·logk): O(n-k) for traverse the nums and O(klogk) for sorting
# Space: O(n−k+1) extra linear space for the window container.



# Method 2: 
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        res, window = [], []
        
        for i in range(len(nums)):
            # Find position where outgoing element should be removed from
            if i >= k:
                # window.remove(nums[i-k])
                window.pop(bisect.bisect(window, nums[i-k]) - 1)

            # Maintain the sorted invariant while inserting incoming element
            bisect.insort(window, nums[i])

            # Find the medians
            if i >= k - 1:
                if k % 2 == 1:
                    median = float(window[k // 2])    
                else:
                    median = float((window[k//2 - 1] + window[k//2]) * 0.5)
                res.append(median)

        return res
    
# Time: O((n-k+1)·(k+logk)): O(n-k+1) is the number of window O(logk) for bisect.bisect, O(k) for bisect.insort
# Space: O(n−k+1) for result, O(k) for window container.